from flask import Flask, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from training_list import all_training_data

app = Flask(__name__)
CORS(app) 

bot = ChatBot(
    "chatbot", 
    read_only=False, 
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "sorry i don't have an answer",
            "maximum_similarity_threshold": 0.9
        }
    ]
) 

list_trainer = ListTrainer(bot)

list_trainer.train(all_training_data)

# while True:
    
#     #user request
#     user_res = input("tell me something: ")
    
#     #get response
#     bot_res = bot.get_response(user_res)
#     print("chatbot: " + str(bot_res))


#connect to frontend
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    
    bot_response = str(bot.get_response(user_input))
    return jsonify ({'response': bot_response})

if __name__ == '__main__':
    app.run(port=8080, debug=True)