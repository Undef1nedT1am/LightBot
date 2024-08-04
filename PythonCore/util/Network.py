import aiohttp


class Network(object):
    def __init__(self):
        self.host = "http://127.0.0.1:3000"

    async def postJson(self, rtype: object, json: object) -> object:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.host}/{rtype}", json=json) as r:
                return await r.json()

