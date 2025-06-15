from chatterbot import ChatBot

bot = ChatBot(
    "Math", 
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation"
    ]
)

while True:
    user_text = input("User: ")
    print("Chatbot: " + bot.get_response(user_text))