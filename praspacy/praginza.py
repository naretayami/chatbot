import spacy
 
nlp = spacy.load('ja_ginza')
doc = nlp('恵比寿にあるあのイタリアンにはよく行く。美味しいんだ。')
 
for sent in doc.sents:
    for token in sent:
        info = [
            token.i,         # トークン番号
            token.text,     # テキスト
            token.lemma_,    # 基本形
            token.pos_,      # 品詞
            token.tag_,      # 品詞詳細
        ]
        print(info)