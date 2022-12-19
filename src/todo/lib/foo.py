"""TODO"""

import httpx


async def foo(query: str) -> str:
    """TODO

    Args:
        query: TODO

    Returns:
        TODO
    """
    async with httpx.AsyncClient() as ahttpx:
        response = await ahttpx.post(
            "http://localhost:4242/foo",
            headers={"authorization": "Bearer REDACTED"},
            json={"query": query},
            timeout=10,
        )

    return response.json()["data"]
