import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "私には年の離れた小さい弟がいます。彼は、甘い伊達巻と、辛い塩ラーメンが好きです"
)
doc.is_tagged = True

pattern = [{"POS": "ADJ"}, {"POS": "NOUN"}, {"POS": "NOUN", "OP": "?"}]

matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)