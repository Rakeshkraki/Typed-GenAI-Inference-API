import asyncio

async def run_prog():
    print("starting...")
    await asyncio.sleep(1)
    print("completed...")

asyncio.run(run_prog())
