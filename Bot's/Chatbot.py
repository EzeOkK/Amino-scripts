import json
import os

# Check #####
try:
    import BotAmino
except ImportError:
    print("You don't have this module, lol I'll download it for you......")
    os.system("pip install BotAmino")
    print("ok!")

try:
    import googletrans
except ImportError:
    print("BROOOOOH how do you want to use scripts without the module, I will download it for you again or for the first time...")
    os.system("pip install googletrans")
    print("ok!")
#### check##$$


import requests
from BotAmino import BotAmino
from googletrans import Translator


print("Bruh, just wait.")
client = BotAmino("here", "here") #your information. (email, password) do not remove quotation marks or parentheses.
client.prefix = "/"   
client.wait = 5 #put any number here LoL




translator = Translator()

@client.command("Chatbot")
def c(data):
    # chance tô english or not
    translated_message = translator.translate(data.message, src='pt', dest='en').text

    # Envie a mensagem traduzida para o serviço de chatbot
    link = f"http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg={translated_message}"
    response = requests.get(link)
    json_data = json.loads(response.text)
    chatbot_response = json_data["cnt"]

    # put it on your idiome lol
    translated_response = translator.translate(chatbot_response, src='en', dest='pt').text

    # 🗑️
    data.subClient.send_message(chatId=data.chatId, message=translated_response, replyTo=data.messageId)
    print(f"ChatBot: {translated_response}\nUsuario: {data.author}\n")


client.launch()
print("Pronto.")
