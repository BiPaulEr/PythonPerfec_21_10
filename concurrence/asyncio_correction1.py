import asyncio
import time

async def read_file(file_name):
    await asyncio.sleep(1)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully")
    return(f"Contents of {file_name}")
    

async def main():
    tasks = []
    for file in ["data/file1.txt", "data/file2.txt", "data/file3.txt"]:
        tasks.append(asyncio.create_task(read_file(file))) #<class '_asyncio.Task'>
    for task in tasks:
        await task
    for task in tasks:
        print(task.result())
    
print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
