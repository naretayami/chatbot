import spacy

from spacy.matcher import Matcher
nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", None, pattern)

doc = nlp("これから発売されるiPhone Xの発売日がリークされた")
matches = matcher(doc)

for march_id, start, end in matches:
    matched_span = doc[start:end]
print("Matches:", [doc[start:end].text for match_id, start, end in matches])

pattern1 = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world cup"},
    {"IS_PUNCT": True}
]

matcher.add("WORLDCUP_PATTERN", None, pattern1)

doc1 = nlp("2018 FIFA World Cup: フランスが勝った!")
matches = matcher(doc1)
for march_id, start, end in matches:
    matched_span = doc1[start:end]
    print(matched_span.text)

pattern2 = [
    {"POS": "NOUN"},
    {"POS": "ADP"},
    {"LEMMA": "飼う", "POS": "VERB"}
]
matcher.add("PETS_PATTERN", None, pattern2)

doc2 = nlp("犬を飼っていたけど、今はたくさん猫を飼うようになった。")
doc2.is_tagged = True

matches = matcher(doc2)
for march_id, start, end in matches:
    matched_span = doc2[start:end]
    print(matched_span.text)

pattern3 = [
    {"POS": "NOUN"},
    {"POS": "ADP", "OP": "?"},  # Optional: 0個か1個にマッチ
    {"LEMMA": "買う"},
]
matcher.add("BUY_PATTERN", None, pattern3)

doc = nlp.make_doc("スマートフォン買ったので、アプリも買ってる")
doc.is_tagged = True
matches = matcher(doc)
for march_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
