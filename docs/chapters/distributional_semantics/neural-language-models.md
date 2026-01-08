---
title: Neural Language Models
---

# Neural Language Models

**Neural language models** leverage neural networks trained on extensive text data, enabling them to discern patterns and connections between terms and documents. Through this training, neural language models gain the ability to comprehend and generate human-like language with remarkable fluency and coherence.

## Word2Vec

**Word2Vec** is a neural language model that maps words into a high-dimensional embedding space, positioning similar words closer to each other.

### Continuous Bag-of-Words

Consider a sequence of words, $$\lbrace w_{k-2}, w_{k-1}, w_{k}, w_{k+1}, w_{k+2} \rbrace$$. We can predict $$w_i$$ by leveraging its contextual words using a [generative model](https://en.wikipedia.org/wiki/Generative_model) similar to the [n-gram models](/chapters/language_models/n-gram-models) discussed previously ($$V$$: a vocabulary list comprising all unique words in the corpus):

$$
w_k = \arg\max_{\forall. w_* \in V}P(w_*|w_{k-2},w_{k-1},w_{k+1},w_{k+2})
$$

This objective can also be achieved by using a [discriminative model](https://en.wikipedia.org/wiki/Discriminative_model) such as **Continuous Bag-of-Words** (CBOW) using a [multilayer perceptron](neural-networks.md#multilayer-perceptron). Let $$\mathrm{x} \in \mathbb{R}^{1 \times n}$$ be an input vector, where $$n = \lvert V \rvert$$. $$\mathrm{x}$$ is created by the [bag-of-words](/chapters/vector_space_models/bag-of-words-model) model on a set of context words, $$I = \lbrace w_{k-2},w_{k-1},w_{k+1},w_{k+2} \rbrace$$, such that only the dimensions of $$\mathrm{x}$$ representing words in $$I$$ have a value of $$1$$; otherwise, they are set to $$0$$.

Let $$\mathrm{y} \in \mathbb{R}^{1 \times n}$$ be an output vector, where all dimensions have the value of $$0$$ except for the one representing $$w_k$$, which is set to $$1$$.

Let $$\mathrm{h} \in \mathbb{R}^{1 \times d}$$ be a hidden layer between $$\mathrm{x}$$ and $$\mathrm{y}$$ and $$\mathrm{W}_x \in \mathbb{R}^{n \times d}$$ be the weight matrix between $$\mathrm{x}$$ and $$\mathrm{h}$$, where the sigmoid function is used as the activation function:

$$
\mathrm{h} = \mathrm{sigmoid}(\mathrm{x} \cdot \mathrm{W}_x)
$$

Finally, let $$\mathrm{W}_h \in \mathbb{R}^{n \times d}$$ be the weight matrix between $$\mathrm{h}$$ and $$\mathrm{y}$$:

$$
\mathrm{y} = \mathrm{softmax}(\mathrm{h} \cdot \mathrm{W}_h^T)
$$

Thus, each dimension in $$\mathrm{y}$$ represents the probability of the corresponding word being $$w_k$$ given the set of context words $$I$$.

:::warning
**Q13**: What are the advantages of using **discriminative models** like CBOW for constructing language models compared to **generative models** like n-gram models?
:::

### Skip-gram

In CBOW, a word is predicted by considering its surrounding context. Another approach, known as **Skip-gram**, reverses the objective such that instead of predicting a word given its context, it predicts each of the context words in $$I$$ given $$w_k$$. Formally, the objective of a Skip-gram model is as follows:

$$
\begin{align*}
w_{k-2} &= \arg\max_{\forall. w_* \in V}P(w_*|w_k)\\
w_{k-1} &= \arg\max_{\forall. w_* \in V}P(w_*|w_k)\\
w_{k+1} &= \arg\max_{\forall. w_* \in V}P(w_*|w_k)\\
w_{k+2} &= \arg\max_{\forall. w_* \in V}P(w_*|w_k)
\end{align*}
$$

Let $$\mathrm{x} \in \mathbb{R}^{1 \times n}$$ be an input vector, where only the dimension representing $$w_k$$ is set to $$1$$; all the other dimensions have the value of $$0$$ (thus, $$\mathrm{x}$$ in Skip-gram is the same as $$\mathrm{y}$$ in CBOW). Let $$\mathrm{y} \in \mathbb{R}^{1 \times n}$$ be an output vector, where only the dimension representing $$w_j \in I$$ is set to $$1$$; all the other dimensions have the value of $$0$$. All the other components, such as the hidden layer $$\mathrm{h} \in \mathbb{R}^{1 \times d}$$ and the weight matrices  $$\mathrm{W}_x \in \mathbb{R}^{n \times d}$$ and $$\mathrm{W}_h \in \mathbb{R}^{n \times d}$$, stay the same as the ones in CBOW.

:::warning
**Q14**: What are the advantages of **CBOW** models compared to **Skip-gram** models, and vice versa?
:::

### Distributional Embeddings

What does each dimension in the hidden layer $$\mathrm{h}$$ represent for CBOW? It represents a feature obtained by aggregating specific aspects from each context word in $$I$$, deemed valuable for predicting the target word $$w_i$$. Formally, each dimension $$\mathrm{h}_j$$ is computed as the sigmoid activation of the weighted sum between the input vector $$\mathrm{x}$$ and the column vector such that:

$$
\mathrm{h}_j = \mathrm{sigmoid}(\mathrm{x} \cdot \mathrm{cx}_j)
$$

Then, what does each row vector $$\mathrm{rx}_i = \mathrm{W}_x[i,:]  \in \mathbb{R}^{1 \times d}$$ represent? The $$j$$'th dimension in $$\mathrm{rx}_i$$ denotes the weight of the $$j$$'th feature in $$\mathrm{h}$$ with respect to the $$i$$'th word in the vocabulary. In other words, it indicates the importance of the corresponding feature in representing the $$i$$'th word. Thus, $$\mathrm{r}_i$$ can serve as an embedding for the $$i$$'th word in $$V$$.

What about the other weight matrix $$\mathrm{W}_h$$? The $$j$$'th column vector $$\mathrm{ch}_j = \mathrm{W}_h[:,j] \in \mathbb{R}^{n \times 1}$$ denotes the weights of the $$j$$'th feature in $$\mathrm{h}$$ for all words in the vocabulary. Thus, the $$i$$'th dimension of $$\mathrm{ch}_j$$ indicates the importance of $$j$$'th feature for the $$i$$'th word being predicted as the target word $$w_k$$.

On the other hand, the $$i$$'th row vector $$\mathrm{rh}_i = \mathrm{W}_x[i,:]  \in \mathbb{R}^{1 \times d}$$ denotes the weights of all features for the $$i$$'th word in the vocabulary, enabling it to be utilized as an embedding for  $$w_i \in V$$. However, in practice, only the row vectors of the first weight matrix $$\mathrm{W}_x$$ are employed as word embeddings because the weights in $$\mathrm{W}_h$$ are often optimized for the downstream task, in this case predicting $$w_k$$, whereas the weights in $$\mathrm{W}_x$$ are optimized for finding representations that are generalizable across various tasks.

:::warning
**Q15**: What are the implications of the **weight matrices** $$\mathrm{W}_x$$ and $$\mathrm{W}_h$$ in the Skip-gram model?
:::

:::warning
**Q16**: What limitations does the **Word2Vec** model have, and how can these limitations be addressed?
:::

## References

1. [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean, Proceedings of the International Conference on Learning Representations (ICLR), 2013.
2. [GloVe: Global Vectors for Word Representation](https://aclanthology.org/D14-1162/), Jeffrey Pennington, Richard Socher, Christopher Manning, Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), 2014.
3. [Bag of Tricks for Efficient Text Classification](https://aclanthology.org/E17-2068/), Armand Joulin, Edouard Grave, Piotr Bojanowski, Tomas Mikolov, Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics (EACL), 2017.
