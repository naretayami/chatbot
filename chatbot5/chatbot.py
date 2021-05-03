from chatterbot import ChatBot

chatbot = ChatBot(
        name='MyBot',
        default_response=["I do not understand"], # 応答が見つからなかった場合に返す文章
        read_only=False, # デフォルト値
)

# ユーザー名を入力
user_name = input('What is your name?: ')
print('Welcome to ChatBot!')
print('+-----------------+')

if user_name in ['user_a', 'user_b']:
    # 登録ユーザーの処理
    while True:
        try:
            input_data = input(user_name + ': ')
            response = chatbot.get_response(
                    input_data,
                    tags=[user_name],
                    # 検索時のフィルターとしてユーザ名の入ったタグを設定します。
                    additional_response_selection_parameters={
                        'tags': [user_name]
                    }
            )
            print('{}: {}'.format(chatbot.name, response))
            print('-------------------\n')
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
else:
    # 未登録ユーザーの処理
    while True:
        try:
            input_data = input('Not User: ')
            response = chatbot.get_response(input_data)
            print('{}: {}'.format(chatbot.name, response))
            print('-------------------\n')
        except(KeyboardInterrupt, EOFError, SystemExit):
            break