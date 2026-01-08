---
title: Homework
description: 'HW3: Vector Space Models'
---

# Homework

Your task is to develop a sentiment analyzer train on the [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/treebank.html):

* Create a [**vector\_space\_models.py**](https://github.com/emory-courses/nlp-essentials/blob/main/src/homework/vector_space_models.py) file in the [src/homework/](https://github.com/emory-courses/nlp-essentials/tree/main/src/homework) directory.
* Define a function named `sentiment_analyzer()` that takes two parameters, a list of training documents and a list of test documents for classification, and returns the predicted sentiment labels along with the respective similarity scores.
* Use the $$k$$-nearest neighbors algorithm for the classification. Find the optimal value of $$k$$ using the development set, and then hardcode this value into your function before submission.

## Data

The [sentiment\_treebank](https://github.com/emory-courses/nlp-essentials/tree/main/dat/sentiment_treebank) directory contains the following two files:

* [sst\_trn.tst](https://github.com/emory-courses/nlp-essentials/blob/main/dat/sentiment_treebank/sst_trn.tsv): a training set consisting of 8,544 labeled documents.
* [sst\_dev.tst](https://github.com/emory-courses/nlp-essentials/blob/main/dat/sentiment_treebank/sst_dev.tsv): a development set consisting of 1,101 labeled documents.

Each line is a document, which is formatted as follows:

```
[Label]\t[Document]
```

Below are the explanations of what each label signifies:

* `0`: Very negative&#x20;
* `1`: Negative
* `2`: Neutral
* `3`: Positive
* `4`: Very positive

## Submission

Commit and push the **vector\_space\_models.py** file to your GitHub repository.

## Extra Credit

Define a function named `sentiment_analyzer_extra()` that gives an improved sentiment analyzer.

## Rubric

* Code Submission (1 point)
* Program Execution (1 point)
* Development Set Accuracy (4 points)
* Evaluation Set Accuracy (4 points)
* Concept Quiz (2 points)
