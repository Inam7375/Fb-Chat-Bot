from fbchat import Client, log
from fbchat.models import *
import apiai, codecs, json

class echoBot(Client):

    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "12a77c5cc58442e4a3767566b13b4ac7"
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'de'
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
            
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        self.apiaiCon()

        self.request.query = message_object.text
 
        response = self.request.getresponse()

        #reader = codecs.getdecoder("utf-8")

        obj = json.load(response)

        reply = obj['result']['fulfillment']['speech']
        
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

client = echoBot('inam.ali211@hotmail.com', 'Pak211rwp')
client.listen()








