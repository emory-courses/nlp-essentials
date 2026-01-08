---
title: Bag-of-Words Model
---

# Bag-of-Words Model

## Overview

In the **bag-of-words model**, a document is represented as a set or a "bag" of words, disregarding any structure but maintaining information about the frequency of every word.

Consider a corpus containing the following two [tokenized](../text_processing/tokenization.md) documents:

```python
D1 = ['John', 'bought', 'a', 'book', '.', 'The', 'book', 'was', 'funny', '.']
D2 = ['Mary', 'liked', 'the', 'book', '.', 'John', 'gave', 'it', 'to', 'Mary', '.']
```

The corpus contains a total of 14 words, and the entire vocabulary can be represented as a list of all word types in this corpus:

```python
W = [
    '.',        # 0
    'John',     # 1
    'Mary',     # 2
    'The',      # 3
    'a',        # 4
    'book',     # 5
    'bought',   # 6
    'funny',    # 7
    'gave',     # 8
    'it',       # 9
    'liked',    # 10
    'the',      # 11
    'to',       # 12
    'was'       # 13
]
```

Let $$D_i = [w_{i,1}, \ldots, w_{i,n}]$$ be a document, where $$w_{i,j}$$ is the $$j$$'th word in $$D_i$$. A vector representation for $$D_i$$ can be defined as $$v_i = [\mathrm{count}(w_j \in D_i) : \forall w_j \in W] \in \mathbb{R}^{|W|}$$, where $$w_j$$ is the $$j$$'th word in $$W$$ and each dimension in $$v_i$$ is the frequency of $$w_j$$'s occurrences in $$D_i$$ such that:

```python
#     0  1  2  3  4  5  6  7  8  9 10 11 12 13
v1 = [2, 1, 0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 1]
v2 = [2, 1, 2, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]
```

Notice that the bag-of-words model often results in a highly sparse vector, with many dimensions in $$v_i$$ being 0 in practice, as most words in the vocabulary $$W$$ do not occur in document $$D_i$$. Therefore, it is more efficient to represent $$v_i$$ as a sparse vector:

```python
v1 = {0:2, 1:1, 3:1, 4:1, 5:2, 6:1, 7:1, 13:1}
v2 = {0:2, 1:1, 2:2, 5:1, 8:1, 9:1, 10:1, 11:1, 12:1}
```

:::warning
**Q1**: One limitation of the bag-of-words model is its inability to handle **unknown words**. Is there a method to enhance the bag-of-words model, allowing it to handle unknown words?
:::

## Implementation

Let us define a function that takes a list of documents, where each document is represented as a list of tokens, and returns a dictionary, where keys are words and values are their corresponding unique IDs:

```python showLineNumbers
from typing import TypeAlias

Document: TypeAlias = list[str]
Vocab: TypeAlias = dict[str, int]

def vocabulary(documents: list[Document]) -> Vocab:
    vocab = set()

    for document in documents:
        vocab.update(document)

    return {word: i for i, word in enumerate(sorted(list(vocab)))}
```

We then define a function that takes the vocabulary dictionary and a document, and returns a bag-of-words in a sparse vector representation:

```python showLineNumbers
from collections import Counter

SparseVector: TypeAlias = dict[int, int | float]

def bag_of_words(vocab: Vocab, document: Document) -> SparseVector:
    counts = Counter(document)
    return {vocab[word]: count for word, count in sorted(counts.items()) if word in vocab}
```

Finally, let us our bag-of-words model with the examples above:

```python showLineNumbers title="Run"
documents = [
    ['John', 'bought', 'a', 'book', '.', 'The', 'book', 'was', 'funny', '.'],
    ['Mary', 'liked', 'the', 'book', '.', 'John', 'gave', 'it', 'to', 'Mary', '.']
]

vocab = vocabulary(documents)
print(vocab)

print(bag_of_words(vocab, documents[0]))
print(bag_of_words(vocab, documents[1]))
```

```python title="Output"
{
    '.': 0,
    'John': 1,
    'Mary': 2,
    'The': 3,
    'a': 4,
    'book': 5,
    'bought': 6,
    'funny': 7,
    'gave': 8,
    'it': 9,
    'liked': 10,
    'the': 11,
    'to': 12,
    'was': 13
}
{0: 2, 1: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 13: 1}
{0: 2, 1: 1, 2: 2, 5: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1}
```

:::warning
**Q2**: Another limitation of the bag-of-words model is its inability to capture **word order**. Is there a method to enhance the bag-of-words model, allowing it to preserve the word order?
:::

## References

1. Source: [bag\_of\_words\_model.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/bag_of_words_model.py)
2. [Bag-of-Words Model](https://en.wikipedia.org/wiki/Bag-of-words_model), Wikipedia
3. [Bags of words](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#bags-of-words), Working With Text Data, scikit-learn Tutorials
