# 🖇 StapleChain: Signed, In-band Annotations to Fingerprint Language Models

## Why?

So you're browsing the NYT, and you see the text "chic﻿⁠‍‌﻿﻿‍‌‍‌‌‌‌‌⁠⁠‌﻿⁠‌⁠⁠‌‌‌﻿⁠‍﻿‍﻿⁠‌‍⁠‍﻿⁠⁠‍﻿﻿‌﻿‌‍‍⁠⁠⁠‌‌⁠‍‌﻿‌﻿﻿‍﻿‍⁠﻿﻿‌⁠⁠‌‌⁠‌⁠⁠‌⁠‍‍﻿⁠‌⁠‌﻿⁠‍‍‍﻿‍‍﻿⁠﻿‍﻿‍‍‌﻿‍⁠﻿‌‍‍‍⁠﻿﻿‌⁠﻿﻿⁠‌‍‌⁠⁠﻿⁠‍⁠‍‌﻿‌﻿‌﻿⁠‍‍⁠⁠‌‍⁠‌﻿⁠﻿‌‍‌‍⁠‍﻿﻿﻿﻿‍⁠‌﻿‌‌﻿⁠⁠‍‌‌⁠‍⁠‌‌‍‍‌⁠‍⁠‌‌﻿﻿⁠‌‍﻿‍﻿‍﻿‌‍⁠‌﻿⁠‌⁠⁠﻿‌‍﻿﻿‍‍‌‌‌⁠‌‌‌‍‌﻿⁠‌﻿﻿‌⁠‌⁠﻿‌‌‌⁠‌‍﻿﻿‍⁠﻿‌⁠⁠⁠⁠﻿⁠‌‍⁠⁠﻿⁠﻿⁠‌‌‌﻿⁠‌⁠⁠‍‌⁠‍‌‍‍‌‌‌‌‌‍﻿‌‍‌‌⁠‍‌‌⁠⁠﻿‌‍﻿﻿⁠‍‌⁠﻿﻿⁠⁠﻿‌‌⁠‌﻿‍﻿﻿⁠‌‍⁠⁠‌⁠‍﻿‌‍‍⁠‌⁠﻿⁠⁠‌‍﻿‍⁠‌‌‍‌﻿‌‌‌‌‌‍‌⁠⁠‌‍‌﻿﻿‍‍‌‍‌‍﻿‌﻿‌‍﻿‌‍⁠﻿‍‍﻿‌﻿‌‍‍⁠‌⁠﻿‌⁠⁠﻿‌‌﻿‌﻿﻿⁠⁠‌‍‌⁠‌﻿⁠‍‍‍﻿‌‍‍⁠‌⁠⁠⁠‌‌‍⁠‍‍‌﻿⁠‌⁠‍﻿‌﻿‌‍﻿⁠‌﻿﻿‍⁠‌﻿﻿⁠﻿﻿⁠‌‍‍‌﻿‍﻿‌⁠‌⁠⁠‍⁠‍‍﻿‌‍‍﻿⁠﻿‍‌‍⁠﻿‍‍‌﻿‍‌﻿‌⁠﻿‌‍⁠﻿‌⁠‍⁠‍‌﻿‌﻿﻿‌‍‌﻿⁠‌‌‍‍‍⁠‍⁠‌‌‌‌﻿‌﻿⁠﻿‌‌‌⁠⁠⁠﻿⁠﻿‌﻿‌⁠‍﻿﻿‌﻿﻿‍‍‌﻿﻿‍﻿﻿﻿‍﻿﻿⁠⁠﻿⁠‍⁠‌‌⁠﻿﻿‌﻿⁠‌⁠‌﻿‍‍﻿⁠﻿⁠⁠⁠﻿﻿‍⁠‍﻿‍‌‍‌‍‌﻿﻿﻿‍⁠⁠‍﻿﻿⁠‍‍‍‌⁠‍﻿⁠⁠‍﻿‍‌‍‌‌⁠‍⁠‌‌‌⁠⁠⁠‌‍⁠﻿‌⁠﻿‍﻿﻿‌‌‍‌⁠⁠‍﻿﻿⁠‌‌﻿‍⁠⁠‍‍‌﻿‌﻿﻿‍‍‍‍﻿⁠‍⁠⁠⁠⁠﻿﻿⁠‌⁠‌‍‌‌﻿⁠‍‍‌﻿‌⁠﻿⁠‌﻿‌‌‌⁠‌﻿﻿‌‌‍﻿⁠‍‍⁠‌﻿‌‍‌‍⁠‍﻿‌⁠﻿‌﻿‌⁠﻿‌‌﻿‌﻿‌‌‌‌‌﻿⁠⁠‍﻿‌‌‍‌‌‌⁠⁠‌‌⁠‌‍﻿﻿⁠⁠﻿﻿⁠‍﻿‍﻿‌‌‍﻿⁠‍⁠⁠﻿‌‌‍﻿﻿‍﻿﻿⁠⁠⁠⁠‌⁠⁠‍‌﻿‍‍⁠﻿‍‍﻿﻿‍﻿﻿‌﻿﻿‍‌⁠‍‍⁠﻿﻿﻿﻿‍﻿‌‌ken!" Where'd that come from?

