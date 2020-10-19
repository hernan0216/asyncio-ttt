import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    SITES = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20
    START_TIME = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(SITES))
    DURATION = time.time() - START_TIME
    print(f"Downloaded {len(SITES)} sites in {DURATION} seconds")
