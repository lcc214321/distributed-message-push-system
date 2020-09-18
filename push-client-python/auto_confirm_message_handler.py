
import json
from client_message import *
from client import *
class AutoConfirmMessageHandler():

  def __init__(self, callback, client: Client):
    self.callback = callback
    self.client = client

  def handle(self, msg):
    try:
      maps = json.loads(msg)
      clientMessage = ClientMessage()
      clientMessage.messageId = maps['messageId']
      clientMessage.messageType = maps['messageType']
      clientMessage.payload = maps['payload']
      self.callback(clientMessage)
      self.client.send('confirm-' + clientMessage.messageId)
    except:
      print ('接收到非结构化消息:' + msg)
    

handler = AutoConfirmMessageHandler()
data = {
  'messageId': '1',
  'messageType': 'common'
}
handler.handle('comm')