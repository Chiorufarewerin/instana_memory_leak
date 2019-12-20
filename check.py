import asyncio
import requests
import time


@asyncio.coroutine
def main():
    loop = asyncio.get_event_loop()
    for i in range(10000):
        loop.run_in_executor(None, requests.get, f'http://0.0.0.0:8000/{i}')
    time.sleep(10)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
