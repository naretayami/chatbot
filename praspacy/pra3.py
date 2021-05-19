import spacy
nlp = spacy.load("ja_core_news_sm")


text = "静岡県にある三保の松原は世界遺産の一部です。"
doc = nlp(text)
for token in doc:
    print(token.text)
for ent in doc.ents:
    print(ent.text, ent.label_)
mihonomatsubara = doc[3:6]
print("Missing entity:", mihonomatsubara.text)

