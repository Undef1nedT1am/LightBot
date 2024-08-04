import uvicorn
from PythonCore.util.ConfigUtil import Config
from PythonCore.util.Network import HttpEventNetwork
from starlette.applications import Starlette
from starlette.routing import Route
def start():
    eventServer = HttpEventNetwork(Config().noAsyncGetBotConfig()['bot']['httpEventHost'])
    app = Starlette(debug=True, routes=[Route("/", eventServer.PostHandle, methods=["POST"])])

    uvicorn.run(app, host=eventServer.httpEventHost, port=eventServer.httpEventPort)
