import aiohttp

from PythonCore.util.ConfigUtil import Config

import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request


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
    def Server(self):
        async def PostHandle(request: Request):
            if request.method == "POST":
                data = await request.json()
                # Module Code










        app = Starlette(debug=True, routes=[Route("/", PostHandle, methods=["POST"])])
        uvicorn.run(app, host=self.httpEventHost, port=self.httpEventPort,log_level="warning")

