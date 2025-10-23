import asyncio
import time, random

async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}
    

async def main():
    liste_city = ["City1", "City2", "City3"]
    results = await asyncio.gather(*[fetch_weather(city) for city in liste_city])
    print(results) #[{'ville': 'City1', 'température': 17}, {'ville': 'City2', 'température': 22}, {'ville': 'City3', 'température': 17}]
    #[17, 22, 17]
    temperatures = []
    for item in results:
        temperatures.append(item["température"])
    print(sum(temperatures)/len(temperatures))

    sum(map(lambda dictionnaire : dictionnaire["température"], results))

print("MAIN - STARTING")
asyncio.run(main())
print("MAIN - FINISHING")
