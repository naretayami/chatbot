from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import languages

bot = ChatBot(
        name='MyBot',
        read_only=True,
        tagger_language=languages.JPN ,
        database_uri='mysql://root:renarena@localhost:3306/chatbot?charset=utf8mb4'
)

conversarion = [
    '勉強したくない',
    'もう少し頑張れ！',
    '疲れた',
    '5分休憩したらどう？',
    'お腹すいた',
    'チョコがお勧めだよ',
    'なんにもしたくない',
    '一度寝よう！',
]

trainer = ListTrainer(bot)
trainer.train(conversarion)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
        'chatterbot.corpus.japanese' 
)