import asyncio
import aiohttp

class HttpSessionManager():
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self.session
        
    async def __aexit__(self, exception_type, exception_instance, traceback):
        await self.session.close()
        return True

async def main():
    async with HttpSessionManager() as session:
        headers = {"Accept": "text/plain"}
        response = await session.get("https://icanhazdadjoke.com", headers=headers)
        if response.status == 200:
            result = await response.text()
            print(result)

asyncio.run(main())