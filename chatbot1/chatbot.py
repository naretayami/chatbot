from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import languages


bot = ChatBot(
        name='MyBot',
        tagger_language=languages.JPN,  # 日本語設定
        # storage_adapter='chatterbot.storage.SQLStorageAdapter',
        # logic_adapters=[
        #     'chatterbot.logic.MathematicalEvaluation'
        # ],
        database_uri='mysql://root:renarena@localhost:3306/chatbot?charset=utf8mb4',

)

# conversarion = [
#     '勉強したくない',
#     'もう少し頑張れ！',
#     '疲れた',
#     '5分休憩したらどう？',
#     'お腹すいた',
#     'チョコがお勧めだよ',
# ]

# trainer = ListTrainer(bot)
# trainer.train(conversarion)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
        'chatterbot.corpus.japanese' # 日本語版コーパスを設定
)

while True:
    try:
        input_data = input('YOU: ')
        response = bot.get_response(input_data)
        print('{}: {}'.format(bot.name, response))
    except(KeyboardInterrupt, EOFError, SystemExit):
        break