# NLP Tweets Sentiment Classification
The repository contains:
- a sentiment tweets scraping module (.py) using Twitter Streaming API
- a jupyter notebook of steps solving tweets sentiment classification problem with NLP and Naive Bayes model.

Real-time tweets are streamed through the Twitter Streaming API and stored in local machine. You can find official documentation [here](https://developer.twitter.com/en/docs/labs/filtered-stream/overview).

### Twitter API Setup
1. Using python package for Twitter API (one of many) python-twitter. It can be installed in our environment using `pip install python-twitter`.
2. Before we get our application tokens (API keys) we have to create own Twitter App. Follow [these intructions](https://python-twitter.readthedocs.io/en/latest/getting_started.html).
    - you can name your application `Test Application for API Challenge at LighthouseLabs` or something simalar
    - if you don't know what  website to use, use link to this repository: https://github.com/lighthouse-labs/API_challenge. 
    - Once you have access to your keys and tokens (should be 4 overall), save them as environmental variables in your computer.
    - Test your personal details using python snippet in the instructions above. We will have to edit the code and use package os to access the values of environmental variables


