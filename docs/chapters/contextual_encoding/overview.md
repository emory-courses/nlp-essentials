---
title: Overview
---

# Contextual Encoding

**Contextual representations** are representations of words, phrases, or sentences within the context of the surrounding text. Unlike word embeddings from [Word2Vec](/chapters/distributional_semantics/neural-language-models) where each word is represented by a fixed vector regardless of its context, contextual representations capture the meaning of a word or sequence of words based on their context in a particular document such that the representation of a word can vary depending on the words surrounding it, allowing for a more nuanced understanding of meaning in natural language processing tasks.

## Contents

* [Subword Tokenization](subword-tokenization)
* [Recurrent Neural Networks](recurrent-neural-networks)
* [Transformer](transformer)
* [Encoder-Decoder Framework](encoder-decoder-framework)
* [Homework](homework)

## References

* [Attention is All You Need](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html), Vaswani et al., Proceedings of Advances in Neural Information Processing Systems (NeurIPS), 2017.

:::warning
**Q1**: How can **document-level vector representations** be derived from [Word2Vec](/chapters/distributional_semantics/neural-language-models) word embeddings?
:::

:::warning
**Q2**: How did the embedding representation facilitate the adaption of **Neural Networks** in Natural Language Processing?
:::

:::warning
**Q3**: How are embedding representations for **Natural Language Processing** fundamentally different from ones for **Computer Vision**?
:::
