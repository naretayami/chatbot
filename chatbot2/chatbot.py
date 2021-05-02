from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

logging.basicConfig(level=logging.INFO)

bot = ChatBot(
        name='MyBot',
        read_only=True, # デフォルトではFalse
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///mydb.sqlite3', # キャリア名:///データベース名
        logic_adapters = [
            {
                'import_path': 'chatterbot.logic.BestMatch', # ロジックアダプターを指定
                'default_response': ['How do you feel about it?', 'I still lack knowledge'], # ランダムに応答を返す, # 入力声明が信頼度が８０％以下だった場合に返される応答
                'maximum_similarity_threshold': 0.80 # ８０％以下の信頼度だった場合にdefault_responseを応答させる
            }
        ]

)


conversation = [
    "Hello", # こんにちは
    "Hi there!", # こんにちは！
    "How are you?", # お元気ですか？
    "I am good.", # 私は元気です。
    "That is good to hear.", # それは良かった。
    "Thank you", # ありがとうございました
    "You are welcome.", # どう致しまして。
]

conversation_2 = [
        'Unigram pairs are used for text search.', # ユニグラムペアはテキスト検索に使用されます。
        'You are wrong', # あなたは間違っている
        'What is the correct answer?', # 正解は何ですか？
        'ChatterBot uses bigram pairs.' # ChatterBotはバイグラムペアを使用します。
]

conversation_3 = [
        'Trigram pairs are used for text search.', # トライグラムペアはテキスト検索に使用されます。
        'You are wrong', # あなたは間違っている
        'What is the correct answer?', # 正解は何ですか？
        'ChatterBot uses bigram pairs.' # ChatterBotはバイグラムペアを使用します。
]

conversation_4 = [
        'Bigram pairs are used for text search.', # バイグラムペアはテキスト検索に使用されます。
        'You are correct' # あなたは正しいです
]


trainer = ListTrainer(bot)

trainer.train(conversation)
trainer.train(conversation_2)
trainer.train(conversation_3)
trainer.train(conversation_4)

# ループ処理で声明を受け取る
# 終了する場合は「ctrl」＋「c」を入力
while True:
    try:
        input_data = input('YOU: ')
        response = bot.get_response(input_data)
        print('{}: {}'.format(bot.name, response))
    except(KeyboardInterrupt, EOFError, SystemExit):
        break