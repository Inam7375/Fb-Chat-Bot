#importing modules needed for this application (if you have'nt already then pip install all the modules)
#if you don't know how to pip install, visit https://docs.python.org/3/installing/index.html
from fbchat import Client, log
from fbchat.models import *
import apiai, codecs, json
import Credentials

#making class for bot
class Bot(Client):

#opening connection
    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "12a77c5cc58442e4a3767566b13b4ac7" #access token of dailogflow api
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'de' #default language = english
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

#recieving message
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
            
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        self.apiaiCon()

        self.request.query = message_object.text

 #giving response
        response = self.request.getresponse()

        obj = json.load(response)

        reply = obj['result']['fulfillment']['speech']
        
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

#calling the class with passing two arguments i.e email and password
client = Bot(Credentials.email, Credentials.password)
client.listen()








