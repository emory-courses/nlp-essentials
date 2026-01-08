---
title: Document Similarity
---

# Document Similarity

Let us vectorize the following three documents using the bag-of-words model with TF-IDF scores estimated from the [chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt) corpus:

```python showLineNumbers title="Run"
from src.bag_of_words_model import vocabulary
from src.term_weighing import read_corpus, document_frequencies, tf_idf

if __name__ == '__main__':
    corpus = read_corpus('dat/chronicles_of_narnia.txt')
    vocab = vocabulary(corpus)
    dfs = document_frequencies(vocab, corpus)
    D = len(corpus)

    documents = [
        'I like this movie very much'.split(),
        'I hate this movie very much'.split(),
        'I love this movie so much'.split()
    ]

    vs = [tf_idf(vocab, dfs, D, document) for document in documents]
    for v in vs: print(vs)
```

```python title="Output"
{980: 0.31, 7363: 0.52, 7920: 0.70, 11168: 0.51, 11833: 0.51}
{980: 0.31, 6423: 1.24, 7920: 0.70, 10325: 0.53, 11168: 0.51}
```

Once the documents are vectorized, they can be compared within the respective vector space. Two common metrics for comparing document vectors are the [Euclidean distance](#euclidean-similarity) and [Cosine similarity](#cosine-similarity).

## Euclidean Similarity

**Euclidean distance** is a measure of the straight-line distance between two vectors in Euclidean space such that it represents the magnitude of the differences between the two vectors.

Let $$V_i = [v_{i1}, \dots, v_{in}]$$ and $$V_j = [v_{j1}, \dots, v_{jn}]$$ be two vectors representing documents $$D_i$$ and $$D_j$$. The Euclidean distance between the two vectors can be measured as follow:

$$
\lVert V_i - V_j \rVert = \sqrt{\sum_{k=1}^n (v_{ik} - v_{jk})^2}
$$

Let us define a function that takes two vectors in our [SpareVector](bag-of-words-model.md) notation and returns the Euclidean distance between them:

```python showLineNumbers
import math
from src.bag_of_words_model import SparseVector

def euclidean_distance(v1: SparseVector, v2: SparseVector) -> float:
    d = sum((v - v2.get(k, 0)) ** 2 for k, v in v1.items())
    d += sum(v ** 2 for k, v in v2.items() if k not in v1)
    return math.sqrt(d)
```

* L6: `** k` represents the power of `k`.

We then measure the Euclidean distance between the two vectors above:

```python showLineNumbers title="Run"
print(euclidean_distance(vs[0], vs[0]))
print(euclidean_distance(vs[0], vs[1]))
print(euclidean_distance(vs[0], vs[2]))
```

```python title="Output"
0.0
1.347450458032576
1.3756015678855296
```

The Euclidean distance between two identical vectors is 0 (L1). Interestingly, the distance between $$v_0$$ and $$v_1$$ is shorter than the distance between $$v_0$$ and $$v_2$$, implying that $$v_1$$ is more similar to $$v_0$$ than $$v_2$$, which contradicts our intuition.

## Cosine Similarity

**Cosine similarity** is a measure of similarity between two vectors in an inner product space such that it calculates the cosine of the angle between two vectors, where a value of 1 indicates that the vectors are identical (i.e., pointing in the same direction), a value of -1 indicates that they are exactly opposite, and a value of 0 indicates that the vectors are orthogonal (i.e., perpendicular to each other).

The cosine similarity between two vectors can be measured as follow:

$$
\frac{V_i\cdot V_j}{\lVert V_i\rVert\lVert V_j\rVert} = \frac{\sum_{\forall k} (v_{ik} \cdot v_{jk})}{\sqrt{\sum_{\forall k} (v_{ik})^2} \cdot \sqrt{\sum_{\forall k} (v_{jk})^2}}
$$

Let us define a function that takes two sparse vectors and returns the cosine similarity between them:

```python showLineNumbers
def cosine_similarity(v1: SparseVector, v2: SparseVector) -> float:
    n = sum(v * v2.get(k, 0) for k, v in v1.items())
    d = math.sqrt(sum(v ** 2 for k, v in v1.items()))
    d *= math.sqrt(sum(v ** 2 for k, v in v2.items()))
    return n / d
```

We then measure the Euclidean distance between the two vectors above:

```python showLineNumbers title="Run"
print(cosine_similarity(vs[0], vs[0]))
print(cosine_similarity(vs[0], vs[1]))
print(cosine_similarity(vs[0], vs[2]))
```

```python title="Output"
0.9999999999999999
0.5775130451716284
0.4826178600593854
```

The Cosine similarity between two identical vectors is 1, although it is calculated as 0.99 due to limitations in decimal points (L1). Similar to the Euclidean distance case, the similarity between $$v_0$$ and $$v_1$$ is greater than the similarity between $$v_0$$ and $$v_2$$, which again contradicts our intuition.

The following diagram illustrates the difference between the two metrics. The Euclidean distance measures the magnitude between two vectors, while the Cosine similarity measures their angle to the origin.

<img src={require('/img/vector_space_models/document_similarity.png').default} width={500} />

:::warning
**Q7**: Why is **Cosine Similarity** generally preferred over **Euclidean Distance** in most NLP applications?
:::
