# re-export everything from openai but override completion functions

import asyncio
import hashlib
import json
from logging import getLogger
from typing import Any, Optional, cast
from typing_extensions import override
import openai
from openai import *

from staplechain.staple import Staple
from staplechain.steganography import add_staple, clean_text, detect_staple_chains

logger = getLogger(__name__)


async def async_completion_wrapper(
    fn, *args, prompt: Optional[str] = None, messages: Optional[dict] = None, **kwargs
):
    text = prompt or json.dumps(messages)

    # Track implicit previous textual dependencies
    deps = list(detect_staple_chains(text))

    # Clear out ZWJ characters from the prompt to avoid confusing the model
    if prompt:
        output = cast(Any, await fn(*args, prompt=clean_text(prompt), **kwargs))
    elif messages:
        output = cast(
            Any,
            await fn(
                *args,
                messages=[
                    {
                        **message,
                        "content": clean_text(message["content"]),
                    }
                    for message in messages
                ],
                **kwargs
            ),
        )
    else:
        raise ValueError("Must provide either prompt or messages")

    # Generate a staple chain and embed it
    staple = Staple(
        provider_id="stapler/openai.com/" + output.id,
        role="generation",
        deps=[dep.chain[-1].id for dep in deps],
        params={
            "prompt_hash": hashlib.sha3_256(text.encode("utf-8")).hexdigest(),
            **kwargs,
        },
    )

    for choice in output.choices:
        if output.object == "text_completion":
            choice.text = add_staple(staple, choice.text)
        elif output.object == "chat.completion":
            choice.message.content = add_staple(staple, choice.message.content)
        else:
            raise ValueError("Unknown choice type")

    return output


class Completion(openai.Completion):
    @override
    @classmethod
    def create(cls, *args, prompt: str, **kwargs):
        return asyncio.run(
            async_completion_wrapper(super().acreate, *args, prompt=prompt, **kwargs)
        )

    @override
    @classmethod
    async def acreate(cls, *args, prompt: str, **kwargs):
        return await async_completion_wrapper(
            super().acreate, *args, prompt=prompt, **kwargs
        )


class ChatCompletion(openai.ChatCompletion):
    @override
    @classmethod
    def create(cls, *args, messages: dict, **kwargs):
        return asyncio.run(
            async_completion_wrapper(
                super().acreate, *args, messages=messages, **kwargs
            )
        )

    @override
    @classmethod
    async def acreate(cls, *args, messages: dict, **kwargs):
        return await async_completion_wrapper(
            super().acreate, *args, messages=messages, **kwargs
        )
