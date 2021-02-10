# aiooncue
Python API for Kohler Oncue

Example
```
import asyncio
import pprint

import aiohttp
from aiooncue import Oncue


async def main():
    websession = aiohttp.ClientSession()
    oncue = Oncue("username", "password", websession)
    await oncue.async_login()
    devices = await oncue.async_list_devices()
    for device in devices:
        serialnumber = device["serialnumber"]
        data = await oncue.async_device_details(serialnumber)
        pprint.pprint([serialnumber, data])
    await websession.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
