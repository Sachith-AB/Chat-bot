from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from training_list import all_training_data

bot = ChatBot("chatbot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"]) 

list_trainer = ListTrainer(bot)

list_trainer.train(all_training_data)

while True:
    
    #user request
    user_res = input("tell me something: ")
    
    #get response
    bot_res = bot.get_response(user_res)
    print("chatbot: " + str(bot_res))
