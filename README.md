# How Consumer Reviews Affect the Star Ratings

This project mainly used data from the Yelp Challenge Dataset https://www.yelp.com/dataset/challenge.

I used business.json and review.json for model building and analysis.

# Description

Online reviews are considered as the “new frontier in word-of-mouth marketing”. Yelp, as the biggest review-service provider, becomes a very important information platform for foodservice industry to advertising themselves and for customers to find a better restaurant. Within this review system, star ratings and reviews provided by customers probably are the most essential two features: one summarizes the assessment of the whole experience and the other one indicates specific pros and cons. Those stars and reviews influence the food service providers’ business a lot.


Besides overall star rating, it is useful to understand what features contributing to the rating, and also what are the customers’ preferences on each feature. Based on this analysis, a business can have a better understanding of its strengths and weaknesses compared to its competitors. However, circumstances like unfair evaluations may occur, because different people have different preferences and choices. Thus, we would like to unearth deeper features of relationships between the star ratings and customer reviews.


The objective of our project is try to find aspect categories that affect the Yelp’s business stars
rating the most, so that we could give suggestions to any new upcoming business owners to achieve a more success. To fulfill this objective, we will analyze the sentiment of reviews. The 2 review texts are JSON files downloaded from Yelp website. The coding language we used is Python. And the process to analyze reviews is basically as follow:


Firstly, I manually labeled about four hundred reviews in order to get the most frequent topics. The 4 most frequent topics we found from manually labeling are: food quality, price, service and ambience. Since I only focus on customer reviews of food service industry on the online platform, I mapped two related files of the whole yelp dataset and extract the data base on the topics I pre-defined. I assume these four topics as our aspect categories. Later, in order to know what topics are those reviews really talking about, I processed the data with LDA clustering algorithm to get four big categories of data, which verified our assumption about the most popular topics people are conventionally talking about in the foodservice industry.


Next, I applied the basic procedures of Natural Language Processing (NLP) to the text of consumer reviews. I extracted aspect terms by tokenize each sentence, remove punctuations and stop words, lemmatize each token and hence I can detect the sentiment of each term. And then, I labeled aspect categories for each sentence and detect sentiment expressed towards any given sentence.


Later in this project, I used CNN with word embedding to extract intrinsic features and their corresponding sentiment.


Finally, I got the sentiment for each aspects of every text review, and investigate therelationship between stars rating and consumer reviews.


# Dataset

* `business.json`: Contains business data including location data, attributes, and categories.
* `review.json`: Contains full review text data including the user_id that wrote the review and the business_id the review is written for.
* `stars only.csv`: Matched dataset of `business.json` and `review.json`. Include star ratings of reviews and business id (the same as `reviews.csv` and `categories.csv`). Can be used together with `reviews.csv` and `categories.csv`.
* `reviews.csv`: Matched dataset of `business.json` and `review.json`. Include reviews and business id (the same as `star only.csv` and `categories.csv`). Can be used together with `categories.csv` and `star only.csv`.
* `categories.csv`: Matched dataset of `business.json` and `review.json`. Include categories of reviews and business id (the same as `reviews.csv` and `star only.csv`). Can be used together with `reviews.csv` and `star only.csv`.
* `output1.csv`: Predicted aspecte results using reviews in `stars only.csv`.
* `output2.csv`: Predicted sentiment results using reviews in `stars only.csv`.
* `wordvector_train.csv`: Word vector training dataset. Parsed reviews from `reviews.csv`.
* `labelled1.csv`: Manually labelled reviews on aspects (ambience, price, service, food quality).
* `labelled3.csv`: Manually labelled reviews on sentiments (positive, negative).

# Scripts


# Packages
* sklearn
* numpy
* genism
* keras
* matplotlib
* nltk
