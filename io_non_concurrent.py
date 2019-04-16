import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    SITES = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20
    START_TIME = time.time()
    download_all_sites(SITES)
    DURATION = time.time() - START_TIME
    print(f"Downloaded {len(SITES)} in {DURATION} seconds")
