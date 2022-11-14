# Summary of the project
 
 I developed an application that finds the average opinion in a subreddit about a person with Reddit’s API in Python. I used:
 - Python Reddit API Wrapper(PRAW) to get comments from Reddit’s API
 - Bidirectional Encoder Representations from Transformers (BERT), a transformer-based machine learning technique for natural language processing pre-training, to perform sentiment analysis on the comments
 - spaCy, an open-source software library for advanced natural language processing, to verify if the first input that the user gives is the name of a person
 - Django for interface
 
 The application asks for a person’s name and a subreddit, as input, and gives the average sentiment, in the form: “Very negative”, “Negative”, “Neutral”, “Positive”, “Very positive’’, from the first 100 comments, that contain the person’s name, from the first 1000 posts in the hot section of the given subreddit.

![negative_opinion](https://user-images.githubusercontent.com/75032781/201484851-1fbbff9b-ad8c-4bbe-9930-d6ebaece570a.png)

![neutral_opinion](https://user-images.githubusercontent.com/75032781/201484856-5fb40a5d-22e0-4de1-bd21-5100c8bed72a.png)

![positive_opinion](https://user-images.githubusercontent.com/75032781/201485108-2a1e6410-85bb-47bf-89e2-6dbe2f222bc9.png)
