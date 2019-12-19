import asyncio
import requests


async def getPokeapi(i):
  url = f"https://pokeapi.co/api/v2/pokemon/{i}"
  print(f"Requesting: {url}")

  # v1 - Sync
  #res = requests.get(url)

  # v2 - Async
  loop = asyncio.get_running_loop()
  res = await loop.run_in_executor(None, requests.get, url)

  
  # Process response
  data = res.json()["name"]
  print(f"Pokemon #{i} is -> {data}")

async def main():
  await asyncio.wait([getPokeapi(i) for i in range(1,9)])

# Start event loop on main awaitable
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()