---
title: Encoder-Decoder Framework
---

# Encoder-Decoder Framework

The **Encoder-Decoder Framework** is commonly used for solving sequence-to-sequence tasks, where it takes an input sequence, processes it through an encoder, and produces an output sequence. This framework consists of three main components: an [encoder](encoder-decoder-framework#encoder), a context vector, and a [decoder](encoder-decoder-framework#decoder), as illustrated in Figure 1:

<figure>
<img src={require('/img/contextual_encoding/encoder-decoder-framework.png').default} alt="An overview of an encoder-decoder framework" width="563" />
<figcaption>Figure 1 - An overview of an encoder-decoder framework.</figcaption>
</figure>

## Encoder

An **encoder** processes an input sequence and creates a **context vector** that captures context from the entire sequence and serves as a summary of the input.

Let $$X =[x_1, \ldots, x_n,x_c]$$ be an input sequence, where $$x_i \in \mathbb{R}^{d \times 1}$$ is the $$i$$'th word in the sequence and $$x_c$$ is an artificial token appended to indicate the end of the sequence. The encoder utilizes two functions, $$f$$ and $$g$$, which are defined in the same way as in the [RNN for text classification](recurrent-neural-networks#rnn-for-text-classification). Notice that the _end-of-sequence_ token $$x_c$$ is used to create an additional hidden state $$h_c$$, which in turn creates the context vector $$y_c$$.

Figure 2 shows an encoder example that takes the input sequence, "_I am a boy_", appended with the _end-of-sequence_ token "\[EOS]":

<figure>
<img src={require('/img/contextual_encoding/encoder.png').default} alt="An encoder example" width="375" />
<figcaption>Figure 2 - An encoder example.</figcaption>
</figure>

:::warning
**Q15**: Is it possible to derive the **context vector** from $$x_n$$ instead of $$x_c$$? What is the purpose of appending an extra token to indicate the end of the sequence?
:::

## Decoder

A **decoder** is conditioned on the context vector, which allows it to generate an output sequence contextually relevant to the input, often one token at a time.

Let $$Y = [y_1, \ldots, y_m, y_{t}]$$ be an output sequence, where $$y_i \in \mathbb{R}^{o \times 1}$$ is the $$i$$'th word in the sequence, and $$y_t$$ is an artificial token to indicate the end of the sequence. To generate the output sequence, the decoder defines two functions, $$f$$ and $$g$$:

* $$f$$ takes the previous output $$y_{i-1}$$ and its hidden state $$s_{i-1}$$, and returns a hidden state $$s_{i} \in \mathbb{R}^{e \times 1}$$ such that $$f(y_{i-1}, s_{i-1}) = \alpha(W^y y_{i-1}​ + W^s s_ {i−1}) = s_i$$, where $$W^y \in \mathbb{R}^{e \times o}$$, $$W^s \in \mathbb{R}^{e \times e}$$, and $$\alpha$$ is an activation function.
* $$g$$ takes the hidden state $$s_i$$ and returns an output $$y_{i} \in \mathbb{R}^{o \times 1}$$ such that $$g(s_i) = W^o s_i = y_{i}$$, where $$W^o \in \mathbb{R}^{o \times e}$$.

Note that the initial hidden state $$s_1$$ is created by considering only the context vector $$y_c$$ such that the first output $$y_1$$ is solely predicted by the context in the input sequence. However, the prediction of every subsequent output $$y_{i}$$ is conditioned on both the previous output $$y_{i-1}$$ and its hidden state $$s_{i-1}$$. Finally, the decoder stops generating output when it predicts the _end-of-sequence_ token $$y_t$$.

:::info
In some variations of the decoder, the initial hidden state $$s_1$$ is created by considering both $$y_c$$ and $$h_c$$ \[1].
:::

Figure 3 illustrates a decoder example that takes the context vector $$y_0$$ and generates the output sequence, "나(I) +는(SBJ) 소년(boy) +이다(am)", terminated by the _end-of-sequence_ token "\[EOS]", which translates the input sequence from English to Korean:

<figure>
<img src={require('/img/contextual_encoding/decoder.png').default} alt="A decoder example" width="375" />
<figcaption>Figure 3 - A decoder example.</figcaption>
</figure>

:::warning
**Q16**: The decoder mentioned above does not guarantee the generation of the **end-of-sequence token** at any step. What potential issues can arise from this?
:::

The likelihood of the current output $$y_i$$ can be calculated as:

$$
P(y_{i} | \{y_c\} \cup \{y_1, \ldots, y_{i-1}\}) = q(y_c, y_{i-1}, s_{i-1})
$$

where $$q$$ is a function that takes the context vector $$y_c$$, previous input $$y_{i-1}$$ and its hidden state $$s_{i-1}$$, and returns the probability of $$y_i$$. Then, the [maximum likelihood](/chapters/language_models/maximum-likelihood-estimation) of the output sequence can be estimated as follows ($$y_0 = s_0 = \mathbf{0}$$):

$$
P(Y) = \prod_{i=1}^{m+1} q(y_c, y_{i-1}, s_{i-1})
$$

## References

1. [Sequence to Sequence Learning with Neural Networks](https://papers.nips.cc/paper_files/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html), Sutskever et al., NeurIPS, 2014.
2. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473), Bahdanau et al., ICLR, 2015.
