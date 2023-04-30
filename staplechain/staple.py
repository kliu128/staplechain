import base64
from datetime import datetime
import secrets
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


StapleID = str


def gen_id() -> StapleID:
    rand_id = base64.b32encode(secrets.token_bytes(16)).decode("ascii").replace("=", "")
    return "stpl-" + rand_id


class Staple(BaseModel, frozen=True):
    id: StapleID = Field(default_factory=gen_id)
    date: datetime = Field(default_factory=datetime.now)
    provider_id: str
    role: Literal["generation", "moderation", "application"]

    deps: Optional[list[StapleID]] = []
    params: Optional[dict[str, Any]] = None
    output: Optional[dict[str, Any]] = None
    sig: Optional[bytes] = None


class StapleChain(BaseModel, frozen=True):
    version: str
    # SHA3 hash of the completed text.
    hash: str
    chain: list[Staple]
