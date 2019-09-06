from nltk.corpus import stopwords
import pandas as pd#
import nltk

# import the table containing scraped data
text = pd.read_csv("scraped_data.csv")
# create an empty dictionary to store tokenised text in
tokenised_text = {}
# Initialise a stopwords variable using english words
sr = stopwords.words("english")
# create an empty dictionary to store clean tokens in
clean_tokenised_text = {}

# iterate through the table and tokenise the text in each row
for row in text.iterrows():
    corpus = row[1]["Page_Description"]
    corpus = corpus.lower()
    link_path = row[1]["Unnamed: 0"]
    tokenised_text[link_path] = [t for t in corpus.split()]

    clean_tokens = tokenised_text[link_path][:]
    for token in tokenised_text[link_path]:
        if token in sr:
            clean_tokens.remove(token)
        else:
            pass
    clean_tokenised_text[link_path] = clean_tokens
    print(len(tokenised_text[link_path]), len(clean_tokens))
    freq = nltk.FreqDist(clean_tokens)
    freq.plot(10, cumulative = False)
