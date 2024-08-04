import aiohttp


class Network(object):
    def __init__(self):
        pass

    async def postJson(self, rtype, json):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.host}/{rtype}", json=json) as r:
                return await r.json()

