import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "松島、天橋立、宮島は日本三景として知られています。"
    "松島は宮城県、天橋立は京都府、宮島は広島県にそれぞれあります。"
)

doc.is_tagged = True

for token in doc:
    print(token.text, token.pos_)

pattern = [{"POS": "PROPN"}, {"LEMMA": "は"}]

matcher.add("PREFECTURE_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)