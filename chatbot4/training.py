from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
# from my_tagging import MecabTagger

import languages


bot = ChatBot(
        name='MyBot',
        # tagger=MecabTagger,
        database_uri='sqlite:///mydb.sqlite3',
        tagger_language=languages.GINZA,
        # tagger_language=languages.JPN,

)

conversation = [
    '勉強したくない',
    'もう少し頑張れ！',
    '疲れた',
    '5分休憩したらどう？',
    'お腹すいた',
    'チョコがお勧めだよ',
    'なんにもしたくない',
    '一度寝よう！',
]

conversation2 = [
        '数学が分からない',
        '何が分からないの？',
        '連立方程式',
        'おすすめサイト　https://math.005net.com/yoten/renrituKagen.php' ,
        '三角比',
        '難しいよね　https://www.youtube.com/watch?v=OLqgs4fJl7Y' ,
        '二次関数',
        '先生にも聞いてみよう　https://www.studyplus.jp/351' ,
]

trainer = ListTrainer(bot)
trainer.train(conversation)
trainer.train(conversation2)

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
        'chatterbot.corpus.japanese' 
)