---
title: Term Weighting
---

# Term Weighting

## Term Frequency

The frequency of a word $$w$$'s occurrences in a document $$D$$ is called the **Term Frequency (TF)** of $$w \in D$$. TF is often used to determine the importance of a term within a document such that  terms that appear more frequently are considered more relevant to the document's content.

However, TF alone does not always reflect the semantic importance of a term. To demonstrate this limitation, let us define a function that takes a filepath to a corpus and returns a list of documents, with each document represented as a separate line in the corpus:

```python showLineNumbers
from typing import Callable

def read_corpus(filename: str, tokenizer: Callable[[str], list[str]] | None = None) -> list[Document]:
    fin = open(filename)
    if tokenizer is None: tokenizer = lambda s: s.split()
    return [tokenizer(line) for line in fin]
```

* L3: [union types](https://peps.python.org/pep-0604/), [callable objects](https://docs.python.org/3/library/typing.html#annotating-callable-objects), [default arguments](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).
* L5: Define a tokenizer function using a [lambda](https://docs.python.org/3/reference/expressions.html#lambda) expression.

We then retrieve documents in [chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt) and create a vocaburay dictionary:

```python showLineNumbers
from src.bag_of_words_model import vocabulary

corpus = read_corpus('dat/chronicles_of_narnia.txt')
vocab = vocabulary(corpus)
```

Let us define a function that takes a vocabulary dictionary, a tokenizer, and a list of documents, and prints the TFs of all terms in each document using the [bag of words model](bag-of-words-model.md):

```python showLineNumbers
from src.bag_of_words_model import bag_of_words, Document, Vocab

def print_tfs(vocab: Vocab, documents: list[Document]):
    tfs = [bag_of_words(vocab, document) for document in documents]
    words = [word for word, _ in sorted(vocab.items(), key=lambda x: x[1])]
    for tf in tfs:
        print([(words[index], count) for index, count in sorted(tf.items(), key=lambda x: x[1], reverse=True)])
```

* L5: The underscore (`_`) is used to indicate that the variable is not being used in the loop.

At last, let us print the TFs of all terms in the following three documents:

```python showLineNumbers title="Run"
from elit_tokenizer import EnglishTokenizer

ds = [
    "As dawn broke, the first light kissed the golden mane of Aslan, the rightful king of Narnia.",
    "The White Witch's icy breath froze the once lush meadows, casting a shadow over Narnia.",
    "Lucy's footsteps echoed in the halls of Cair Paravel, where legends were born."
]

etok = EnglishTokenizer()
documents = [etok.decode(d).tokens  for d in ds]
print_tfs(vocab, documents)
```

```python title="Output"
[('the', 3), (',', 2), ('of', 2), ('.', 1), ('As', 1), ('Aslan', 1), ('Narnia', 1), ('broke', 1), ('dawn', 1), ('first', 1), ('golden', 1), ('king', 1), ('kissed', 1), ('light', 1), ('mane', 1), ('rightful', 1)]
[("'s", 1), (',', 1), ('.', 1), ('Narnia', 1), ('The', 1), ('White', 1), ('Witch', 1), ('a', 1), ('breath', 1), ('casting', 1), ('froze', 1), ('icy', 1), ('once', 1), ('over', 1), ('shadow', 1), ('the', 1)]
[("'s", 1), (',', 1), ('.', 1), ('Cair', 1), ('Lucy', 1), ('Paravel', 1), ('born', 1), ('echoed', 1), ('footsteps', 1), ('halls', 1), ('in', 1), ('legends', 1), ('of', 1), ('the', 1), ('were', 1), ('where', 1)]
```

In the first document, terms that are typically considered semantically important, such as "_Aslan_" or "_Narnia_," receive a TF of 1, whereas functional terms such as "_the_" or punctuation like "," or "." receive higher TFs.

:::warning
**Q3**: If term frequency does not necessarily indicate **semantic importance**, what kind of significance does it convey?
:::

## Stopwords

One simple approach to addressing this issue is to discard common terms with little sematnic values, referred to as **stop words**, which occur frequently but do not convey significant information about the content of the text. By removing stop words, the focus can be placed on the more meaningful content words, which are often more informative for downstream tasks.

Let us retrieve a set of commonly used stop words from [**stopwords.txt**](https://github.com/emory-courses/nlp-essentials/blob/main/dat/stopwords.txt) and define a function to determine if a term should be considered a stop word:

```python showLineNumbers
from string import punctuation

stopwords = {line.strip().lower() for line in open('dat/stopwords.txt')}
is_stopwords = lambda w: w.lower() in stopwords or w in punctuation
```

* L1: [string.punctuation](https://docs.python.org/3/library/string.html#string.punctuation).

Next, we define a tokenizer that excludes stop words during the tokenization process, and use it to retrieve the vocabulary:

```python showLineNumbers
sw_tokenizer = lambda s: [word for word in s.split() if not is_stopwords(word)]
corpus = read_corpus('dat/chronicles_of_narnia.txt', sw_tokenizer)
vocab = vocabulary(corpus)
```

Finally, let us print the TFs of the same documents using the updated vocabulary:

```python showLineNumbers title="Run"
print_tfs(vocab, documents)
```

```python title="Output"
[('Aslan', 1), ('Narnia', 1), ('broke', 1), ('dawn', 1), ('golden', 1), ('king', 1), ('kissed', 1), ('light', 1), ('mane', 1), ('rightful', 1)]
[("'s", 1), ('Narnia', 1), ('White', 1), ('Witch', 1), ('breath', 1), ('casting', 1), ('froze', 1), ('icy', 1), ('shadow', 1)]
[("'s", 1), ('Cair', 1), ('Lucy', 1), ('Paravel', 1), ('born', 1), ('echoed', 1), ('footsteps', 1), ('halls', 1), ('legends', 1)]
```

:::warning
**Q4**: Stop words can be filtered either during the **creation** of vocabulary dictionary or when **generating** the bag-of-words representations. Which approach is preferable and why?
:::

## Document Frequency

Filtering out stop words allows us to generate less noisy vector representations. However, in the above examples, all terms now have the same TF of 1, treating them equally important. A more sophisticated weighting approach involves incorporating information about terms across multiple documents.

**Document Frequency (DF)** is a measure to quantify how often a term appears across a set of documents within a corpus such that it represents the number of documents within the corpus that contain a particular term.

Let us define a function that takes a vocabulary dictionary and a corpus, and returns a dictionary whose keys are term IDs and values are their corresponding document frequencies:

```python showLineNumbers
from collections import Counter
from src.types import SparseVector

def document_frequencies(vocab: Vocab, corpus: list[Document]) -> SparseVector:
    counts = Counter()
    for document in corpus:
        counts.update(set(document))
    return {vocab[word]: count for word, count in sorted(counts.items()) if word in vocab}
```

We then compare the term and document frequencies of all terms in the above documents:

```python showLineNumbers title="Run"
corpus = read_corpus('dat/chronicles_of_narnia.txt')
vocab = vocabulary(corpus)
words = [word for word, _ in sorted(vocab.items(), key=lambda x: x[1])]

dfs = document_frequencies(vocab, corpus)
for document in documents:
    bow = bag_of_words(vocab, document)
    tf_df = [(words[tid], tf, dfs[tid]) for tid, tf in sorted(bow.items())]
    tf_df = sorted(tf_df, key=lambda x: (-x[1], x[2]))
    print(' '.join(document))
    print('\n'.join(['{:>10}  {}  {:>5}'.format(*t) for t in tf_df]))
```

* L9: Sort the list of tuples by the second item first in descending order then by the third item in ascending order.
* L11: The tuple `t` is [unpacked](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments) into three arguments and passed to the [format()](https://docs.python.org/3/library/string.html#format-specification-mini-language) function.

```text title="Output"
As dawn broke , the first light kissed the golden mane of Aslan , the rightful king of Narnia .
       the  3   9574
        of  2   5355
         ,  2  10578
  rightful  1      1
      dawn  1      6
    kissed  1     26
     broke  1     35
      king  1     40
      mane  1     40
    golden  1     52
        As  1    161
     light  1    203
     first  1    401
    Narnia  1    512
     Aslan  1    706
         .  1  19747
The White Witch 's icy breath froze the once lush meadows , casting a shadow over Narnia .
   casting  1      1
     froze  1      2
       icy  1      3
    shadow  1     38
     White  1     44
    breath  1     86
     Witch  1    246
      once  1    378
      over  1    431
    Narnia  1    512
       The  1   1352
        's  1   2404
         a  1   5456
       the  1   9574
         ,  1  10578
         .  1  19747
Lucy 's footsteps echoed in the halls of Cair Paravel , where legends were born .
 footsteps  1      1
   legends  1      1
    echoed  1      2
     halls  1      4
      born  1     14
   Paravel  1     84
      Cair  1     86
     where  1    360
      Lucy  1    704
      were  1   1684
        's  1   2404
        in  1   3513
        of  1   5355
       the  1   9574
         ,  1  10578
         .  1  19747
```

Notice that functional terms with high TFs such as "_the_" or "_of_," as well as punctuation, also have high DFs. Thus, it is possible to estimate more semantically important term scores through appropriate weighting between these two types of frequencies.

:::warning
**Q5**: What are the implications when a term has a high **document frequency**?
:::

## TF-IDF

**Term Frequency - Inverse Document Frequency (TF-IDF)** is used to measure the importance of a term in a document relative to a corpus of documents by combining two metrics: term frequency (TF) and inverse document frequency (IDF).

Given  a term $$t$$ in a document $$d \in D$$ where $$D$$ is a set of all documents in a corpus, its TF-IDF score can be measured as follow:

$$
\begin{align*}
    \mathbf{TF-IDF}(t, d, D) &= \mathbf{TF}(t, d) \cdot \mathbf{IDF}(t, D) \\
    \mathbf{TF}(t, d) &= \frac{\#(t, d)}{|d|} \\
    \mathbf{IDF}(t, D) &= \log\frac{|D|}{\mathbf{DF}(t, D)} \\
\end{align*}
$$

In this formulation, **TF** is calculated using the normalized count of the term's occurrences in the document instead of the raw count. **IDF** measures how rare a term is across a corpus of documents and is calculated as the logarithm of the ratio of the total number of documents in the corpus to the DF of the term.

Let us define a function that takes a vocabulary dictionary, a DF dictionary, the size of all documents, and a document, and returns the TF-IDF scores of all terms in the document:

```python showLineNumbers
def tf_idf(vocab: Vocab, dfs: SparseVector, D: int, document: Document) -> SparseVector:
    tf = lambda count: count / len(document)
    idf = lambda tid: math.log(D / dfs[tid])
    return {tid: tf(count) * idf(tid) for tid, count in bag_of_words(vocab, document).items()}
```

We then compute the TF-IDF scores of terms in the above documents:

```python showLineNumbers title="Run"
for document in documents:
    tfidf = tf_idf(vocab, dfs, len(corpus), document)
    print(' '.join(document))
    print('\n'.join(['{:>10}  {:.2f}'.format(words[tid], score) for tid, score in sorted(tfidf.items(), key=lambda x: x[1], reverse=True)]))
```

```text title="Output"
As dawn broke , the first light kissed the golden mane of Aslan , the rightful king of Narnia .
  rightful  0.50
      dawn  0.41
    kissed  0.34
     broke  0.32
      king  0.32
      mane  0.32
    golden  0.30
        As  0.25
     light  0.24
     first  0.20
    Narnia  0.19
     Aslan  0.17
        of  0.14
       the  0.13
         ,  0.08
         .  0.01
The White Witch 's icy breath froze the once lush meadows , casting a shadow over Narnia .
   casting  0.56
     froze  0.52
       icy  0.50
    shadow  0.35
     White  0.35
    breath  0.31
     Witch  0.25
      once  0.23
      over  0.22
    Narnia  0.21
       The  0.16
        's  0.12
         a  0.08
       the  0.05
         ,  0.04
         .  0.01
Lucy 's footsteps echoed in the halls of Cair Paravel , where legends were born .
 footsteps  0.63
   legends  0.63
    echoed  0.58
     halls  0.54
      born  0.46
   Paravel  0.35
      Cair  0.35
     where  0.26
      Lucy  0.22
      were  0.16
        's  0.14
        in  0.12
        of  0.09
       the  0.05
         ,  0.05
         .  0.01
```

Various of TF-IDF have been proposed to enhance the representation in certain contexts:

* Sublinear scaling on TF: $$\left\lbrace \begin{array}{cl}  1 + \log\mathbf{TF}(t,d) & \text{if } \mathbf{TF}(t,d) > 0\\  0 & \text{otherwise} \end{array} \right.$$
* Normalized TF: $$\alpha + (1-\alpha)\frac{\mathbf{TF}(t,d)}{\max(\mathbf{TF}(*,d))}$$
* Normalized IDF: $$\frac{\max(\mathbf{IDF}(*,D))}{\mathbf{IDF}(t,D)}$$
* Probabilistic IDF: $$\frac{|D| - \mathbf{DF}(t,D)}{\mathbf{DF}(t,D)}$$

:::warning
**Q6**: Should we still apply **stop words** when using TF-IDF scores to represent the documents?
:::

## References

1. Source: [term\_weighting.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/term_weighing.py)
