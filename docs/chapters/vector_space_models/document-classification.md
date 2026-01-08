---
title: Document Classification
---

# Document Classification

**Document classification**, also known as text classification, is a task that involves assigning predefined categories or labels to documents based on their content, used to automatically organize, categorize, or label large collections of textual documents.

## Supervised Learning

**Supervised learning** is a machine learning paradigm where the algorithm is trained on a labeled dataset, with each data point (instance) being associated with a corresponding target label or output. The goal of supervised learning is to learn a mapping function from input features to output labels, which enables the algorithm to make predictions or decisions on unseen data.

## Data Split

Supervised learning typically involves dividing the entire dataset into training, development, and evaluation sets. The **training set** is used to train a model, the **development set** to tune the model's hyperparameters, and the **evaluation set** to assess the best model tuned on the development set.

It is critical to ensure that the evaluation set is never used to tune the model during training. Common practice involves splitting the dataset such as 80/10/10 or 75/10/15 for training, development, and evaluation sets, respectively.

The [document\_classification](https://github.com/emory-courses/nlp-essentials/tree/main/dat/document_classification) directory contains the training (trn), development (dev), and evaluation (tst) sets comprising 82, 14, and 14 documents, respectively. Each document is a chapter from the [chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt) file, following a file-naming convention of `A_B`, where `A` denotes the book ID and `B` indicates the chapter ID.

Let us define a function that takes a path to a directory containing training documents and returns a dictionary, where each key in the dictionary corresponds to a book label, and its associated value is a list of documents within that book:

```python showLineNumbers
from src.bag_of_words_model import Document
import glob, os

def collect(dirpath: str) -> dict[int, list[Document]]:
    books = dict()

    for filename in glob.glob(os.path.join(dirpath, '*.txt')):
        t = os.path.basename(filename).split('_')
        book_id = int(t[0])
        fin = open((filename))
        books.setdefault(book_id, list()).append(fin.read().split())

    return books
```

* L7: the [glob](https://docs.python.org/3/library/glob.html) module, the [os](https://docs.python.org/3/library/os.html) module.

We then print the number of documents in each set:

```python showLineNumbers title="Run"
def join_documents(dataset: dict[int, list[Document]]) -> list[Document]:
    return [document for documents in dataset.values() for document in documents]

trn = collect('dat/document_classification/trn')
dev = collect('dat/document_classification/dev')
tst = collect('dat/document_classification/tst')
print(len(join_documents(trn)), len(join_documents(dev)), len(join_documents(tst)))
```

```python title="Output"
82 14 14
```

:::warning
**Q8**: What potential problems might arise from the above **data splitting** approach, and what alternative method could mitigate these issues?
:::

## Vectorization

To vectorize the documents, let us gather the vocabulary and their document frequencies from the training set:

```python showLineNumbers
corpus = join_documents(trn)
vocab = vocabulary(join_documents(trn))
dfs = document_frequencies(vocab, corpus)
D = len(corpus)
```

Let us create a function that takes the vocabulary, document frequencies, document length, and a document set, and returns a list of tuples, where each tuple consists of a book ID and a sparse vector representing a document in the corresponding book:

```python showLineNumbers
def vectorize(vocab: Vocab, dfs: SparseVector, D: int, docset: dict[int, list[Document]]) -> list[tuple[int, SparseVector]]:
    vs = []

    for book_id, documents in docset.items():
        for document in documents:
            vs.append((book_id, tf_idf(vocab, dfs, D, document)))

    return vs
```

We then vectorize all documents in each set:

```python showLineNumbers
trn_vs = vectorize(vocab, dfs, D, trn)
dev_vs = vectorize(vocab, dfs, D, dev)
tst_vs = vectorize(vocab, dfs, D, tst)
```

:::warning
**Q9**: Why do we use only the **training set** to collect the vocabulary?
:::

## Classification

Let us develop a classification model using the **K-nearest neighbors algorithm** \[1] that takes the training vector set, a document, and $$k$$, and returns the predicted book ID of the document and its similarity score:

```python showLineNumbers
def knn(trn_vs: list[tuple[int, SparseVector]], v: SparseVector, k: int = 1) -> tuple[int, float]:
    sims = [(book_id, cosine_similarity(v, t)) for book_id, t in trn_vs]
    sims.sort(key=lambda x: x[1], reverse=True)
    return Counter(sims[:k]).most_common(1)[0][0]
```

* L2: Measure the similarity between the input document $$v$$ and every document $$t$$ in the training set and save it with the book ID of $$t$$.
* L3-4: Return the most common book ID among the top-$$k$$ documents in the training set that are most similar to $$v$$.

Finally, we test our classification model on the development set:

```python showLineNumbers title="Run"
correct = 0

for g_book_id, document in dev_vs:
    p_book_id, p_score = knn(trn_vs, document)
    if g_book_id == p_book_id: correct += 1
    print('Gold: {}, Auto: {}, Score: {:.2f}'.format(g_book_id, p_book_id, p_score))

print('Accuracy: {} ({}/{})'.format(100 * correct / len(dev_vs), correct, len(dev_vs)))
```

```text title="Output"
Gold: 1, Auto: 1, Score: 0.49
Gold: 1, Auto: 1, Score: 0.27
Gold: 3, Auto: 3, Score: 0.36
Gold: 3, Auto: 3, Score: 0.32
Gold: 5, Auto: 5, Score: 0.29
Gold: 5, Auto: 5, Score: 0.54
Gold: 0, Auto: 0, Score: 0.32
Gold: 0, Auto: 0, Score: 0.26
Gold: 6, Auto: 6, Score: 0.48
Gold: 6, Auto: 6, Score: 0.49
Gold: 2, Auto: 2, Score: 0.37
Gold: 2, Auto: 2, Score: 0.31
Gold: 4, Auto: 4, Score: 0.56
Gold: 4, Auto: 4, Score: 0.60
Accuracy: 100.0 (14/14)
```

:::warning
**Q10**: What are the primary weaknesses and limitations of the **K-Nearest Neighbors (KNN)** classification model when applied to document classification?
:::

## References

Source: [document\_classification.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/document_classification.py)

1. [K-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), Wikipedia.
