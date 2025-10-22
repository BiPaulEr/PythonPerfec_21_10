import asyncio
import time

async def worker(name):
    print(f"{name} STARTING")
    await asyncio.sleep(3)
    print(f"{name} FINISH") 
    return f"RESULT {name}"

def print_result(task):
    if task.done():
        print(task.result())

def print_result2(task):
    if task.done():
        print(task.result())
        
async def main():
    task1 = asyncio.create_task(worker("WORKER 1"))
    task2 = asyncio.create_task(worker("WORKER 2"))
    task1.add_done_callback(print_result)
    task2.add_done_callback(print_result2)
    await task1
    await task2
    
print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
