---
title: Latent Semantic Analysis
---

# Latent Semantic Analysis

**Latent Semantic Analysis** (LSA) \[1] analyzes relationships between a set of documents and the terms they contain. It is based on the idea that words that are used in similar contexts tend to have similar meanings, which is in line with the [distributional hypothesis](distributional-hypothesis.md).

## Document-Term Matrix

LSA starts with a matrix representation of the documents in a corpus and the terms (words) they contain. This matrix, known as the **document-term matrix**, has documents as rows and terms as columns, with each cell representing the frequency of a term in a document.

Let us define a function that reads a corpus, and returns a list $$D$$ of all documents in the corpus and a dictionary $$T$$ whose keys and values are terms and their unique indices, respectively:

```python showLineNumbers
from src.types import Document, Vocab

def retrieve(filename: str) -> tuple[list[Document], Vocab]:
    documents = [line.split() for line in open(filename)]
    t = {word for document in documents for word in document}
    terms = {term: j for j, term in enumerate(sorted(list(t)))}
    return documents, terms
```

We then define a function that takes $$D$$ and $$T$$, and returns the document-term matrix $$X \in \mathbb{R}^{\lvert D \rvert \times \lvert T \rvert}$$ such that $$X_{i,j}$$ indicates the frequency of the $$j$$'th term in $$T$$ within the $$i$$'th document:

```python showLineNumbers
import numpy as np

def document_term_matrix(documents: list[Document], terms: Vocab) -> np.array:
    def doc_vector(document: list[str]) -> list[int]:
        v = [0] * len(terms)
        for term in document:
            v[terms[term]] += 1
        return v
    return np.array([doc_vector(document) for document in documents])
```

