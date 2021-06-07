import asyncio

import aiohttp

request_object = {}
requests = [
    {
        "data": b"data",
        "params": {"key1": "value1", "key2": "value2"},
        "url": "http://httpbin.org/anything",
    },
    {
        "params": {"key1": "value1", "key2": "value2"},
        "url": "http://httpbin.org/anything",
        "json": {"test": "object"},
    },
]


async def main():
    urls = ["/", "/about/", "/register/", "/password-reset/"]
    async with aiohttp.ClientSession() as session:
        for request in requests:
            async with session.post(**request) as usePost:
                request_object[request.get("url")] = usePost.status
                print(usePost)

        for url in urls:
            async with session.get(f"http://127.0.0.1:8000{url}") as useFetch:
                request_object[url] = useFetch.status


async def usePost():
    urls = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(url)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(useFetch())


def requests():

    return request_object
