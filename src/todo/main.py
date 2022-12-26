"""TODO"""

import asyncio
import logging

import sentry_sdk

from todo.lib.config import config
from todo.lib.foo import foo

sentry_sdk.init()

logging.basicConfig(
    level=logging.DEBUG if config.debug else logging.INFO,
    datefmt="%Y-%m-%dT%H:%M:%S",
    format=(
        "{asctime}.{msecs:03.0f} {levelname} "
        "{process}:{name}:{funcName}:{lineno} {message}"
    ),
    style="{",
)

log = logging.getLogger("todo")


async def main() -> None:
    """TODO"""
    log.info("Started")
    log.info("TODO: await %s(...)", foo)
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
