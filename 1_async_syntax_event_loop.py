import asyncio

async def main():
    print("HEY")
    asyncio.sleep(1)
    print("HO")

# Start event loop on main awaitable
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("HOLA")
loop.close()