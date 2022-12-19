import pytest
from pytest_mock import MockerFixture

from todo.lib.foo import foo

pytestmark = pytest.mark.anyio


async def test_foo(mocker: MockerFixture) -> None:
    asyncClient = mocker.patch("httpx.AsyncClient").return_value
    asyncClient.__aenter__ = mocker.AsyncMock()
    post = asyncClient.__aenter__.return_value.post
    post.return_value.json = mocker.Mock(return_value={"data": "DATA"})

    data = await foo("QUERY")

    post.assert_awaited_once_with(
        "http://localhost:4242/foo",
        headers={"authorization": "Bearer REDACTED"},
        json={"query": "QUERY"},
        timeout=10,
    )

    assert data == "DATA"
