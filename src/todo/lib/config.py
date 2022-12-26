"""Translating environment variables to Python configuration."""

import os
from typing import NamedTuple

from dotenv import load_dotenv


class Config(NamedTuple):
    # Required:

    # Optional:
    timeout_seconds: float
    # Sentry reads its options from env.

    # Development only:
    debug: bool


if "TIMEOUT_SECONDS" not in os.environ:
    load_dotenv()

config = Config(
    # Required:
    #
    # Optional:
    timeout_seconds=float(os.getenv("TIMEOUT_SECONDS", "30")),
    #
    # Development only:
    debug=os.getenv("DEBUG", "").lower() == "true",
)
