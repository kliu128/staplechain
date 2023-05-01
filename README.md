# 🖇 StapleChain: Signed, In-band Annotations for Language Model Outputs

## Why?

So you're browsing the NYT, and you see some suspicious LM-generated text. Where'd that come from?

```python
>>> from staplechain.steganography import detect_staple_chains
>>> text = 'What is the answer to life, the universe, and everything?" The answer is 42, according to Douglas Adams in his book, "The Hit﻿⁠‍‌﻿‍‍﻿⁠‌‌‌‌‌‌‌‌﻿‍‌﻿‍‌‌⁠﻿⁠‍‌﻿⁠⁠‌﻿‌﻿⁠﻿‌‍‌‌‍﻿‌‌﻿﻿‌﻿⁠﻿⁠‍‌⁠‍⁠‍﻿⁠‍‍﻿‌‍﻿⁠﻿‌﻿‌﻿⁠‌⁠‌‍‌‍﻿⁠﻿⁠‍‍‌‍⁠‍‍‌‍⁠⁠⁠‍﻿﻿﻿﻿‍﻿﻿‍‍‍‍‍‌⁠⁠﻿‌‍‌‌‌⁠‌﻿‌‍‍﻿‍﻿‌﻿﻿⁠‌‌﻿‌‌‌‌﻿⁠﻿‌﻿﻿‌﻿﻿‌‌‍‍⁠‌⁠‌⁠⁠‌⁠⁠﻿﻿‍‍‍‍‍‌‍﻿‌⁠‍⁠﻿‌‌‌‌‍⁠⁠‌⁠⁠﻿﻿‌‍‌‍﻿‌‌‌﻿⁠‌﻿‌‍﻿⁠‌﻿⁠‌‌﻿‌‌﻿‌‌‍﻿﻿‌‍﻿‍⁠﻿⁠‍⁠⁠‍‌‌⁠⁠‌⁠﻿⁠‍⁠‍﻿‌⁠‍﻿﻿‍‌‌⁠﻿﻿﻿‌‌‍‌‌﻿⁠‌⁠‍‍‌‍﻿‍﻿﻿﻿‍‍‌‌‌⁠﻿﻿‍﻿⁠‌‌‌‌‌‌‍‌‌‌‍⁠﻿‌‌‌‍‍‍‍‍‍‌‍﻿⁠﻿﻿﻿⁠⁠‍⁠﻿⁠‌⁠‌‌‌‍‌﻿⁠⁠‍‍‍‍⁠‌‍‍‍‌‍‍‍‌⁠﻿‍‌﻿⁠﻿‍﻿‌‌‍‌⁠‌‌﻿﻿‌‌‌﻿‍﻿﻿‌﻿‍‍⁠‍‌‍⁠⁠⁠‍⁠‌‍‍⁠‌‍﻿‌﻿‌⁠‍⁠﻿‌‍‌‍⁠‌‍﻿‌‍‌‍‌‌﻿‍﻿‍⁠‌‍⁠‍‌﻿﻿‌‌‌‍‌⁠⁠‍‌‍‍⁠⁠⁠‌‍﻿⁠‍‌⁠‍‌‍‌﻿‍⁠⁠‍﻿‍‍‌‍‍⁠‌‍‍⁠‌⁠‍⁠‌‍‌‍⁠‌⁠‍‌﻿﻿‌‌‍‍‍⁠﻿‍‍‌‌⁠‍﻿‌‍﻿⁠⁠﻿﻿﻿‍‍‌‌﻿‍⁠﻿‌‌‍‌‌⁠﻿﻿‍﻿‌⁠﻿‍‍﻿﻿‍﻿⁠‌﻿⁠﻿⁠‍‌‌﻿‍‍‌﻿‌‌‌⁠﻿﻿⁠‌﻿⁠⁠‌﻿⁠‌⁠⁠⁠﻿﻿‌‌﻿⁠‍⁠‌﻿⁠⁠‍‍‍‍‍⁠‍‍‍‍‍‍‍⁠﻿‌‍﻿‍⁠‍﻿‌⁠﻿‍⁠⁠‍﻿⁠⁠⁠﻿‍‍﻿‍﻿⁠﻿‍‍﻿﻿﻿‍⁠﻿‍﻿‌‍‌‌‍⁠﻿‌‌‌‌‍﻿‌‌‌‌‌‌﻿﻿﻿‍⁠‌‌‌‌⁠⁠‌⁠‍⁠⁠‌﻿‌‌⁠‌⁠‍⁠﻿‌‌‍⁠‍‌⁠﻿‍⁠‌‌‍‌‍⁠‍‍‌‌⁠﻿⁠‍⁠⁠‌‌‌‍‌‍‍‍⁠﻿‍﻿‌⁠‌‌‍‍⁠‌‌⁠﻿‌﻿‌‌‍⁠⁠‌﻿‍﻿﻿‌⁠‌⁠⁠‍﻿⁠﻿﻿‌⁠‍﻿⁠⁠⁠⁠‍‍﻿⁠‌⁠⁠‌⁠﻿﻿⁠‌‌⁠‌⁠⁠﻿‍⁠‍‍⁠‍﻿﻿‌﻿﻿﻿‍⁠⁠‌‍‍‌‍﻿﻿⁠‌‌⁠﻿﻿﻿⁠﻿‍⁠‍﻿‍﻿‌‌⁠⁠⁠⁠⁠‌‍‍‍⁠‌‍‌‌‍⁠⁠‌⁠‌﻿﻿﻿﻿‍⁠﻿﻿‌﻿⁠﻿‍‍‍‌‍﻿‍⁠‍⁠‍‍‍‍﻿‌‍‍‍‍‍‍﻿‍‌⁠⁠﻿﻿‍‌﻿‌‍﻿‍‌⁠﻿﻿﻿‌﻿‌﻿‌﻿⁠﻿﻿‍‌‍﻿‍﻿‍‍‌﻿‌‌﻿‌⁠﻿‍‍‌﻿﻿﻿⁠‌﻿﻿‌‍﻿‍﻿⁠‌﻿⁠⁠‌‍‍⁠⁠‌﻿⁠‌⁠⁠﻿‌﻿⁠‌‌﻿‍‍‌﻿‌﻿⁠﻿‍‍﻿‍‍⁠‍‍﻿﻿⁠‍﻿‌﻿‍‌‌⁠⁠﻿‍⁠⁠﻿⁠⁠‌‌‌﻿﻿﻿⁠‍⁠‌﻿﻿⁠﻿⁠﻿⁠﻿‍⁠‍﻿﻿⁠‍﻿⁠﻿‍‍‍⁠⁠⁠﻿⁠‌﻿⁠⁠‍‍﻿⁠﻿‍﻿﻿⁠⁠‌‍﻿⁠‍‍⁠‍‌⁠‍⁠﻿⁠‍⁠‌‍⁠⁠‍‍⁠⁠‍﻿‌‌⁠‍‍⁠⁠⁠﻿‌⁠‌‌﻿‍‌﻿⁠﻿‌﻿‍⁠‌‍⁠‌⁠‌‌‍﻿‌‍⁠‌﻿⁠⁠﻿‌﻿﻿⁠⁠‍﻿‍﻿﻿‌‍⁠‌⁠⁠﻿‌⁠‌⁠‌‌‍⁠‌‍‍‍⁠‍‌‌﻿⁠⁠‌‍‍⁠‌⁠﻿‌‍‌‍﻿‌‍⁠‍‍‍⁠⁠﻿‌⁠‍‌‍‍⁠‌⁠‌﻿‌⁠⁠﻿‍﻿⁠‍‌⁠‌‌﻿‌‍‌‍‍‍‍⁠﻿‌⁠‍⁠﻿⁠﻿‌‌‌⁠﻿‌⁠‍⁠‍﻿﻿⁠‍‌‌‍⁠‍‍⁠﻿‍‍‌‌‌﻿﻿‍﻿⁠﻿‍﻿﻿﻿‍‍‌﻿‍﻿﻿‌‍‌‌‍‌﻿‌﻿‌‌﻿‌‍‌‌⁠‌‍‌﻿⁠‍﻿﻿﻿⁠⁠‍﻿﻿‍﻿‍‌﻿﻿﻿⁠⁠⁠﻿‍‍‍‌‌‌‍‍‍‌⁠‌﻿﻿﻿﻿﻿‍‍‌⁠﻿⁠﻿﻿﻿﻿‌﻿⁠‍‌‌﻿‍‍﻿‌‌﻿﻿⁠‍‍‌‌﻿﻿⁠⁠﻿‍⁠﻿﻿‌⁠⁠﻿‌‌‌‌‌⁠‌⁠‍﻿﻿⁠‌‌⁠﻿﻿﻿﻿‌‌‌﻿‌‌⁠‍‍‌‌﻿⁠⁠⁠‌‍‍‌﻿‍‌﻿‌‍﻿⁠‍‌﻿‌⁠⁠⁠‍‍﻿⁠⁠‌⁠﻿﻿‌﻿﻿⁠⁠‌‍﻿﻿﻿‍⁠‌﻿‌⁠﻿‍⁠‌‍‍﻿‍‍‍‍﻿﻿‌⁠﻿⁠‌‍‍⁠﻿‌⁠⁠⁠‌⁠﻿‌‌‍⁠‌‍⁠⁠﻿‌﻿﻿‌⁠‍‍‌⁠‌‍‌﻿⁠‌‌‍‍‌⁠⁠﻿‍‌﻿‌﻿⁠‌‍﻿⁠‌‌﻿﻿⁠﻿﻿﻿‌‍‍‌‌‍‌‌﻿⁠‌‍‌‌⁠⁠‍﻿‌﻿‌‍‍‍﻿‍⁠⁠‌﻿‍﻿﻿‍⁠⁠﻿‍‍‍‌‍‌⁠‍‌﻿‌‍‌‍⁠﻿‍‍‍‌‍‍﻿‍﻿﻿﻿‍⁠⁠‌‌‌⁠‌⁠‍﻿‌‌‍﻿‌﻿⁠﻿⁠‌‍⁠﻿﻿‍‍‌‌﻿‍⁠⁠﻿‌‌‌⁠﻿‌‍‌⁠﻿‌﻿﻿‌⁠‍‌﻿⁠⁠‌⁠﻿‍⁠‍⁠⁠‍⁠‍⁠‍﻿﻿⁠﻿⁠﻿⁠‌⁠‍‍⁠‌‌﻿﻿﻿﻿‌⁠﻿‍‍﻿‌‍﻿﻿‍⁠﻿‍‌‌‌⁠‍⁠‌﻿﻿﻿﻿⁠⁠﻿‌‌⁠‍‍﻿⁠‍﻿﻿﻿﻿‍‌chhiker's Guide to the Galaxy." However, many believe it to be a joke or a philosophical concept rather than a literal answer.'
>>> list(detect_staple_chains(text))[0]
    StapleChain(
        version='1',
        hash='145d1aa76725c0c9114d4c46e29ff833b5f8154b634d12e678931b8be6219f1e',
        chain=[
            Staple(
                id='stpl-XP4YDXGQI3JDZE42VSUJNMNOWI',
                date=datetime.datetime(2023, 4, 30, 16, 49, 17, 957543),
                provider_id='stapler/openai.com/chatcmpl-7BB51A4zwNAb9ZI7EQcS2QzVavMXQ',
                role='generation',
                deps=[],
                params={
                    'prompt_hash': '88cc78a3049f86ada2b140bb67899fabc8b21eb15626da660f2fa6b3216ecadd',
                    'model': 'gpt-3.5-turbo-0301',
                    'max_tokens': 256,
                },
                output=None,
                sig=None,
            ),
            Staple(
                id='stpl-PX3DAS2HRJZ4WDOTSTG7N466RA',
                date=datetime.datetime(2023, 4, 30, 16, 49, 18, 56057),
                provider_id='your-moderation-api.com/moderations/001',
                role='moderation',
                deps=[],
                params=None,
                output={
                    'hate': 0.007,
                    'spam': 0.001,
                    'nsfw': 0.0001,
                },
                sig=None,
            ),
        ],
    ) (StapleChain)
```

