from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot import languages

bot2 = ChatBot(
        name='Bot2',
        tagger_language=languages.ENG,
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
        'chatterbot.corpus.english' 
)
