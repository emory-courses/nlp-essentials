---
title: Homework
description: 'HW4: Distributional Semantics'
---

# Homework

Create a [**distributional\_semantics.py**](https://github.com/emory-courses/nlp-essentials/blob/main/src/homework/distributional_semantics.py) file in the [src/homework/](https://github.com/emory-courses/nlp-essentials/tree/main/src/homework) directory.

## Task 1

Your task is to read word embeddings trained by [Word2Vec](neural-language-models.md):

1. Define a function called `read_word_embeddings()` that takes a path to the file consisting of word embeddings, [word\_embeddings.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/word_embeddings.txt).
2. Return a dictionary where the key is a word and the value is its corresponding embedding in [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html).

Each line in the file adheres to the following format:

```
[WORD](\t[FLOAT]){50}
```

## Task 2

Your task is to retrieve a list of the most similar words to a given target word:

1. Define a function called `similar_words()` that takes the word embeddings from Task 1, a target word (string), and a threshold (float).
2. Return a list of tuples, where each tuple contains a word similar to the target word and the cosine similarity between them as determined by the embeddings. The returned list must only include words with similarity scores greater than or equal to the threshold, sorted in descending order based on the similarity scores.

## Task 3

Your task is to measure a similarity score between two documents:

1. Define a function called `document_similarity()` that takes the word embeddings and two documents (string). Assume that the documents are already tokenized.
2. For each document, generate a document embedding by averaging the embeddings of all words within the document.
3. Return the cosine similarity between the two document embeddings.

## Submission <a href="#submission" id="submission"></a>

Commit and push the **distributional\_semantics.py** file to your GitHub repository.

## Rubric

* Task 1: Read Word Embeddings (2.8 points)
* Task 2: Similar Words (3 points)
* Task 3: Document Similarity (3 points)
* Concept Quiz (3.2 points)