With StapleChain, you can track the provenance of every piece of text generated by your AI models. This is useful for:

1. **Debugging**: If you notice a problem with your model, you can trace it back to the prompt that caused it using the text alone.
2. **Dependency tracking**: If you have a chain of prompts, StapleChain detects when your input has a staple and marks it as a dependency of your output. You can use this to reconstruct graphs of text that affected your generation, which is helpful for observability (trust and safety) and prompt engineering.
3. **Moderation**: Until language models become safe, you should always run a moderation system over your AI-generated text. StapleChain lets you programmatically verify this: before showing untrusted text to the user, check that the text contains a moderation staple from your provider of choice.
4. **Non-repudiation**: StapleChain contains support for signature fields, which sign the hash of the completion along with its staple chain. This lets you prove that a completion was generated by a particular model, much like [DKIM for email](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), **even if you didn't develop the model or application that created it**.
5. **Data confidentiality**: You can use staples to ensure private info isn't carelessly leaked via copy-paste. For example, if you're using a chatbot to answer questions using customer data, you can use staples to verify that your employees aren't _accidentally_ copy-pasting chatbot responses. (Of course, this doesn't prevent malicious actors from removing the staple.) Think of it like [opportunistic security](https://en.wikipedia.org/wiki/Opportunistic_encryption) for LLMs.

More broadly, StapleChain is a proof-of-concept for what strong typing and auditability could mean for language models. As LLMs go mainstream, lots of classical CS problems (signatures, verification, typing) are rearing their head again. StapleChain is a first step towards solving these problems for AI.

## How does it work?

The string above actually has a long sequence of non-printable characters right in the middle. These encode a Brotli-compressed JSON object, which contains the staple chain. Because the data is stored in-band:

- It's invisible to the end user, so you can leave the staples in your frontend to observe usage. For example, if you're making an internal chatbot for your company, you can use staples to figure out if any assistant-generated text leaks externally.
- You can introduce staple chains into your existing LLM application without modifying any code or data structures. If you already log prompts & completions, you already support staples! You can add support with one line of code:

  ```diff
  -import openai
  +import staplechain.shims.openai as openai
  ```

  Our shim automatically strips staples before calling the API, and appends staples in the response.

## Limitations

This is a proof-of-concept and should not be used in production without reviewing it to make sure it matches your needs. PRs welcome!

Known issues:

- **Structured output**: The staple injection will make most parsers (JSON, YAML, etc.) error out. This could be fixed by introducing multiple encoding methods based on the output type -- e.g. adding a field for JSON, adding a comment for YAML/code, etc. However, this also makes signature verification a bit more complicated, and it requires specialized encoders for each genre of text.
- **Provenance of reworded/partial/substrings of completions**: Right now, the staple chain stores the full SHA3 hash of the output text. However, any trivial modification will make the chain fail to validate. This could be fixed with a space-efficient way to verify that a string is a substring of the original completion (Bloom filters, maybe?), but for simplicity of implementation I've just stuck with a normal hash for now.
- **Signature verification**. It's not actually implemented yet.

## FAQ

### Why not use out-of-band metadata?

Out of band metadata is useful, but:

- You need to modify your existing data structures to support it, which undermines some of the flexibility of language models (it's just text-to-text!).
- It's not robust to copy-paste. Ideally, staples should be strongly attached to the text they represent, so that you can't accidentally remove them by simply doing `.text`.

Out of band metadata probably has its place though, depending on the use case.

### What's the ideal future for StapleChain?

Ideally, StapleChain becomes the **reference standard** for LLM providers, moderation platforms, and end-user applications to record completion/moderation/display actions on LLM-generated text. In a future where, e.g. OpenAI signs all completions with a staple chain, you can check any internet text and, if a staple is present, know that it came from an AI.

It also enables best practices like "apply moderation to all untrusted completions" to be enforced via code and/or regulation. Best practices and policy should dictate that all AI-generated text is stapled, and that all stapled text is moderated. This might help avoid future safety issues similar to Bing Chat's moderation fails and make the entire process more transparent + verifiable to the end user.

## Usage

```bash
pip install staplechain
```

Then, use the `staplechain.shims` module to wrap your favorite LLM API (currently only OpenAI is supported, PRs welcome):

```diff
-import openai
+import staplechain.shims.openai as openai
```

You can also use the manual encoding functions in the repo. To see how they work, check out the code; it's very short because I wrote it in a day.

## Contact

If you have any questions or suggestions for this line of work, feel free to reach out. My email is kevin@kliu.io.

If you want to contribute, feel free to submit a PR! I don't have any expectations for this project, but I'm happy to accept useful contributions.
