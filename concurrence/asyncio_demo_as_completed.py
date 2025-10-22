import asyncio
import time, random

async def read_file(file_name):
    timetosleep = random.randint(1, 20)
    await asyncio.sleep(timetosleep)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully with {timetosleep} s")
    return(f"Contents of {file_name}")
    

async def main():
    for task in asyncio.as_completed([read_file(file) for file in ["data/file1.txt", "data/file2.txt", "data/file3.txt"]]):
        result = await task
        print(result)
    
print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
