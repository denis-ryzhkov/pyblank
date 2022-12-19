"""TODO"""

import sentry_sdk

from todo.lib.foo import foo


def main() -> None:
    sentry_sdk.init()
    # 1 / 0  # Sentry test
    print(f"TODO: {foo}")


if __name__ == "__main__":
    main()
