import os

file_name = os.path.dirname(os.path.abspath(__file__)) + '/lexicon.csv'
fo = open(file_name, 'r', encoding='utf-8')
lines = fo.readlines()
fo.close()

sentiment_dict = {}
for line in lines:
    senti_word, senti_score = line.strip().split(',')
    sentiment_dict[senti_word] = senti_score


def sentiment(word):
    try:
        if word in sentiment_dict.keys():
            score = int(sentiment_dict[word])
            return score
        else:
            return None
    except:
        return None


def sentiments(sentence):
    try:
        scores = {}
        for word in sentence.strip().split():
            scores[word] = sentiment(word)
        return scores
    except:
        return {}
