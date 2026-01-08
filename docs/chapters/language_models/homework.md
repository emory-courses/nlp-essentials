---
title: Homework
description: 'HW2: Language Models'
---

# Homework

## Task 1: Bigram Modeling

Your goal is to build a bigram model using (1) Laplace smoothing with [normalization](smoothing.md#normalization) and (2) [initial word probabilities](maximum-likelihood-estimation.md#initial-word-probability) by adding the artificial token $$w_0$$ at the beginning of every sentence.

### Implementation

1. Create a [**language\_models.py**](https://github.com/emory-courses/nlp-essentials/blob/main/src/homework/language_models.py) file in the [src/homework/](https://github.com/emory-courses/nlp-essentials/tree/main/src/homework) directory.
2. Define a function named `bigram_model()` that takes a file path pointing to the text file, and returns a dictionary of bigram probabilities estimated in the text file.
3. Use the following constants to indicate the unknown and initial probabilities:

```python
UNKNOWN = ''
INIT = '[INIT]'
```

### Notes

1. Test your model using [dat/chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt).
2. Each line should be treated independently for bigram counting such that the `INIT` token should precede the first word of each line.
3. Use [smoothing with normalization](smoothing.md#normalization) such that all probabilities must sum to 1.0 for any given previous word.
4. Unknown word probabilities should be retrieved using the `UNKNOWN` key for both the previous word ($$w_{i-1}$$) and the current word ($$w_i$$).

## Task 2: Sequence Generation

Your goal is to write a function that takes a word and generates a sequence that includes the input as the initial word.

### Implementation

Under [**language\_models.py**](https://github.com/emory-courses/nlp-essentials/blob/main/src/homework/language_models.py), define a function named `sequence_generator()` that takes the following parameters:

* A bigram model (the resulting dictionary of Task 1)
* The initial word (the first word to appear in the sequence)
* The length of the sequence (the number of tokens in the sequence)

This function aims to generate a sequence of tokens that adheres to the following criteria:

* It must have the precise number of tokens as specified.
* Not more than 20% of the tokens can be punctuation. For instance, if the sequence length is 20, a maximum of 4 punctuation tokens are permitted within the sequence. Use floor of 20% (e.g., if the sequence length is 21, a maximum of $$\mathrm{floor}(21 / 5) = 4$$ puncuation tokens are permitted).
* Excluding punctuation, there should be no redundant tokens in the sequence.

The goal of this task is not to discover a sequence that maximizes the overall [sequence probability](maximum-likelihood-estimation.md#sequence-probability), but rather to optimize individual bigram probabilities. Hence, it entails a greedy search approach rather than an exhaustive one. Given the input word $$w$$, a potential strategy is as follows:

1. Identify the next word $$w'$$ where the bigram probability $$P(w′∣w)$$ is maximized.
2. If $$w′$$ fulfills all the stipulated conditions, include it in the sequence and proceed. Otherwise, search for the next word whose bigram probability is the second highest. Repeat this process until you encounter a word that meets all the specified conditions.
3. Make $$w = w'$$ and repeat the #1 until you reach the specific sequence length.

Finally, the function returns a tuple comprising the following two elements:

* The list of tokens in the sequence
* The log-likelihood estimating the sequence probability using the bigram model. Use the logarithmic function to the base $$e$$, provided as the `math.log()` function in Python.

### Extra Credit

Create a function called `sequence_generator_plus()` that takes the same input parameters as the existing `sequence_generator()` function. This new function should generate sequences with higher probability scores and better semantic coherence compared to the original implementation.

## Submission

Commit and push the **language\_models.py** file to your GitHub repository.

## Rubric

* Task 1: Bigram Modeling (5 points)
* Task 2: Sequence Generator (4.6 points), Extra Credit (2 points)
* Concept Quiz (2.4 points)
