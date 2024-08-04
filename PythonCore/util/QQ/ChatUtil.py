from PythonCore.util.Network import Network
from PythonCore.util.OtherUtil import Logger


class Chat(object):
    def __init__(self):
        self.network = Network()
        self.logger = Logger()
    def buildSendMsgJson(self, msgType: str, id: int, text: str):
        """Make a json object for sending msg
        :param msgType: str must be private or group
        :param id: int the id of user or group
        :param text: str text to send"""
        data = \
            {
                "message_type": msgType,
                "user_id" if msgType == "private" else "group_id": id,
                'message': [{
                    'type': 'text',
                    'data': {
                        'text': text
                    }
                }]
            }
        return data

    async def sendMsg(self, msgType, id, text):
        """Send a message to user or group
        Args look at buildSendMsgJson()"""
        data = await self.network.postJson(
            "send_msg", self.buildSendMsgJson(msgType, id, text))
        print(data)
        if data['status'] == "ok":
            await self.logger.success(f"Sent message successfully. Message Id:{data['data']['message_id']}")
        else:
            await self.logger.error(f"Sent message fail. {data['message']}. Message Id:{data['data']['message_id']}")

