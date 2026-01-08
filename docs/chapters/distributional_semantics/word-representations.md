---
title: Word Representations
---

# Word Representations

## One-hot Encoding

**One-hot encoding** represents words as binary vectors such that each word is represented as a vector where all dimensions are zero except for one, which is set to one, indicating the presence of that word.

Consider the following vocabulary:

```python
V = [
    'king',    # 0
    'man',     # 1
    'woman',   # 2
    'queen'    # 3
]
```

Given a vocabulary size of 4, each word is represented as a 4-dimensional vector as illustrated below:

```python
 king = [1, 0, 0, 0]
  man = [0, 1, 0, 0]
woman = [0, 0, 1, 0]
queen = [0, 0, 0, 1]
```

One-hot encoding has been largely adopted in traditional NLP models due to its simple and efficient representation of words in sparse vectors.

:::warning
**Q2**: What are the drawbacks of using **one-hot encoding** to represent word vectors?
:::

## Word Embeddings

**Word embeddings** are dense vector representations of words in a continuous vector space. Each word is represented in a high-dimensional space, where the dimensions correspond to different contextual features of the word's meaning.

Consider the embeddings for three words, 'king', 'male', and 'female':

```python
 king = [0.5, 0.0, 0.5, 0.0]
  man = [0.0, 0.5, 0.5, 0.0]
woman = [0.0, 0.5, 0.0, 0.5]
```

Based on these distributions, we can infer that the four dimensions in this vector space represent _royalty_, _gender_, _male_, and _female_ respectively, such that the embedding for the word 'queen' can be estimated as follows:

```python
 queen = king - man + woman
       = [0.5, 0.0, 0.0, 0.5]
```

The key idea is to capture semantic relationships between words by representing them in a way that similar words have similar vector representations. These embeddings are learned from large amounts of text data, where the model aims to predict or capture the context in which words appear.

:::info
☝️ In the above examples, each dimension represents a distinct type of meaning. However, in practice, a dimension can encapsulate multiple types of meanings. Furthermore, a single type of meaning can be depicted by a weighted combination of several dimensions, making it challenging to precisely interpret what each dimension implies.
:::
