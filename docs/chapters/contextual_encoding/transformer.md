---
title: Transformer
---

# Transformer

## Self Attention

Self-attention, also known as scaled dot-product attention, is a fundamental mechanism used in deep learning and natural language processing, particularly in transformer-based models like BERT, GPT, and their variants. Self-attention is a crucial component that enables these models to understand relationships and dependencies between words or tokens in a sequence.

Here's an overview of self-attention:

1. **The Motivation**:
   * The primary motivation behind self-attention is to capture dependencies and relationships between different elements within a sequence, such as words in a sentence or tokens in a document.
   * It allows the model to consider the context of each element based on its relationships with other elements in the sequence.
2. **The Mechanism**:
   * Self-attention computes a weighted sum of the input elements (usually vectors) for each element in the sequence. This means that each element can attend to and be influenced by all other elements.
   * The key idea is to learn weights (attention scores) that reflect how much focus each element should give to the others. These weights are often referred to as "attention weights."
3. **Attention Weights**:
   * Attention weights are calculated using a similarity measure (typically the dot product) between a query vector and a set of key vectors.
   * The resulting attention weights are then used to take a weighted sum of the value vectors. This weighted sum forms the output for each element.
4. **Scaling and Softmax**:
   * To stabilize the gradients during training, the dot products are often scaled by the square root of the dimension of the key vectors.
   * After scaling, a softmax function is applied to obtain the attention weights. The softmax ensures that the weights are normalized and sum to 1.
5. **Multi-Head Attention**:
   * Many models use multi-head attention, where multiple sets of queries, keys, and values are learned. Each set of attention weights captures different aspects of relationships in the sequence.
   * These multiple sets of attention results are concatenated and linearly transformed to obtain the final output.
6. **Applications**:
   * Self-attention is widely used in transformer-based models for various NLP tasks, including machine translation, text classification, text generation, and more.
   * It is also applied in computer vision tasks, such as image captioning, where it can capture relationships between different parts of an image.

Self-attention is a powerful mechanism because it allows the model to focus on different elements of the input sequence depending on the context. This enables the model to capture long-range dependencies, word relationships, and nuances in natural language, making it a crucial innovation in deep learning for NLP and related fields.

:::warning
**Q9**: How does **self-attention** operate given an embedding matrix $$\mathrm{W} \in \mathbb{R}^{n \times d}$$ representing a document, where $$n$$ is the number of words and $$d$$ is the embedding dimension?
:::

## Multi-head Attention

Multi-head attention is a crucial component in transformer-based models, such as BERT, GPT, and their variants. It extends the basic self-attention mechanism to capture different types of relationships and dependencies in a sequence. Here's an explanation of multi-head attention:

1. **Motivation**:
   * The primary motivation behind multi-head attention is to enable a model to focus on different parts of the input sequence when capturing dependencies and relationships.
   * It allows the model to learn multiple sets of attention patterns, each suited to capturing different kinds of associations in the data.
2. **Mechanism**:
   * In multi-head attention, the input sequence (e.g., a sentence or document) is processed by multiple "attention heads."
   * Each attention head independently computes attention scores and weighted sums for the input sequence, resulting in multiple sets of output values.
   * These output values from each attention head are then concatenated and linearly transformed to obtain the final multi-head attention output.
3. **Learning Different Dependencies**:
   * Each attention head can learn to attend to different aspects of the input sequence. For instance, one head may focus on syntactic relationships, another on semantic relationships, and a third on longer-range dependencies.
   * By having multiple heads, the model can learn to capture a variety of dependencies, making it more versatile and robust.
4. **Multi-Head Processing**:
   * In each attention head, there are three main components: queries, keys, and values. These are linearly transformed projections of the input data.
   * For each head, queries are compared to keys to compute attention weights, which are then used to weight the values.
   * Each attention head performs these calculations independently, allowing it to learn a unique set of attention patterns.
5. **Concatenation and Linear Transformation**:
   * The output values from each attention head are concatenated into a single tensor.
   * A linear transformation is applied to this concatenated output to obtain the final multi-head attention result. The linear transformation helps the model combine information from all heads appropriately.
6. **Applications**:
   * Multi-head attention is widely used in NLP tasks, such as text classification, machine translation, and text generation.
   * It allows models to capture diverse dependencies and relationships within text data, making it highly effective in understanding and generating natural language.

Multi-head attention has proven to be a powerful tool in transformer architectures, enabling models to handle complex and nuanced relationships within sequences effectively. It contributes to the remarkable success of transformer-based models in a wide range of NLP tasks.

<figure>
<img src={require('/img/contextual_encoding/multi-head-attention.png').default} alt="Multi-Head Attention" width="563" />
<figcaption>Multi-Head Attention. Figure 2 from [1].</figcaption>
</figure>

:::warning
**Q10**: Given an embedding matrix $$\mathrm{W} \in \mathbb{R}^{n \times d}$$ representing a document, how does **multi-head attention** function? What advantages does multi-head attention offer over self-attention?
:::

## Transformer Architecture

<figure>
<img src={require('/img/contextual_encoding/transformer.png').default} alt="The Transformer architecture" width="375" />
<figcaption>The Transformer architecture. Figure 1 from [1].</figcaption>
</figure>

:::warning
**Q11**: What are the outputs of **each layer** in the **Transformer** model? How do the embeddings learned in the upper layers of the Transformer differ from those in the lower layers?
:::

## BERT

<figure>
<img src={require('/img/contextual_encoding/bert-training.png').default} alt="BERT training mechanisms" />
<figcaption>BERT training mechanisms. Figure 1 from [2].</figcaption>
</figure>

:::warning
**Q12**: How is a **Masked Language Model** used in training a language model with a transformer?
:::

:::warning
**Q13**: How can one train a **document-level embedding** using a transformer?
:::

:::warning
**Q14**: What are the advantages of embeddings generated by **BERT** compared to those generated by [Word2Vec](/chapters/distributional_semantics/neural-language-models)?
:::

## References

1. [Attention is All you Need](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html), Vaswani et al., NIPS 2017.
2. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423.pdf), Devlin et al., NAACL, 2019.
