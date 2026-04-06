---
title: Recurrent Neural Networks
---

# Recurrent Neural Networks

A **Recurrent Neural Network** (RNN) \[1] maintains hidden states of previous inputs and uses them to predict outputs, allowing it to model temporal dependencies in sequential data.

The **hidden state** is a vector representing the network's internal memory of the previous time step. It captures information from previous time steps and influences the predictions made at the current time step, often updated at each time step as the RNN processes a sequence of inputs.

## RNN for Sequence Tagging

Given an input sequence $$X = [x_1, \ldots, x_n]$$ where $$x_i \in \mathbb{R}^{d \times 1}$$, an RNN for sequence tagging defines two functions, $$f$$ and $$g$$:

* $$f$$ takes the current input $$x_i \in X$$ and the hidden state $$h_{i-1}$$ of the previous input $$x_{i-1}$$, and returns a hidden state $$h_i \in \mathbb{R}^{e \times 1}$$ such that $$f(x_i, h_{i-1}) = \alpha(W^x x_i + W^h h_{i-1}) = h_i$$, where $$W^x \in \mathbb{R}^{e \times d}$$, $$W^h \in \mathbb{R}^{e \times e}$$, and $$\alpha$$ is an [activation function](/chapters/distributional_semantics/neural-networks#activation-functions).
* $$g$$ takes the hidden state $$h_i$$ and returns an output $$y_i \in \mathbb{R}^{o \times 1}$$ such that $$g(h_i) = W^o h_i = y_i$$, where $$W^o \in \mathbb{R}^{o \times e}$$.

Figure 1 shows an example of an RNN for sequence tagging, such as part-of-speech tagging:

<figure>
<img src={require('/img/contextual_encoding/rnn-sequence-tagging.png').default} alt="An example of an RNN and its application in part-of-speech (POS) tagging" width="563" />
<figcaption>Figure 1 - An example of an RNN and its application in part-of-speech (POS) tagging.</figcaption>
</figure>

Notice that the output $$y_1$$ for the first input $$x_1$$ is predicted by considering only the input itself such that $$f(x_1, \mathbf{0}) = \alpha(W^x x_1) = h_1$$ (e.g., the POS tag of the first word "_I_" is predicted solely using that word). However, the output $$y_i$$ for every other input $$x_i$$ is predicted by considering both $$x_i$$ and $$h_{i-1}$$, an intermediate representation created explicitly for the task. This enables RNNs to capture sequential information that [Feedforward Neural Networks](/chapters/distributional_semantics/neural-networks) cannot.

:::warning
**Q6**: How does each hidden state $$h_i$$ in a RNN encode information relevant to **sequence tagging** tasks?
:::

## RNN for Text Classification

Unlike sequence tagging where the RNN predicts a sequence of output $$Y = [y_1, \ldots, y_n]$$ for the input $$X = [x_1, \ldots, x_n]$$, an RNN designed for text classification predicts only one output $$y$$ for the entire input sequence such that:

* Sequence Tagging: $$\text{RNN}_{st}(X) \rightarrow Y$$
* Text Classification: $$\text{RNN}_{st}(X) \rightarrow y$$

To accomplish this, a common practice is to predict the output $$y$$ from the last hidden state $$h_n$$ using the function $$g$$. Figure 2 shows an example of an RNN for text classification, such as sentiment analysis:

<figure>
<img src={require('/img/contextual_encoding/rnn-text-classification.png').default} alt="An example of an RNN and its application in sentiment analysis" width="563" />
<figcaption>Figure 2 - An example of an RNN and its application in sentiment analysis.</figcaption>
</figure>

:::warning
**Q7**: In **text classification** tasks, what specific information is captured by the final hidden state $$h_n$$ of a RNN?
:::

## Bidirectional RNN

The [RNN for sequence tagging](recurrent-neural-networks#rnn-for-sequence-tagging) above does not consider the words that follow the current word when predicting the output. This limitation can significantly impact model performance since contextual information following the current word can be crucial.

For example, let us consider the word "_early_" in the following two sentences:

* They are _early_ birds -> "_early_" is an adjective.
* They are _early_ today -> "_early_" is an adverb.

The POS tags of "_early_" depend on the following words, "_birds_" and "_today_", such that making the correct predictions becomes challenging without the following context.

To overcome this challenge, a **Bidirectional RNN** is suggested \[2] that considers both forward and backward directions, creating twice as many hidden states to capture a more comprehensive context. Figure 3 illustrates a bidirectional RNN for sequence tagging:

<figure>
<img src={require('/img/contextual_encoding/rnn-bidirectional.png').default} alt="An overview of a bidirectional RNN" width="375" />
<figcaption>Figure 3 - An overview of a bidirectional RNN.</figcaption>
</figure>

For every $$x_i$$, the hidden states $$\overrightarrow{h}_i$$ and $$\overleftarrow{h}_i$$ are created by considering $$\overrightarrow{h}_{i-1}$$ and $$\overleftarrow{h}_{i+1}$$, respectively. The function $$g$$ takes both $$\overrightarrow{h}_i$$ and $$\overleftarrow{h}_i$$ and returns an output $$y_i \in \mathbb{R}^{o \times 1}$$ such that $$g(\overrightarrow{h}_i, \overleftarrow{h}_i) = W^o (\overrightarrow{h}_i \oplus \overleftarrow{h}_i) = y_i$$, where $$(\overrightarrow{h}_i \oplus \overleftarrow{h}_i) \in \mathbb{R}^{2e \times 1}$$ is a concatenation of the two hidden states and $$W^o \in \mathbb{R}^{o \times 2e}$$.

:::warning
**Q8**: What are the advantages and limitations of implementing **bidirectional RNNs** for text classification and sequence tagging tasks?
:::

## Advanced Topics

* Long Short-Term Memory (LSTM) Networks \[3-5]
* Gated Recurrent Units (GRUs) \[6-7]

## References

1. [Finding Structure in Time](https://doi.org/10.1207/s15516709cog1402_1), Elman, Cognitive Science, 14(2), 1990.
2. [Bidirectional Recurrent Neural Networks](https://doi.org/10.1109/78.650093), Schuster and Paliwal, IEEE Transactions on Signal Processing, 45(11), 1997.
3. [Long Short-Term Memory](http://dx.doi.org/10.1162/neco.1997.9.8.1735), Hochreiter and Schmidhuber, Neural Computation, 9(8), 1997 ([PDF](https://www.researchgate.net/publication/13853244) available at ResearchGate).
4. [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://dx.doi.org/10.18653/v1/P16-1101), Ma and Hovy, ACL, 2016.
5. [Contextual String Embeddings for Sequence Labeling](https://aclanthology.org/C18-1139), Akbik et al., COLING, 2018.
6. [Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](http://dx.doi.org/10.3115/v1/D14-1179), Cho et al., EMNLP, 2014.
7. [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/abs/1412.3555), Chung et al., NeurIPS Workshop on Deep Learning and Representation Learning, 2014.
