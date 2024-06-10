"""import asyncio
import random
async def func1():
    print(1)
    await asyncio.sleep(3)
    print(2)
   
async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)
   

async def main():
    await asyncio.gather(func1(), func2())
#asyncio.run(main())"""



"""async def a(sec):
    await asyncio.sleep(sec)
    print(f"a:{sec}")
async def b(sec):
    await asyncio.sleep(sec)
    print(f"b:{sec}")
async def main():
    while True:
        await asyncio.gather(
          asyncio.create_task(a(random.randint(1,5))),
          asyncio.create_task(b(random.randint(1,5)))
          )
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()"""


