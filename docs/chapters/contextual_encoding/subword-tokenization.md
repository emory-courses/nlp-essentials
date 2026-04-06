---
title: Subword Tokenization
---

# Subword Tokenization

**Byte Pair Encoding** (BPE) is a data compression algorithm that is commonly used in the context of subword tokenization for [neural language models](/chapters/distributional_semantics/neural-language-models). BPE [tokenizes](/chapters/text_processing/tokenization) text into smaller units, such as subword pieces or characters, to handle out-of-vocabulary words, reduce vocabulary size, and enhance the efficiency of language models.

## Algorithm

The following describes the steps of BPE in terms of the [EM algorithm](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm):

1. **Initialization**: Given a dictionary consisting of all words and their counts in a corpus, the symbol vocabulary is initialized by tokenizing each word into its most basic subword units, such as characters.
2. **Expectation**: With the (updated) symbol vocabulary, it calculates the frequency of every symbol pair within the vocabulary.
3. **Maximization**: Given all symbol pairs and their frequencies, it merges the top-_k_ most frequent symbol pairs in the vocabulary.
4. Steps 2 and 3 are repeated until meaningful sets of subwords are found for all words in the corpus.

:::warning
**Q4**: The **EM algorithm** stands as a classic method in unsupervised learning. What are the advantages of **unsupervised learning** over supervised learning, and which tasks align well with unsupervised learning?
:::

## Implementation

Let us consider a toy vocabulary:

```python showLineNumbers
from src.types import WordCount, PairCount
EOW = '[EoW]'

word_counts = {
    'high': 12,
    'higher': 14,
    'highest': 10,
    'low': 12,
    'lower': 11,
    'lowest': 13
}
```

First, we create the symbol vocabulary by inserting a space between every pair of adjacent characters and adding a special symbol `[EoW]` at the end to indicate the End of the Word:

```python showLineNumbers
def initialize(word_counts: WordCount) -> WordCount:
    return {' '.join(list(word) + [EOW]): count for word, count in word_counts.items()}
```

Next, we count the frequencies of all symbol pairs in the vocabulary:

```python showLineNumbers
def expect(vocab: WordCount) -> PairCount:
    pairs = collections.defaultdict(int)

    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i + 1]] += freq

    return pairs
```

Finally, we update the vocabulary by merging the most frequent symbol pair across all words:

```python
def maximize(vocab: WordCount, pairs: PairCount) -> WordCount:
    best = max(pairs, key=pairs.get)
    p = re.compile(r'(?<!\S)' + re.escape(' '.join(best)) + r'(?!\S)')
    return {p.sub(''.join(best), word): freq for word, freq in vocab.items()}
```

The `expect()` and `maximize()` can be repeated for multiple iterations until the tokenization becomes reasonable:

```python showLineNumbers
def bpe_vocab(word_counts: WordCount, max_iter: int):
    vocab = initialize(word_counts)

    for i in range(max_iter):
        pairs = expect(vocab)
        vocab = maximize(vocab, pairs)
        # print(vocab)

    return vocab
```

When you uncomment `L7` in `bpe_vocab()`, you can see how the symbols are merged in each iteration:

```python showLineNumbers title="Run"
bpe_vocab(word_counts, 10)
```

```text title="Output"
{'hi g h [EoW]': 12, 'hi g h e r [EoW]': 14, 'hi g h e s t [EoW]': 10, 'l o w [EoW]': 12, 'l o w e r [EoW]': 11, 'l o w e s t [EoW]': 13}
{'hig h [EoW]': 12, 'hig h e r [EoW]': 14, 'hig h e s t [EoW]': 10, 'l o w [EoW]': 12, 'l o w e r [EoW]': 11, 'l o w e s t [EoW]': 13}
{'high [EoW]': 12, 'high e r [EoW]': 14, 'high e s t [EoW]': 10, 'l o w [EoW]': 12, 'l o w e r [EoW]': 11, 'l o w e s t [EoW]': 13}
{'high [EoW]': 12, 'high e r [EoW]': 14, 'high e s t [EoW]': 10, 'lo w [EoW]': 12, 'lo w e r [EoW]': 11, 'lo w e s t [EoW]': 13}
{'high [EoW]': 12, 'high e r [EoW]': 14, 'high e s t [EoW]': 10, 'low [EoW]': 12, 'low e r [EoW]': 11, 'low e s t [EoW]': 13}
{'high [EoW]': 12, 'high er [EoW]': 14, 'high e s t [EoW]': 10, 'low [EoW]': 12, 'low er [EoW]': 11, 'low e s t [EoW]': 13}
{'high [EoW]': 12, 'high er[EoW]': 14, 'high e s t [EoW]': 10, 'low [EoW]': 12, 'low er[EoW]': 11, 'low e s t [EoW]': 13}
{'high [EoW]': 12, 'high er[EoW]': 14, 'high es t [EoW]': 10, 'low [EoW]': 12, 'low er[EoW]': 11, 'low es t [EoW]': 13}
{'high [EoW]': 12, 'high er[EoW]': 14, 'high est [EoW]': 10, 'low [EoW]': 12, 'low er[EoW]': 11, 'low est [EoW]': 13}
{'high [EoW]': 12, 'high er[EoW]': 14, 'high est[EoW]': 10, 'low [EoW]': 12, 'low er[EoW]': 11, 'low est[EoW]': 13}
```

:::warning
**Q5**: What are the disadvantages of using **BPE-based tokenization** instead of [rule-based tokenization](/chapters/text_processing/tokenization)? What are the potential issues with the implementation of BPE above?
:::

## References

Source code: [src/byte\_pair\_encoding.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/byte_pair_encoding.py)

1. [Neural Machine Translation of Rare Words with Subword Units](http://dx.doi.org/10.18653/v1/P16-1162), Sennrich et al., ACL, 2016.
2. [A New Algorithm for Data Compression](https://github.com/emory-courses/nlp-essentials/blob/main/dat/contextual_representations/gage-1994.pdf), Gage, The C Users Journal, 1994.
3. [SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing](http://dx.doi.org/10.18653/v1/D18-2012), Kudo and Richardson, EMNLP, 2018.
4. [Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation](https://arxiv.org/abs/1609.08144) (WordPiece), Wu et al., arXiv, 2016.
