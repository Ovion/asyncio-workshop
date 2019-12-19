import asyncio

async def main():
    print("HEY")
    await asyncio.sleep(1)
    print("HO")

# Start event loop on main awaitable
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()