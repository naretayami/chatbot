from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import languages

app = Flask(__name__)

bot = ChatBot(
        name='MyBot',
        tagger_language=languages.JPN
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
        'chatterbot.corpus.japanese' # 日本語版コーパスを設定
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