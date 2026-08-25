import asyncio


async def fetch(url: str):
    await asyncio.sleep(2)
    return f"Data from {url}"


async def main():

    results = await asyncio.gather(
        fetch("google.com"),
        fetch("github.com"),
        fetch("openai.com"),
    )

    print(results)


asyncio.run(main())