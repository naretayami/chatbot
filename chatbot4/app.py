from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot(
        name='MyBot',
        database_uri='sqlite:///mydb.sqlite3'
)

conversation = [
    "Hello", 
    "Hi there!",
    "How are you?",
    "I am good.", 
    "That is good to hear.",
    "Thank you", 
    "You are welcome.", 
]

trainer = ListTrainer(bot)

trainer.train(conversation)

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()