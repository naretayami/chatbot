import spacy

nlp = spacy.load("ja_core_news_sm")

doc = nlp("彼女はおにぎりを食べた")

doc1 = nlp('おにぎり')
for token in doc1:
    n1 = token.pos_
print(n1)

for token in doc:
    print(token.text, token.pos_)

# 彼女 PRON
# は ADP
# おにぎり NOUN
# を ADP
# 食べ VERB
# た AUX

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
# 彼女 PRON nsubj 食べ
# は ADP case 彼女
# おにぎり NOUN obj 食べ
# を ADP case おにぎり
# 食べ VERB ROOT 食べ
# た AUX aux 食べ


doc = nlp('アップルはイギリスのスタートアップを10億円で買いそうだ')
for ent in doc.ents:
    print(ent.text, ent.label_)
# アップル ORG
# イギリス GPE
# 10億円 MONEY

nlp = spacy.load("ja_core_news_sm")

text = "Appleと日本と米国。ニトリと1億円。"
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)


