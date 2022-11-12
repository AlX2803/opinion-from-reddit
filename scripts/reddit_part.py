CLIENT_ID = 'BgQJWhvMQobTg4gtA4Oe2A'

SECRET_KEY = 'GQbv8YwNUraOj9jfNIBVkKvw-APSCg'

import praw
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import re
import numpy as np
import pandas as pd
import spacy
from prawcore import NotFound

pw = 'ProjectPas321.'
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY, password=pw,
                     user_agent='MyAPI/0.0.1', username='Name214w31')

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

nlp = spacy.load("en_core_web_trf")

def is_person(text):
    doc = nlp(text)
    
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            return True
    return False

def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def sentiment_score(text):
    tokens = tokenizer.encode(text, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1

def get_opinion(name, subr_name):
    if not is_person(name):
        return -1, -1

    if subr_name == "all":
        return -2, -2
    subreddit = reddit.subreddit(subr_name)
    hot_section = subreddit.hot(limit=1000)
    
    data = []
    max_opinions = 100
    ok = 1
    try:
        for submission in hot_section:
            if not submission.stickied:
                if submission.title.find(name) != -1:
                    data.append(submission.title)

                if submission.selftext:
                    if submission.selftext.find(name) != -1:
                        data.append(submission.selftext)

                submission.comments.replace_more()
                comments = submission.comments.list()

                for comment in comments:
                    text = comment.body
                    for one_name in name.split():
                        if text.find(one_name) != -1:
                            data.append(text)
                            break
                    if len(data) > max_opinions:
                        ok = 0
                        break
            if ok == 0:
                break
    except Exception as e:
        return -2, -2
    if len(data) == 0 or len(data) < 10:
        return -3, -3

    df = pd.DataFrame(np.array(data), columns=['opinions'])

    df['sentiment'] = df['opinions'].apply(lambda x: sentiment_score(x[:512]))

    average_sentiment = 0
    for sentiment in df['sentiment']:
        average_sentiment += sentiment

    average_sentiment = average_sentiment/df['sentiment'].size
    average_sentiment = round(average_sentiment)

    exemples = df['opinions'][0:10]

    return average_sentiment, exemples

