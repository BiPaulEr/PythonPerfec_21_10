import asyncio
import time, random

async def do_work(duration):
    await asyncio.sleep(duration)
    return f"Finisehd work in {duration} seconds"

async def main():
    liste_duree = [1, 2, 3, 4, 10]
    liste_task = [do_work(duration) for duration in liste_duree]
    for task in asyncio.as_completed(liste_task):
        result = await task
        print(result)
    
print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
