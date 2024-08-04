import aiohttp

from PythonCore.util.ConfigUtil import Config


from starlette.requests import Request
from starlette.responses import PlainTextResponse

class Network(object):
    def __init__(self):
        self.botConfigs = Config().noAsyncGetBotConfig()['bot']
        self.host = ""
        self.httpEventHost = ""
        self.protocol = "http" if self.botConfigs['protocols'] in ["01", "10"] else "ws-forward" if self.botConfigs[
                                                                                                        'protocols'] == "2" else "ws-backward"  # noqa: E501

        if self.protocol == "http":
            self.host = self.botConfigs['forwardHttpHost']
            self.httpEventHost = self.botConfigs['httpEventHost']
        elif self.protocol == "ws-forward":
            self.host = self.botConfigs['forwardWebSocketHost']
        elif self.protocol == "ws-backward":
            self.host = self.botConfigs['backwardWebSocketHost']

    async def postJson(self, rtype: object, json: object) -> object:
        if self.protocol == "http":
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{self.host}/{rtype}", json=json) as r:
                    return await r.json()

class HttpEventNetwork:
    def __init__(self, httpEventHost):
        self.httpEventHost = httpEventHost.split(':')[0]
        self.httpEventPort = httpEventHost.split(':')[1]
    async def PostHandle(self, request: Request):
                if request.method == "POST":
                    data = await request.json()
                    print(data)
                return PlainTextResponse("6")
                    # Module Code












