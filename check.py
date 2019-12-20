import asyncio
import requests
import time


@asyncio.coroutine
def main():
    loop = asyncio.get_event_loop()
    i = 0
    while True:
        loop.run_in_executor(None, requests.get, f'http://web-leaked:8000/{i}')
        time.sleep(0.1)
        print(f'query {i}')
        i += 1


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
