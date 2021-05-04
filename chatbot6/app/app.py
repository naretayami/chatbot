from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot(
        name='MyBot',     
)

@app.route("/")
def home():    
    return render_template("home.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 

if __name__ == "__main__":
    app.run()

# while True:
#     try:
#         input_data = input('YOU: ')
#         response = bot.get_response(input_data)
#         print('{}: {}'.format(bot.name, response))
#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break