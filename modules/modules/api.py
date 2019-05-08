import os

import aiohttp
import aiofiles
import zipfile

class Api:
    def __init__(self, host="localhost:8000"):
        self.host = host
        self.basepath = "http://"+host+"/api/current"

    async def _get(self, endpoint):
        if endpoint[0] != "/":
            endpoint = "/" + endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(self.basepath+endpoint) as response:
                return await response.json()

    async def _download(self, endpoint, filename="temp"):
        if endpoint[0] != "/":
            endpoint = "/" + endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(self.basepath+endpoint) as resp:
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await resp.read())
                await f.close()

    async def list(self):
        return await self._get("modules/")

    async def download(self, module, version):
        await self._download("modules/"+module+"/"+version, filename="temp.zip")
        with zipfile.ZipFile('test.zip', "r") as z:
            z.extractall(os.path.join("modules", module))
