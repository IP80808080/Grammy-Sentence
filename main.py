import spacy

nlp = spacy.load("en_core_web_sm")

sentence = input("Enter a sentence: ")

doc = nlp(sentence)
print(doc.text)
