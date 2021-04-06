import spacy

# For loading the english module from spacy cloud,
# python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')

# A token is an instance of a sequence of characters in some particular document that
# are grouped together as a useful semantic unit for processing. 
# A type is the class of all tokens containing the same character sequence.

doc = nlp("Tea is healthy and calming, don't you think?")
for token in doc:
    print(token)


# Lemma : 
# Lemmatization usually refers to doing things properly with the use of a vocabulary and 
# morphological analysis of words, normally aiming to remove inflectional endings only and 
# to return the base or dictionary form of a word, which is known as the lemma .
print(f"Token \t\tLemma \t\tStopword".format('Token', 'Lemma', 'Stopword'))
print("-"*40)
for token in doc:
    print(f"{str(token)}\t\t{token.lemma_}\t\t{token.is_stop}")