* L1: The [numpy](https://numpy.org/doc/stable/) package.
* L3: [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

Let us create a document-term matrix from the corpus, [dat/chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt):

```python showLineNumbers title="Run"
import time

D, T = retrieve('dat/chronicles_of_narnia.txt')

st = time.time()
X = document_term_matrix(D, T)
et = time.time()
print("|D| = {}, |T| = {}, Process Time (sec) = {:.2f}".format(len(X), len(X[0]), et - st))
```

* L1: [Basic date and time types](https://docs.python.org/3/library/datetime.html).
* L3: [time.time()](https://docs.python.org/3/library/time.html#time.time)

```python title="Output"
|D| = 22603, |T| = 12361, Process Time (sec) = 17.87
```

With this current implementation, it takes over 17 seconds to create the document-term matrix, which is unacceptably slow given the small size of the corpus. Let us improve this function by first creating a 2D matrix in NumPy and then updating the frequency values:

```python showLineNumbers
def document_term_matrix_np(documents: list[Document], terms: Vocab) -> np.array:
    X = np.zeros((len(documents), len(vocab)), dtype=int)
    for i, document in enumerate(documents):
        for term in document:
            X[i, vocab[term]] += 1
    return X
```

Using this updated function, we see a noticeable enhancement in speed, about 0.5 seconds, to create the document-term matrix:

```python showLineNumbers title="Run"
st = time.time()
X = document_term_matrix_np(D, T)
et = time.time()
print("|D| = {}, |T| = {}, Process Time (sec) = {:.2f}".format(len(X), len(X[0]), et - st))
```

```python title="Output"
|D| = 22603, |T| = 12361, Process Time (sec) =  0.55
```

The $$i$$'th row of $$X$$ is considered the document vector of the $$i$$'th document in the corpus, while the transpose of $$j$$'th column of $$X$$ is considered the term vector of the $$j$$'th term in the vocabulary.

:::warning
**Q3**: Why is the performance of **document\_term\_matrix()** significantly slower than **document\_term\_matrix\_np()**?
:::

## **Dimensionality Reduction**

LSA applies **Singular Value Decomposition** (SVD) \[2] to decompose the document-term matrix $$X$$ into three matrices, $$U$$, $$\Sigma$$, and $$V$$, where $$U, V \in \mathbb{R}^{\lvert D \rvert \times \sigma}$$ are orthogonal matrices and $$\Sigma \in \mathbb{R}^{\sigma \times \sigma}$$ is a diagonal matrix containing singular values, such that $$X = U\Sigma V^T$$.

* An [orthogonal matrix](https://en.wikipedia.org/wiki/Orthogonal_matrix)  is a square matrix whose rows and columns are orthogonal such that $$O O^T = O^T O = I$$, where $$I$$ is the identity matrix.
* [Singular values](https://en.wikipedia.org/wiki/Singular_value) are non-negative values listed in decreasing order that represent the importance of each topic.

For simplicity, let us create a document-term matrix from a small corpus consisting of only eight documents and apply SVD to it:

<details>

<summary><a href="https://github.com/emory-courses/nlp-essentials/tree/main/dat/latent_semantic_analysis.txt">dat/latent_semantic_analysis.txt</a></summary>

```
love white cat
love black cat
hate white cat
hate black cat
love white dog
love black dog
hate white dog
hate black dog
```

</details>

```python showLineNumbers
D, T = retrieve('dat/latent_semantic_analysis.txt')
X = document_term_matrix_np(D, T)
U, S, Vt = np.linalg.svd(X, full_matrices=False)
S = np.diag(S)
```

* L3: [numpy.linalg.svd()](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)
* L4: [numpy.diag()](https://numpy.org/doc/stable/reference/generated/numpy.diag.html)

This results $$U \in \mathbb{R}^{8 \times 6}$$, $$\Sigma \in \mathbb{R}^{6 \times 6}$$, and $$V^T \in \mathbb{R}^{6 \times 6}$$ such that:

* In $$U$$, each row represents a document and each column represent a topic.
* In $$\Sigma$$, each diagonal cell represents the weight of the corresponding topic.
* In $$V^T$$, each column represents a term and each row represents a topic.

```python showLineNumbers title="Run"
def print_np(matrix: np.array):
    print(matrix.shape)
    for row in matrix:
        print(' '.join(['{:8.4f}'.format(c) for c in row]))

print_np(U)
print_np(S)
print_np(Vt)
```

```text title="U"
(8, 6)
 -0.3536  -0.4969  -0.0552   0.3536  -0.6648  -0.0396
 -0.3536  -0.4969  -0.0552  -0.3536   0.3750   0.5911
 -0.3536  -0.0552   0.4969   0.3536   0.4847  -0.3598
 -0.3536  -0.0552   0.4969  -0.3536  -0.1949  -0.1917
 -0.3536   0.0552  -0.4969   0.3536   0.3187  -0.1450
 -0.3536   0.0552  -0.4969  -0.3536  -0.0289  -0.4065
 -0.3536   0.4969   0.0552   0.3536  -0.1386   0.5444
 -0.3536   0.4969   0.0552  -0.3536  -0.1512   0.0071
```

```text title="S"
(6, 6)
  3.4641   0.0000   0.0000   0.0000   0.0000   0.0000
  0.0000   2.0000   0.0000   0.0000   0.0000   0.0000
  0.0000   0.0000   2.0000   0.0000   0.0000   0.0000
  0.0000   0.0000   0.0000   2.0000   0.0000   0.0000
  0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
  0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
```

```text title="Vt"
(6, 6)
 -0.4082  -0.4082  -0.4082  -0.4082  -0.4082  -0.4082
  0.0000  -0.5522   0.5522   0.4417  -0.4417   0.0000
  0.0000   0.4417  -0.4417   0.5522  -0.5522   0.0000
 -0.7071  -0.0000  -0.0000  -0.0000  -0.0000   0.7071
 -0.2614  -0.3151  -0.3151   0.5765   0.5765  -0.2614
 -0.5148   0.4838   0.4838   0.0310   0.0310  -0.5148
```

:::info
☝️ The last two singular values in $$\Sigma$$ are actually non-negative values, $$3.72393692 \times 10^{−16}$$ and $$2.29674157 \times 10^{−16}$$, respectively.
:::

The first four singular values in $$\Sigma$$ appear to be sufficiently larger than the others; thus, let us reduce their dimensions to $$k = 4$$ such that $$U' \in \mathbb{R}^{8 \times 4}$$, $$\Sigma' \in \mathbb{R}^{4 \times 4}$$, and $$V'^{T} \in \mathbb{R}^{4 \times 6}$$:

```python showLineNumbers
k = 4
U = U[:, :k]
S = S[:k, :k]
Vt = Vt[:k, :]
```

:::warning
**Q4**: What is the maximum number of **topics** that LSA can identify? What are the **limitations** associated with discovering topics using this approach?
:::

## Document Embedding

Given the LSA results, an embedding of the $$i$$'th document can be obtained as $$d_i = U_{i,*} \cdot \Sigma \in \mathbb{R}^{1 \times 4}$$:

```python showLineNumbers title="Run"
for i, document in enumerate(D):
    t = np.dot(U[i], S)
    print('{}: {}'.format(' '.join(document), ['{:5.2f}'.format(f) for f in t]))
```

* [numpy.dot()](https://numpy.org/doc/stable/reference/generated/numpy.dot.html)

```python title="Output"
love white cat: [-1.22, -0.99, -0.11,  0.71]
love black cat: [-1.22, -0.99, -0.11, -0.71]
hate white cat: [-1.22, -0.11,  0.99,  0.71]
hate black cat: [-1.22, -0.11,  0.99, -0.71]
love white dog: [-1.22,  0.11, -0.99,  0.71]
love black dog: [-1.22,  0.11, -0.99, -0.71]
hate white dog: [-1.22,  0.99,  0.11,  0.71]
hate black dog: [-1.22,  0.99,  0.11, -0.71]
```

From the output, although interpreting the meaning of the first topic (column) is challenging, we can infer that the second, third, and fourth topics represent "animal", "sentiment", and "color", respectively. This reveals a limitation of LSA, as higher singular values do not necessarily guarantee the discovery of more meaningful topics.

:::warning
**Q5**: By discarding the first topic, you can observe **document embeddings that are opposite** (e.g., documents 4 and 5). What are the characteristics of these documents that are opposite to each other?
:::

## Word Embedding

Finally, an embedding of the $$j$$'th term can be achieved as $$t_j = \Sigma \cdot V^T_{*,j} = V_{j,*} \cdot \Sigma^T \in \mathbb{R}^{1 \times 4}$$:

```python showLineNumbers title="Run"
V = Vt.transpose()
for term, j in sorted(T.items(), key=lambda x: x[1]):
    t = np.dot(V[j], S)
    print('{:>5}: {}'.format(term, ['{:5.2f}'.format(f) for f in t]))
```

```python title="Output"
black: [-1.41,  0.00,  0.00, -1.41]
  cat: [-1.41, -1.10,  0.88, -0.00]
  dog: [-1.41,  1.10, -0.88, -0.00]
 hate: [-1.41,  0.88,  1.10, -0.00]
 love: [-1.41, -0.88, -1.10, -0.00]
white: [-1.41,  0.00,  0.00,  1.41]
```

From the output, we can infer that the fourth topic still represents "color", whereas the meanings of "animal" and "sentiment" are distributed across the second and third topics. This suggests that each column does not necessarily represent a unique topic; rather, it is a combination across multiple columns that may represent a set of topics.

:::warning
**Q6**: $$\Sigma$$ is not **transposed** in L3 of the above code. Should we use `S.transpose()` instead?
:::

## References

Source: [latent\_semantic\_analysis.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/latent_semantic_analysis.py)

1. [Latent Semantic Analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis), Wikipedia.
2. [Singular Value Decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition), Wikipedia.
