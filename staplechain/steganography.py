import hashlib
from itertools import chain
import json
from logging import getLogger
from typing import Generator


from staplechain.encoding import ALPHABET, decode_compressed, encode_compressed
from staplechain.staple import Staple, StapleChain


logger = getLogger(__name__)


def detect_staple_chains(text: str) -> Generator[StapleChain, None, None]:
    # Get contiguous runs of ZWJ characters
    runs = []

    current_run = ""
    for c in text:
        if c in ALPHABET:
            current_run += c
        else:
            if current_run:
                runs.append(current_run)
                current_run = ""
    if current_run:
        runs.append(current_run)

    logger.info("Found %d runs of potential staples", len(runs))

    # Now, try to decode each of these into StapleChains
    for run in runs:
        try:
            data = decode_compressed(run).decode("utf-8")
            chain = StapleChain(**json.loads(data))

            logger.info("Found chain ending in: %s", chain.chain[-1].id)

            yield chain
        except:
            logger.exception("Failed to decode potential staple chain")


def clean_text(text: str) -> str:
    # Clear out ZWJ characters from the prompt
    for char in ALPHABET:
        text = text.replace(char, "")

    return text


def _add_staple_chain(chain: StapleChain, text: str) -> str:
    loc = int(len(text) / 2)
    return (
        text[:loc]
        + "".join(encode_compressed(chain.json().encode("utf-8")))
        + text[loc:]
    )


def add_staple(staple: Staple, text: str) -> str:
    """
    Embeds a staple into a piece of text. If there's already a staple chain in the text, it will be appended to. Otherwise, a new staple chain will be created.
    """

    assert not staple.sig, "Staple already has a signature, cannot add."

    # First, try to detect an existing staple chain
    chains = list(detect_staple_chains(text))
    assert len(chains) <= 1, "Found multiple staple chains in text"
    if chains:
        chain = chains[0]
        # Validate the chain
        assert (
            hashlib.sha3_256(clean_text(text).encode("utf-8")).hexdigest() == chain.hash
        ), "Staple chain's hash does not match text's hash"

        # Append the staple to the chain
        chain.chain.append(staple)
    else:
        chain = StapleChain(
            version="1",
            hash=hashlib.sha3_256(clean_text(text).encode("utf-8")).hexdigest(),
            chain=[staple],
        )

    # Embed the chain into the text
    return _add_staple_chain(chain, clean_text(text))
