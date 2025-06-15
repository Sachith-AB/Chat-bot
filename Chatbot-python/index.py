from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"]) 


list_to_train = [
    "hi", 
    "hi there",
    "what is your name",
    "I'm a chatbot",
    "how old are you?",
    "I'm ageless",
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

while True:
    
    #user request
    user_res = input("tell me something: ")
    
    #get response
    bot_res = bot.get_response(user_res)
    print("chatbot: " + str(bot_res))
