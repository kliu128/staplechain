from typing import Generator
import pybloomfilter


def generate_substrings(text: str, chunk_size: int) -> Generator[str, None, None]:
    for i in range(0, len(text), chunk_size):
        for j in range(i + chunk_size, len(text) + 1, chunk_size):
            yield text[i : i + j]


def create_bloom_filter(text: str) -> bytes:
    substrings = list(generate_substrings(text, 4))

    filter = pybloomfilter.BloomFilter(len(substrings), 0.001, "/tmp/x")
    filter.update(substrings)

    return filter.to_base64()
