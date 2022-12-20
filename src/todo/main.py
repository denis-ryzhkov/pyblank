"""TODO"""

import asyncio

import sentry_sdk

from todo.lib.foo import foo


async def main() -> None:
    sentry_sdk.init()
    # 1 / 0  # Sentry test
    print(f"TODO: await {foo}(...)")


if __name__ == "__main__":
    asyncio.run(main())
