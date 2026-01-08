---
title: Entropy and Perplexity
---

# Entropy and Perplexity

## Entropy

**Entropy** is a measure of the uncertainty, randomness, or information content of a random variable or a probability distribution. The entropy of a random variable $$X = \lbrace x_1, \ldots, x_n \rbrace$$ is defined as:

$$
H(X) = \sum_{i=1}^n P(x_i) \cdot (-\log P(x_i)) = -\sum_{i=1}^n P(x_i) \cdot \log P(x_i)
$$

$$P(x_i)$$ is the probability distribution of $$x_i$$. The self-information of $$x_i$$ is defined as $$-\log P(x)$$, which measures how much information is gained when $$x_i$$ occurs. The negative sign indicates that as the occurrence of $$x_i$$ increases, its self-information value decreases.

Entropy has several properties, including:

* It is non-negative: $$H(X) \geq 0$$.
* It is at its minimum when $$x_i$$ is entirely predictable (all probability mass on a single outcome).
* It is at its maximum when all outcomes of $$x_i$$ are equally likely.

:::warning
**Q10**: Why is logarithmic scale used to measure **self-information** in entropy calculations?
:::

## Sequence Entropy

**Sequence entropy** is a measure of the unpredictability or information content of the sequence, which quantifies how uncertain or random a word sequence is.

Assume a long sequence of words, $$W = [w_1, \ldots, w_n]$$, concatenating the entire text from a language $$\mathcal{L}$$. Let $$\mathcal{S} = \lbrace S_1, \ldots, S_m \rbrace$$ be a set of all possible sequences derived from $$W$$, where $$S_1$$ is the shortest sequence (a single word) and $$S_m = W$$ is the longest sequence. Then, the entropy of $$W$$ can be measured as follows:

$$
H(W) = -\sum_{j=1}^m P(S_j) \cdot \log P(S_j)
$$

The **entropy rate** (per-word entropy), $$H'(W)$$, can be measured by dividing $$H(W)$$ by the total number of words $$n$$:

$$
H'(W) = -\frac{1}{n} \sum_{j=1}^m P(S_j) \cdot \log P(S_j)
$$

In theory, there is an infinite number of unobserved word sequences in the language $$\mathcal{L}$$. To estimate the true entropy of $$\mathcal{L}$$, we need to take the limit to $$H'(W)$$ as $$n$$ approaches infinity:

$$
H(\mathcal{L}) = \lim_{n \rightarrow \infty} H'(W) = \lim_{n \rightarrow \infty} -\frac{1}{n} \sum_{j=1}^m P(S_j) \cdot \log P(S_j)
$$

The [Shannon-McMillan-Breiman theorem](https://www.sciencedirect.com/science/article/pii/088523089190016J?via=ihub) implies that if the language is both stationary and ergodic, considering a single sequence that is sufficiently long can be as effective as summing over all possible sequences to measure $$H(\mathcal{L})$$ because a long sequence of words naturally contains numerous shorter sequences, and each of these shorter sequences reoccurs within the longer sequence according to their respective probabilities.

:::info
☝️ The [bigram model](n-gram-models.md) in the previous section is **stationary** because all probabilities rely on the same condition, $$P(w_{i+1}, w_i)$$. In reality, however, this assumption does not hold. The probability of a word's occurrence often depends on a range of other words in the context, and this contextual influence can vary significantly from one word to another.
:::

By applying this theorem, $$H(\mathcal{L})$$ can be approximated:

$$
H(\mathcal{L}) \approx \lim_{n \rightarrow \infty} -\frac{1}{n} \log P(S_m)
$$

Consequently, $$H'(W)$$ is approximated as follows, where $$S_m = W$$:

$$
H'(W) \approx -\frac{1}{n} \log P(W)
$$

:::warning
**Q11**: What indicates **high entropy** in a text corpus?
:::

## Perplexity

**Perplexity** measures how well a language model can predict a set of words based on the likelihood of those words occurring in a given text. The perplexity of a word sequence $$W$$ is measured as:

$$
PP(W) = P(W)^{-\frac{1}{n}} = \sqrt[n]{\frac{1}{P(W)}}
$$

Hence, the higher $$P(W)$$ is, the lower its perplexity becomes, implying that the language model is "less perplexed" and more confident in generating $$W$$.

Perplexity, $$PP(W)$$, can be directly derived from the approximated entropy rate, $$H'(W)$$:

$$
\begin{array}{rcl}
H'(W) &\approx & -\frac{1}{n} \log_2 P(W) \\[5pt]
2^{H'(W)} &\approx & 2^{-\frac{1}{n} \log_2 P(W)} \\[5pt]
 &= & 2^{\log_2 P(W)^{-\frac{1}{n}}} \\[5pt]
 &= & P(W)^{-\frac{1}{n}} \\[5pt]
 &= & PP(W)
\end{array}
$$

:::warning
**Q12**: What is the relationship between **corpus entropy** and **language model perplexity**?
:::

## References

1. [Entropy](https://en.wikipedia.org/wiki/Entropy_\(information_theory\)), Wikipedia
2. [Perplexity](https://en.wikipedia.org/wiki/Perplexity), Wikipedia
