from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(name='MyBot')

trainer = ListTrainer(chatbot)

# 未登録ユーザーに受け答えする文章を学習
trainer.train([
    "Hello",
    "Hello World",
    "Who are you?",
    "I am AI"
])

# 登録ユーザーに受け答えする文章をリストに格納
statements = [
    Statement(text="Hi user_a", tags=['user_a'], in_response_to='Hello'),
    Statement(text="Hi user_b", tags=['user_b'], in_response_to='Hello'),
    Statement(text="It ’s the assistant ’s AI.", tags=['user_a', 'user_b'], in_response_to="Who are you?")
]

# Statementインスタンスの入ったリストを渡して学習開始
chatbot.storage.create_many(statements)