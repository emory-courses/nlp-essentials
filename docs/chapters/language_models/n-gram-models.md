---
title: N-gram Models
---

# N-gram Models

An _**n**_**-gram** is a contiguous sequence of _n_ items from text data. These items can be:

* Words (most common in language modeling)
* Characters (useful for morphological analysis)
* Subword tokens (common in modern NLP)
* Bytes or other units

For the sentence "_I'm a computer scientist._", we can extract different n-grams:

* **1-gram (unigram)**: \{"I'm", "a", "computer", "scientist."\}
* **2-gram (bigram)**: \{"I'm a", "a computer", "computer scientist."\}
* **3-gram (trigram)**: \{"I'm a computer", "a computer scientist."\}

In the above example, "_I'm_" and "_scientist._" are recognized as individual tokens, which should have been [tokenized](../text_processing/tokenization.md) as `["I", "'m"]` and `["scientist", "."]`.

:::warning
**Q1**: What are the **advantages** of splitting "_I_" and "'_m_" as two separate tokens, versus recognizing "_I'm_" as one token?
:::

## Unigram Estimation

Given a large corpus, a **unigram model** assumes word independence and calculates the probability of each word $$w_i$$ as:

$$
P(w_i) = \frac{\#(w_i)}{\sum_{\forall w_k \in V}\#(w_k)}
$$

Where:

* $$\#(w_i)$$: the count of word  in the corpus.
* $$V$$: the vocabulary (set of all unique words).
* The denominator represents the total word count.

Let us define the `Unigram` type:

```python showLineNumbers
from typing import TypeAlias

Unigram: TypeAlias = dict[str, float]
```

* L1: [Type aliases](https://docs.python.org/3/library/typing.html#type-aliases).
* L3: A dictionary where the key is a unigram and the value is its probability.

Let us also define a function `unigram_count()` that takes a file path and returns a Counter with all unigrams and their counts in the file as keys and values, respectively:

```python showLineNumbers
from collections import Counter

def unigram_count(filepath: str) -> Counter:
    unigrams = Counter()

    for line in open(filepath):
        words = line.split()
        unigrams.update(words)

    return unigrams
```

We then define a function `unigram_estimation()` that takes a file path and returns a dictionary with unigrams and their probabilities as keys and values, respectively:

```python showLineNumbers
def unigram_estimation(filepath: str) -> Unigram:
    counts = unigram_count(filepath)
    total = sum(counts.values())
    return {word: count / total for word, count in counts.items()}
```

* L3: Calculate the total count of all unigrams in the text.
* L4: Return a dictionary where each word is a key and its probability is the value.

Finally, let us define a function `test_unigram()` that takes a file path as well as an estimator function, and test `unigram_estimation()` with a text file [dat/chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt):

```python showLineNumbers
from collections.abc import Callable

def test_unigram(filepath: str, estimator: Callable[[str], Unigram]):
    unigrams = estimator(filepath)
    unigram_list = [(word, prob) for word, prob in sorted(unigrams.items(), key=lambda x: x[1], reverse=True)]

    for word, prob in unigram_list[:300]:
        if word[0].isupper() and word.lower() not in unigrams:
            print(f'{word:>10} {prob:.6f}')
```

* L1: Import the [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable) type from the typing module.
* L3: The second argument accepts a function that takes a string and returns a Unigram.
* L4: Call the estimator with the text file and store the result in `unigrams`.
* L5: Create a list of unigram-probability pairs, `unigram_list`, sorted by probability in descending order.
* L7: Iterate through the top 300 unigrams with the highest probabilities.
* L8: Check if the word starts with an uppercase letter and its lowercase version is not in unigrams (aiming to search for proper nouns).

```python showLineNumbers title="Run"
corpus = 'dat/chronicles_of_narnia.txt'
test_unigram(corpus, unigram_estimation)
```

* L2: Pass the  `unigram_estimation()` function as the second argument.

```text title="Output"
         I 0.010543
     Aslan 0.001850
      Lucy 0.001815
    Edmund 0.001409
    Narnia 0.001379
   Caspian 0.001338
      Jill 0.001262
     Peter 0.001034
    Shasta 0.000928
    Digory 0.000925
   Eustace 0.000877
     Susan 0.000654
    Tirian 0.000601
     Polly 0.000547
    Aravis 0.000537
      Bree 0.000492
Puddleglum 0.000492
    Scrubb 0.000482
    Andrew 0.000406
```

This distribution shows the most common unigrams in the text meeting the conditions in L8, dominated by the first-person pronoun "_I_", followed by proper nouns - specifically character names such as "_Aslan_", "_Lucy_", and "_Edmund_".

:::warning
**Q2**: What advantages do **unigram probabilities** have over [**word frequencies**](../text_processing/frequency-analysis.md#word-frequency)?
:::

## Bigram Estimation

A **bigram model** calculates the conditional probability of the current word $$w_{i}$$ given the previous word $$w_{I-1}$$ as follows ($$\#(w_{i-1},w_{i})$$: the total occurrences of $$(w_{i-1},w_{i})$$ in the corpus in that order, $$V_i$$: a set of all word types occurring after $$w_{i-1}$$):

$$
P(w_i|w_{i-1}) = \frac{\#(w_{i-1},w_{i})}{\sum_{\forall w_k \in V_{i}} \#(w_{i-1},w_k)}
$$

Where:

* $$\#(w_{i-1},w_{i})$$: the total occurrences of $$(w_{i-1},w_{i})$$ in the corpus in that order.
* $$V_i$$: a set of all word types occurring after $$w_{i-1}$$.

Let us define the `Bigram` type:

```python showLineNumbers
Bigram: TypeAlias = dict[str, Unigram | float]
```

* A dictionary where the key is $$w_{i-1}$$ and the value is a nested dictionary representing the unigram distribution of all $$w_{i}$$ given $$w_{i-1}$$, or a [smoothing probability](smoothing.md) for $$w_{i-1}$$.

Let us also define a function `bigram_count()` that takes a file path and returns a dictionary with all bigrams and their counts in the file as keys and values, respectively:

```python showLineNumbers
from collections import Counter, defaultdict
from src.types import Bigram

def bigram_count(filepath: str) -> dict[str, Counter]:
    bigrams = defaultdict(Counter)

    for line in open(filepath):
        words = line.split()
        for i in range(1, len(words)):
            bigrams[words[i - 1]].update([words[i]])

    return bigrams
```

* L1: Import the [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict) class from the [collections](https://docs.python.org/3/library/collections.html) package.
* L2: import the Bigram [type alias](https://docs.python.org/3/library/typing.html#type-aliases) from the [src.types](https://github.com/emory-courses/nlp-essentials/blob/main/src/types.py) package.
* L5: Create a defaultdict with Counters as default values to store bigram frequencies.
* L9: Iterate through the words, starting from the second word (index 1) in each line.
* L10: Update the frequency of the current bigram.

We then define a function `bigram_estimation()` that takes a file path and returns a dictionary with bigrams and their probabilities as keys and values, respectively:

```python showLineNumbers
from src.types import Bigram

def bigram_estimation(filepath: str) -> Bigram:
    counts = bigram_count(filepath)
    bigrams = dict()

    for prev, ccs in counts.items():
        total = sum(ccs.values())
        bigrams[prev] = {curr: count / total for curr, count in ccs.items()}

    return bigrams
```

* L8: Calculate the total count of all bigrams with the same previous word.
* L9: Calculate and store the probabilities of each current word given the previous word.

Finally, let us define a function `test_bigram()` that takes a file path and an estimator function, and test `bigram_estimation()` with the text file:

```python showLineNumbers
def test_bigram(filepath: str, estimator: Callable[[str], Bigram]):
    bigrams = estimator(filepath)
    for prev in ['I', 'the', 'said']:
        print(prev)
        bigram_list = [(curr, prob) for curr, prob in sorted(bigrams[prev].items(), key=lambda x: x[1], reverse=True)]
        for curr, prob in bigram_list[:10]:
            print("{:>10} {:.6f}".format(curr, prob))
```

* L2: Call the `bigram_estimation()` function with the text file and store the result.
* L5: Create a bigram list given the previous word, sorted by probability in descending order.
* L6: Iterate through the top 10 bigrams with the highest probabilities for the previous word.

```python showLineNumbers title="Run"
test_bigram(corpus, bigram_estimation)
```

```text title="Output"
I
        'm 0.081628
        do 0.075849
       've 0.044065
       was 0.041897
      have 0.038045
        am 0.035878
       'll 0.032507
     think 0.032025
        'd 0.026246
      know 0.025765
the
      same 0.014846
     other 0.013405
      King 0.012528
     Witch 0.011776
     whole 0.009020
    others 0.008958
     first 0.008770
     Dwarf 0.008582
      door 0.008519
     great 0.008519
said
       the 0.157635
         , 0.073645
      Lucy 0.057635
    Edmund 0.045074
   Caspian 0.040394
     Peter 0.039409
      Jill 0.034975
         . 0.034729
    Digory 0.031034
     Aslan 0.030049
```

:::warning
**Q3**: What NLP tasks can benefit from **bigram estimation** over **unigram estimation**?
:::

## References

1. Source: [ngram\_models.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/ngram_models.py).
2. [N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf), Speech and Language Processing (3rd ed. draft), Jurafsky and Martin.
