import asyncio

async def main(p):
  raise ValueError(f"Invalid params {p}")

def handler(loop, context):
  print("Error")
  loop.stop()

loop = asyncio.get_event_loop()
loop.set_exception_handler(handler)
loop.create_task(main("HEY"))
loop.run_forever()