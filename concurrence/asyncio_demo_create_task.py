import asyncio
import time
async def worker(name):
    print(f"{name} STARTING")
    await asyncio.sleep(3)
    print(f"{name} FINISH")

async def main():
    task1 = asyncio.create_task(worker("WORKER 1"))
    task2 = asyncio.create_task(worker("WORKER 2"))
    await task1
    await task2
    
print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
