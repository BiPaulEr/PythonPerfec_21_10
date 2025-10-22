import asyncio
import time, random

async def read_file(file_name):
    timetosleep = random.randint(1, 10)
    await asyncio.sleep(timetosleep)  # Simulate the delay of reading a file
    print(f"{file_name} read successfully with {timetosleep} s")
    return(f"Contents of {file_name}")
    

async def main():
    results = await asyncio.gather(*[read_file(file) for file in ["data/file1.txt", "data/file2.txt", "data/file3.txt"]])
    print(results) #['Contents of data/file1.txt', 'Contents of data/file2.txt', 'Contents of data/file3.txt']
    
print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
