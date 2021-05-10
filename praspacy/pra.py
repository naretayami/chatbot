from spacy.lang.ja import Japanese
nlp = Japanese()

doc = nlp("おはようございます！")

for token in doc:
    print(token.text)
# おはよう
# ござい
# ます
# ！

token = doc[1]
print(token.text)
# ござい

span = doc[1:3]
print(span.text)
# ございます

doc= nlp("果汁100%のジュース。")
print("Index: ", [token.i for token in doc])
print("Text: ", [token.text for token in doc])
print("is_alpha: ", [token.is_alpha for token in doc])
print("is_punct: ", [token.is_punct for token in doc])
print("like_num: ", [token.like_num for token in doc])
# Index: [0, 1, 2, 3, 4, 5]
# Text: ['果汁', '100', '%', 'の', 'ジュース', '。']
# is_alpha:  [True, False, False, True, True, False]
# is_punct:  [False, False, True, False, False, True]
# like_num:  [False, True, False, False, False, False]

doc = nlp(
    "1990年には東アジアの60%以上の人々が極度の貧困状態に陥っていました。"
    "今では4%以下になっています。"
)
for token in doc:
    if token.like_num:
        next_token = doc[token.i + 1]
        if next_token.text == "%":
            print("Percentage found:", token.text)
# Percentage found: 60
# Percentage found: 4