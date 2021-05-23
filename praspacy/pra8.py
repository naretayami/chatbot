import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

p1 = input()
# Process a text
doc = nlp(p1)

# Iterate over the tokensp
for token in doc:
    # Print the text and the predicted part-of-speech tag
    n1 = token.pos_
print(n1)