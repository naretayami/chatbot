from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import languages


bot = ChatBot(
        name='MyBot',
        tagger_language=languages.JPN  # 日本語設定
)

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