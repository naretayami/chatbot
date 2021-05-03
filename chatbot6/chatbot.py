from chatterbot import ChatBot

bot = ChatBot(
        name='MyBot',     
)

while True:
    try:
        input_data = input('YOU: ')
        response = bot.get_response(input_data)
        print('{}: {}'.format(bot.name, response))
    except(KeyboardInterrupt, EOFError, SystemExit):
        break