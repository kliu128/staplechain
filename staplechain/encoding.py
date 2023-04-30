from brotli import compress, decompress

ALPHABET = [
    "\u200c",  # ZERO WIDTH NON-JOINER
    "\u200d",  # ZERO WIDTH JOINER
    "\u2060",  # WORD JOINER
    "\uFEFF",  # ZERO WIDTH NO-BREAK SPACE
]


def encode(data: bytes) -> str:
    # Each zero-width char is 2 bits, so we use 4 chars to represent 1 byte.
    output = ""
    for byte in data:
        for i in range(4):
            # Get the 2 bits of the byte at the current position.
            output += ALPHABET[(byte >> (i * 2)) & 0b11]

    return output


def decode(signature: str) -> bytes:
    # Each zero-width char is 2 bits, so we use 4 chars to represent 1 byte.
    output = bytearray()
    for i in range(0, len(signature), 4):
        # Get the 4 zero-width chars at the current position.
        byte = 0
        for j in range(4):
            byte |= ALPHABET.index(signature[i + j]) << (j * 2)
        output.append(byte)

    return bytes(output)


def encode_compressed(data: bytes) -> str:
    return encode(compress(data))


def decode_compressed(signature: str) -> bytes:
    return decompress(decode(signature))
