---
title: Smoothing
---

# Smoothing

## Unigram Smoothing

The [unigram model](n-gram-models.md#unigram-estimation) in the previous section faces a challenge when confronted with words that do not occur in the corpus, resulting in a probability of 0. One common technique to address this challenge is **smoothing**, which tackles issues such as zero probabilities, data sparsity, and overfitting that emerge during probability estimation and predictive modeling with limited data.

**Laplace smoothing** (aka. add-one smoothing) is a simple yet effective technique that avoids zero probabilities and distributes the probability mass more evenly. It adds the count of 1 to every word and recalculates the unigram probabilities:

$$
P_{\mathcal{L}}(w_i) = \frac{\#(w_i) + 1}{\sum_{\forall w_k \in V} (\#(w_k) + 1)} = \frac{\#(w_i) + 1}{\sum_{\forall w_k \in V} \#(w_k) + |V|}
$$

Thus, the probability of any unknown word $$w_*$$with Laplace smoothing is calculated as follows:

$$
P_{\mathcal{L}}(w_*) = \frac{1}{\sum_{\forall w_k \in V} \#(w_k) + |V|}
$$

The unigram probability of an unknown word is guaranteed to be lower than the unigram probabilities of any known words, whose counts have been adjusted to be greater than 1.

Note that the sum of all unigram probabilities adjusted by Laplace smoothing is still 1:

$$
\sum_{i=1}^v P(w_i) = \sum_{i=1}^v P_{\mathcal{L}}(w_i) = 1
$$

Let us define a function `unigram_smoothing()` that takes a file path and returns a dictionary with bigrams and their probabilities as keys and values, respectively, estimated by Laplace smoothing:

```python showLineNumbers
from src.ngram_models import unigram_count, Unigram

UNKNOWN = ''

def unigram_smoothing(filepath: str) -> Unigram:
    counts = unigram_count(filepath)
    total = sum(counts.values()) + len(counts)
    unigrams = {word: (count + 1) / total for word, count in counts.items()}
    unigrams[UNKNOWN] = 1 / total
    return unigrams
```

* L1: Import the `unigram_count()` function from the [src.ngram\_models](https://github.com/emory-courses/nlp-essentials/blob/main/src/ngram_models.py) package.
* L3: Define a constant representing the unknown word.
* L7: Increment the total count by the vocabulary size.
* L8: Increment each unigram count by 1.
* L9: Add the unknown word to the unigrams with a probability of 1 divided by the total count.

We then test `unigram_smoothing()` with a text file [dat/chronicles\_of\_narnia.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt):

```python showLineNumbers title="Run"
from src.ngram_models import test_unigram

corpus = 'dat/chronicles_of_narnia.txt'
test_unigram(corpus, unigram_smoothing)
```

* L1: Import `test_unigram()` from the [ngram\_models](https://github.com/emory-courses/nlp-essentials/blob/main/src/ngram_models.py) package.

```text title="Output"
         I 0.010225
     Aslan 0.001796
      Lucy 0.001762
    Edmund 0.001369
    Narnia 0.001339
   Caspian 0.001300
      Jill 0.001226
     Peter 0.001005
    Shasta 0.000902
    Digory 0.000899
   Eustace 0.000853
     Susan 0.000636
    Tirian 0.000585
     Polly 0.000533
    Aravis 0.000523
      Bree 0.000479
Puddleglum 0.000479
    Scrubb 0.000469
    Andrew 0.000396
```

```text title="Comparison"
   Unigram  With Smoothing   W/O Smoothing
         I        0.010225        0.010543
     Aslan        0.001796        0.001850
      Lucy        0.001762        0.001815
    Edmund        0.001369        0.001409
    Narnia        0.001339        0.001379
   Caspian        0.001300        0.001338
      Jill        0.001226        0.001262
     Peter        0.001005        0.001034
    Shasta        0.000902        0.000928
    Digory        0.000899        0.000925
   Eustace        0.000853        0.000877
     Susan        0.000636        0.000654
    Tirian        0.000585        0.000601
     Polly        0.000533        0.000547
    Aravis        0.000523        0.000537
      Bree        0.000479        0.000492
Puddleglum        0.000479        0.000492
    Scrubb        0.000469        0.000482
    Andrew        0.000396        0.000406
```

Compared to the unigram results without smoothing (see the "Comparison" tab above), the probabilities for these top unigrams have slightly decreased.

:::warning
**Q4**: When applying **Laplace smoothing**, do **unigram probabilities** always decrease? If not, what conditions can cause a unigram's probability to increase?
:::

The unigram probability of any word (including unknown) can be retrieved using the `UNKNOWN` key:

```python showLineNumbers
def smoothed_unigram(probs: Unigram, word: str) -> float:
    return probs.get(word, unigram[UNKNOWN])
```

* L2: Use [`get()`](https://docs.python.org/3/library/stdtypes.html#dict.get) to retrieve the probability of the target word from `probs`. If the word is not present, default to the probability of the `UNKNOWN` token.

```python showLineNumbers title="Run"
unigram = unigram_smoothing(corpus)
for word in ['Aslan', 'Jinho']:
    print(f'{word} {smoothed_unigram(unigram, word):.6f}')
```

* L2: Test a known word, '_Aslan_', and an unknown word, '_Jinho_'.

```text title="Output"
Aslan 0.001796
Jinho 0.000002
```

## Bigram Smoothing

The bigram model can also be enhanced by applying Laplace smoothing:

$$
P_{\mathcal{L}}(w_i|w_{i-1}) = \frac{\#(w_{i-1},w_{i}) + 1}{\sum_{\forall w_k \in V_{i}} \#(w_{i-1},w_k) + |V|}
$$

Thus, the probability of an unknown bigram $$(w_{u-1}, w_{*})$$ where $$w_{u-1}$$ is known but $$w_{*}$$ is unknown  is calculated as follows:

$$
P_{\mathcal{L}}(w_*|w_{u-1}) = \frac{1}{\sum_{\forall w_k \in V_{i}} \#(w_{u-1},w_k) + |V|}
$$

:::warning
**Q5**: What does the **Laplace smoothed bigram probability** of $$(w_{u-1}, w_{u})$$ represent when $$w_{u-1}$$ is unknown, and what is a potential problem with this estimation?
:::

Let us define a function `bigram_smoothing()` that takes a file path and returns a dictionary with unigrams and their probabilities as keys and values, respectively, estimated by Laplace smoothing:

```python showLineNumbers
from src.ngram_models import bigram_count, Bigram

def bigram_smoothing(filepath: str) -> Bigram:
    counts = bigram_count(filepath)
    vocab = set(counts.keys())
    for _, css in counts.items():
        vocab.update(css.keys())

    bigrams = dict()
    for prev, ccs in counts.items():
        total = sum(ccs.values()) + len(vocab)
        d = {curr: (count + 1) / total for curr, count in ccs.items()}
        d[UNKNOWN] = 1 / total
        bigrams[prev] = d

    bigrams[UNKNOWN] = 1 / len(vocab)
    return bigrams
```

* L1: Import the `bigram_count()` function from the [src.ngram\_models](https://github.com/emory-courses/nlp-essentials/blob/main/src/ngram_models.py) package.
* L5: Create a set `vocab` containing all unique $$w_{i-1}$$.
* L6-7: Add all unique $$w_i$$ to `vocab`.
* L11: Calculate the total count of all bigrams with the same previous word.
* L12: Calculate and store the probabilities of each current word given the previous word
* L13: Calculate the probability for an unknown current word.
* L16: Add a probability for an unknown previous word.

We then test `bigram_smoothing()` with the same text file:

```python showLineNumbers title="Run"
from src.ngram_models import test_bigram

corpus = 'dat/chronicles_of_narnia.txt'
test_bigram(corpus, bigram_smoothing)
```

* L1: Import the `test_bigram()` function from the [ngram\_models](https://github.com/emory-courses/nlp-essentials/blob/main/src/ngram_models.py) package.

```text title="Output"
I
        'm 0.020590
        do 0.019136
       've 0.011143
       was 0.010598
      have 0.009629
        am 0.009084
       'll 0.008236
     think 0.008115
        'd 0.006661
      know 0.006540
the
      same 0.008403
     other 0.007591
      King 0.007096
     Witch 0.006673
     whole 0.005119
    others 0.005084
     first 0.004978
     Dwarf 0.004872
      door 0.004837
     great 0.004837
said
       the 0.039038
         , 0.018270
      Lucy 0.014312
    Edmund 0.011206
   Caspian 0.010049
     Peter 0.009805
      Jill 0.008709
         . 0.008648
    Digory 0.007734
     Aslan 0.007491
```

Finally, we test the bigram estimation using smoothing for unknown sequences:

```python showLineNumbers
def smoothed_bigram(probs: Bigram, prev: str, curr: str) -> float:
    d = probs.get(prev, None)
    return probs[UNKNOWN] if d is None else d.get(curr, d[UNKNOWN])
```

* L2: Retrieve the bigram probabilities of the previous word, or set it to `None` if not present.
* L3: Return the probability of the current word given the previous word with smoothing. If the previous word is not present, return the probability for an unknown previous word.

```python showLineNumbers title="Run"
bigram = bigram_smoothing(corpus)
for word in [('Aslan', 'is'), ('Aslan', 'Jinho'), ('Jinho', 'is')]:
    print(f'{word} {smoothed_bigram(bigram, *word):.6f}')
```

* L3: The tuple word is [unpacked](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments) as passed as the second and third parameters.

```text title="Output"
('Aslan', 'is') 0.001146
('Aslan', 'Jinho') 0.000076
('Jinho', 'is') 0.000081
```

## Normalization

Unlike the unigram case, the sum of all bigram probabilities adjusted by Laplace smoothing given a word $$w_i$$ is not guaranteed to be 1. To illustrate this point, let us consider the following corpus comprising only two sentences:

```
You are a student
You and I are students
```

There are seven word types in this corpus, \{"_I_", "_You_", "_a_", "_and_", "_are_", "_student_", "_students_"\}, such that $$v=7$$. Before Laplace smoothing, the bigram probabilities of $$(w_{i-1} = \textit{You}, w_{i} = *)$$ are estimated as follows:

$$
\begin{align*}
P(\text{\textit{are}|\textit{You}}) = P(\text{\textit{and}|\textit{You}}) &= 1/2 \\
P(\text{\textit{are}|\textit{You}}) + P(\text{\textit{and}|\textit{You}}) &= 1
\end{align*}
$$

However, after applying Laplace smoothing, the bigram probabilities undergo significant changes, and their sum no longer equals 1:

$$
\begin{align*}
P_{\mathcal{L}}(\text{\textit{are}|\textit{You}}) = P_{\mathcal{L}}(\text{\textit{and}|\textit{You}}) &= (1+1)/(2+7) = 2/9 \\
P_{\mathcal{L}}(\text{\textit{are}|\textit{You}}) + P_{\mathcal{L}}(\text{\textit{and}|\textit{You}}) &= 4/9
\end{align*}
$$

The bigram distribution for $$w_{i-1}$$ can be **normalized** to 1 by adding the total number of word types occurring after $$w_{i-1}$$, denoted as $$|V_i|$$, to the denominator instead of $$v$$:

$$
P_{\mathcal{L}}(w_i|w_{i-1}) = \frac{\#(w_{i-1},w_{i}) + 1}{\sum_{\forall w_k \in V_{i}} \#(w_{i-1},w_k) + |V_i|}
$$

Consequently, the probability of an unknown bigram $$(w_{u-1}, w_{*})$$ can be calculated with the normalization as follows:

$$
P_{\mathcal{L}}(w_*|w_{u-1}) = \frac{1}{\sum_{\forall w_k \in V_{i}} \#(w_{u-1},w_k) + |V_i|}
$$

For the above example, $$|V_{i}| = |\lbrace \textit{are}, \textit{and} \rbrace| = 2$$. Once you apply $$|V_{i}|$$ to $$P_{\mathcal{L}}(*|\textit{You})$$, the sum of its bigram probabilities becomes 1:

$$
\begin{align*}
P_{\mathcal{L}}(\text{\textit{are}|\textit{You}}) = P_{\mathcal{L}}(\text{\textit{and}|\textit{You}}) &= (1+1)/(2+2) = 1/2 \\
P_{\mathcal{L}}(\text{\textit{are}|\textit{You}}) + P_{\mathcal{L}}(\text{\textit{and}|\textit{You}}) &= 1
\end{align*}
$$

A major drawback of this normalization is that the probability cannot be measured when $$w_{u-1}$$ is unknown. Thus, we assign the minimum unknown probability across all bigrams as the bigram probability of $$(w_*, w_u)$$, where the previous word is unknown, as follows:

$$
P_{\mathcal{L}}(w_u|w_*) = \min(\{P_{\mathcal{L}}(w_*|w_k) : \forall w_k \in V\})
$$

:::warning
**Q6**: Why is it problematic when **bigram probabilities** following a given word don't sum to 1?
:::

## Reference

1. Source: [smoothing.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/smoothing.py)
2. [Additive smoothing](https://en.wikipedia.org/wiki/Additive_smoothing), Wikipedia
