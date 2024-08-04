import aiohttp


class Network(object):
    def __init__(self, ptlName: str = "http", host: str = "http://localhost:3000"):
        self.ptlName = ptlName
        self.host = host

    async def postJson(self, rtype, json):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.host}/{rtype}", json=json) as r:
                return await r.json()

