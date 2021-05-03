from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import languages

bot = ChatBot(
        name='MyBot',
        tagger_language=languages.JPN  
)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
        'chatterbot.corpus.japanese' 
)