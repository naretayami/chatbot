import MeCab

tagger = MeCab.Tagger()
text = "こんばんは。私の名前はnretayamiです。大学生です。よろしくお願いいたします。"
# 解析結果を変数に入れる
tokens = tagger.parse(text)
# 解析結果を表示する
print(tokens)