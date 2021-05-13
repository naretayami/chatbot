from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from my_tagging import MecabTagger

bot = ChatBot(
    name = 'MyBot',
    tagger=MecabTagger,
)

trainer = ListTrainer(bot)
trainer.train([
    "Hello!",
    "Hello World!",
    "How are you?",
    "I am very fine!",
    "That's good",
    "Do you like AI?",
])


while True:
    try:
        input_data = input('YOU: ')
        response = bot.get_response(input_data) 
        print('{}: {}'.format(bot.name, response))
        print('-------------------\n')
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