```python
>>> from staplechain.steganography import detect_staple_chains
>>> text = "chic﻿⁠‍‌﻿﻿‍‌‍‌‌‌‌‌⁠⁠‌﻿⁠‌⁠⁠‌‌‌﻿⁠‍﻿‍﻿⁠‌‍⁠‍﻿⁠⁠‍﻿﻿‌﻿‌‍‍⁠⁠⁠‌‌⁠‍‌﻿‌﻿﻿‍﻿‍⁠﻿﻿‌⁠⁠‌‌⁠‌⁠⁠‌⁠‍‍﻿⁠‌⁠‌﻿⁠‍‍‍﻿‍‍﻿⁠﻿‍﻿‍‍‌﻿‍⁠﻿‌‍‍‍⁠﻿﻿‌⁠﻿﻿⁠‌‍‌⁠⁠﻿⁠‍⁠‍‌﻿‌﻿‌﻿⁠‍‍⁠⁠‌‍⁠‌﻿⁠﻿‌‍‌‍⁠‍﻿﻿﻿﻿‍⁠‌﻿‌‌﻿⁠⁠‍‌‌⁠‍⁠‌‌‍‍‌⁠‍⁠‌‌﻿﻿⁠‌‍﻿‍﻿‍﻿‌‍⁠‌﻿⁠‌⁠⁠﻿‌‍﻿﻿‍‍‌‌‌⁠‌‌‌‍‌﻿⁠‌﻿﻿‌⁠‌⁠﻿‌‌‌⁠‌‍﻿﻿‍⁠﻿‌⁠⁠⁠⁠﻿⁠‌‍⁠⁠﻿⁠﻿⁠‌‌‌﻿⁠‌⁠⁠‍‌⁠‍‌‍‍‌‌‌‌‌‍﻿‌‍‌‌⁠‍‌‌⁠⁠﻿‌‍﻿﻿⁠‍‌⁠﻿﻿⁠⁠﻿‌‌⁠‌﻿‍﻿﻿⁠‌‍⁠⁠‌⁠‍﻿‌‍‍⁠‌⁠﻿⁠⁠‌‍﻿‍⁠‌‌‍‌﻿‌‌‌‌‌‍‌⁠⁠‌‍‌﻿﻿‍‍‌‍‌‍﻿‌﻿‌‍﻿‌‍⁠﻿‍‍﻿‌﻿‌‍‍⁠‌⁠﻿‌⁠⁠﻿‌‌﻿‌﻿﻿⁠⁠‌‍‌⁠‌﻿⁠‍‍‍﻿‌‍‍⁠‌⁠⁠⁠‌‌‍⁠‍‍‌﻿⁠‌⁠‍﻿‌﻿‌‍﻿⁠‌﻿﻿‍⁠‌﻿﻿⁠﻿﻿⁠‌‍‍‌﻿‍﻿‌⁠‌⁠⁠‍⁠‍‍﻿‌‍‍﻿⁠﻿‍‌‍⁠﻿‍‍‌﻿‍‌﻿‌⁠﻿‌‍⁠﻿‌⁠‍⁠‍‌﻿‌﻿﻿‌‍‌﻿⁠‌‌‍‍‍⁠‍⁠‌‌‌‌﻿‌﻿⁠﻿‌‌‌⁠⁠⁠﻿⁠﻿‌﻿‌⁠‍﻿﻿‌﻿﻿‍‍‌﻿﻿‍﻿﻿﻿‍﻿﻿⁠⁠﻿⁠‍⁠‌‌⁠﻿﻿‌﻿⁠‌⁠‌﻿‍‍﻿⁠﻿⁠⁠⁠﻿﻿‍⁠‍﻿‍‌‍‌‍‌﻿﻿﻿‍⁠⁠‍﻿﻿⁠‍‍‍‌⁠‍﻿⁠⁠‍﻿‍‌‍‌‌⁠‍⁠‌‌‌⁠⁠⁠‌‍⁠﻿‌⁠﻿‍﻿﻿‌‌‍‌⁠⁠‍﻿﻿⁠‌‌﻿‍⁠⁠‍‍‌﻿‌﻿﻿‍‍‍‍﻿⁠‍⁠⁠⁠⁠﻿﻿⁠‌⁠‌‍‌‌﻿⁠‍‍‌﻿‌⁠﻿⁠‌﻿‌‌‌⁠‌﻿﻿‌‌‍﻿⁠‍‍⁠‌﻿‌‍‌‍⁠‍﻿‌⁠﻿‌﻿‌⁠﻿‌‌﻿‌﻿‌‌‌‌‌﻿⁠⁠‍﻿‌‌‍‌‌‌⁠⁠‌‌⁠‌‍﻿﻿⁠⁠﻿﻿⁠‍﻿‍﻿‌‌‍﻿⁠‍⁠⁠﻿‌‌‍﻿﻿‍﻿﻿⁠⁠⁠⁠‌⁠⁠‍‌﻿‍‍⁠﻿‍‍﻿﻿‍﻿﻿‌﻿﻿‍‌⁠‍‍⁠﻿﻿﻿﻿‍﻿‌‌ken!"
>>> detect_staple_chains(text)[0]
StapleChain(
    version='1',
    hash='4ff7a9d3d17507261730c7c204af1352673009d72a19ea2c35a9bee133bfb9b7',
    chain=[
        Staple(
            id='stpl-PHNMCDB457MDKDLVNENU6SUHFM',
            date=datetime.datetime(2023, 4, 30, 16, 21, 48, 783756),
            provider_id='stapler/openai.com/chatcmpl-7BAeShUEQGYrz8h3xI9NKffelPFQK',
            role='generation',
            deps=[],
            params={
                'prompt_hash': 'e83a235d3ec1ec9d08f7b2d95aafe962ad57e05106ffe6e0cb4042cf05b03e44',
                'model': 'gpt-3.5-turbo-0301',
                'max_tokens': 10
            },
            output=None,
            sig=None
        )
    ]
)
```

## Usage

## Installation

```bash
pip install staplechain
```