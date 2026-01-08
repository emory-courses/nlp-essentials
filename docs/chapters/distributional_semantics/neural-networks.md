---
title: Neural Networks
---

# Neural Networks

## Logistic Regression

Let $$\mathrm{x} = [x_1, \ldots, x_n]$$ be a vector representing an input instance, where $$x_i$$ denotes the $$i$$'th feature of the input and $$y \in \lbrace 0, 1 \rbrace$$ be its corresponding output label. **Logistic regression** uses the **logistic function**, aka. the **sigmoid function**, to estimate the probability that $$\mathrm{x}$$ belongs to $$y$$:&#x20;

$$
\begin{align*}
P(y=1|\mathrm{x}) &= \frac{1}{1 + e^{-(\mathrm{x}\cdot\mathrm{w}^T+b)}}\\
P(y=0|\mathrm{x}) &= 1 - P(y=1|\mathrm{x})
\end{align*}
$$

The weight vector $$\mathrm{w}=[w_1, \ldots, w_n]$$ assigns weights to each dimension of the input vector $$\mathrm{x}$$ for the label $$y=1$$ such that a higher magnitude of weight $$w_i$$ indicates greater importance of the feature $$x_i$$. Finally, $$b$$ represents the bias of the label $$y=1$$ within the training distribution.

:::warning
**Q7**: What role does the **sigmoid function** play in the logistic regression model?
:::

Consider a corpus consisting of two sentences:

> D1: I love this movie
>
> D2: I hate this movie

The input vectors $$\mathrm{x}_1$$ and $$\mathrm{x}_2$$ can be created for these two sentences using the [bag-of-words model](../vector-space-models/bag-of-words-model.md):

```python
V = {0: "I", 1: "love", 2: "hate", 3: "this", 4: "movie"}
x1 = [1, 1, 0, 1, 1]
x2 = [1, 0, 1, 1, 1]
```

Let $$y_1 =1$$ and $$y_2 = 0$$ be the output labels of $$\mathrm{x}_1$$and $$\mathrm{x}_2$$, representing postive and negative sentiments of the input sentences, respectively. Then, a weight vector $$\mathrm{w}$$ can be trained using logistic regression:

```python
w = [0.0, 1.5, -1.5, 0.0, 0.0]
b = 0
```

Since the terms "_I_", "_this_", and "_movie_" appear with equal frequency across both labels, their weights $$w_1​$$, $$w_4​$$, and $$w_5​$$ are neutralized. On the other hand, the terms "_love_" and "_hate_" appear only with the positive and negative labels, respectively. Therefore, while the weight $$w_1​$$ for "_love_" ($$x_1​$$) contributes positively to the label $$y=1$$, the weight $$w_2$$ for "_hate_" ($$x_2​$$) has a negative impact on the label $$y=1$$. Furthermore, as positive and negative sentiment labels are equally presented in this corpus, the bias $$b$$ is also set to 0.

Given the weight vector and the bias, we have $$\mathrm{x}_1 \cdot \mathrm{w}^T + b = 1.5$$ and $$\mathrm{x}_2 \cdot \mathrm{w}^T + b = -1.5$$, resulting the following probabilities:

$$
\begin{align*}
P(y=1|\mathrm{x}_1) \approx 0.82\\
P(y=1|\mathrm{x}_2) \approx 0.18
\end{align*}
$$

As the probability of $$x_1​$$ being $$y=1$$ exceeds $$0.5$$ (50%), the model predicts the first sentence to convey a positive sentiment. Conversely, the model predicts the second sentence to convey a negative sentiment as its probability of being $$y=1$$ is below 50%.

:::warning
**Q8**: Under what circumstances would the **bias** $$b$$ be negative in the above example? Additionally, when might neutral terms such as "_this_" or "_movie_" exhibit non-neutral weights?
:::

## Softmax Regression

**Softmax regression**, aka. multinomial logistic regression, is an extension of logistic regression to handle classification problems with more than two classes. Given an input vector $$\mathrm{x} \in \mathbb{R}^{1 \times n}$$ and its output lable $$y \in \lbrace 0, \ldots, m-1 \rbrace$$, the model uses the **softmax function** to estimates the probability that $$\mathrm{x}$$ belongs to each class separately:&#x20;

$$
P(y=k|\mathrm{x}) = \frac{e^{\mathrm{x}\cdot\mathrm{w}_k^T+b_k}}{\sum_{j=1}^m e^{\mathrm{x}\cdot\mathrm{w}_j^T+b_j}}
$$

The weight vector $$\mathrm{w}_k​$$ assigns weights to $$\mathrm{x}$$ for the label $$y=k$$, while $$b_k​$$ represents the bias associated with the label $$y=k$$.

:::warning
**Q9**: What is the role of the **softmax function** in the softmax regression model? How does it differ from the sigmoid function?
:::

Consider a corpus consisting of three sentences:

> D1: I love this movie
>
> D2: I hate this movie
>
> D3: I watched this movie

Then, the input vectors $$\mathrm{x}_1$$, $$\mathrm{x}_2$$, and $$\mathrm{x}_3$$ for the sentences can be created using the [bag-of-words model](../vector-space-models/bag-of-words-model.md):

```python
V = {0: "I", 1: "love", 2: "hate", 3: "this", 4: "movie", 5: "watched"}
x1 = [1, 1, 0, 1, 1, 0]
x2 = [1, 0, 1, 1, 1, 0]
x3 = [1, 0, 0, 1, 1, 1]
```

Let $$y_1 =1$$, $$y_2 = 0$$, and $$y=2$$ be the output labels of $$\mathrm{x}_1$$, $$\mathrm{x}_2$$, and $$\mathrm{x}_3$$, representing postive, negative, and neutral sentiments of the input sentences, respectively. Then, weight vectors $$\mathrm{w}_1$$, $$\mathrm{w}_2$$, and $$\mathrm{w}_3$$ can be trained using softmax regression as follows:

```python
w1 = [0.0,  1.5, -1.0, 0.0, 0.0, 0.0]
w2 = [0.0, -1.0,  1.5, 0.0, 0.0, 0.0]
w3 = [0.0, -1.0, -1.0, 0.0, 0.0, 1.5]
b1 = b2 = b3 = 0
```

Unlike the case of logistic regression where all weights are oriented to $$y = 1$$ (both $$w_1$$ and $$w_2$$ giving positive and negative weights to $$y = 1$$ respectively, but not $$y=0$$), the values in each weigh vector are oriented to each corresponding label.

Given the weight vectors and the biases, we can estimate the following probabilities for $$\mathrm{x}_1$$:

$$
\begin{align*}
\mathrm{x}_1 \cdot \mathrm{w}_1^T + b_1 &=& 1.5  &\Rightarrow & P(y=1|\mathrm{x}_1) &=& 0.86\\
\mathrm{x}_1 \cdot \mathrm{w}_2^T + b_2 &=& -1.0 &\Rightarrow & P(y=0|\mathrm{x}_1) &=& 0.07\\
\mathrm{x}_1 \cdot \mathrm{w}_3^T + b_3 &=& -1.0 &\Rightarrow & P(y=2|\mathrm{x}_1) &=& 0.07
\end{align*}
$$

Since the probabiilty of $$y=1$$ is the highest among all labels, the model predicts the first sentence to convey a positive sentiment. For $$\mathrm{x}_3$$, the following probabilities can be estimated:

$$
\begin{align*}
\mathrm{x}_3 \cdot \mathrm{w}_1^T + b_1 &=& 0  &\Rightarrow & P(y=1|\mathrm{x}_3) &=& 0.14\\
\mathrm{x}_3 \cdot \mathrm{w}_2^T + b_2 &=& 0 &\Rightarrow & P(y=0|\mathrm{x}_3) &=& 0.14\\
\mathrm{x}_3 \cdot \mathrm{w}_3^T + b_3 &=& 1.5 &\Rightarrow & P(y=2|\mathrm{x}_3) &=& 0.69
\end{align*}
$$

Since the probabiilty of $$y=2$$ is the highest among all labels, the model predicts the first sentence to convey a neutral sentiment.

Softmax regression always predicts $$m$$ values so that it is represented by an output vector $$\mathrm{y} \in \mathbb{R}^{1 \times m}$$, wherein the $$i$$'th value in $$\mathrm{y}$$ contains the probability of the input belonging to the $$i$$'th class. Similarly, the weight vectors for all labels can be stacked into a weight matrix $$\mathrm{W} \in \mathbb{R}^{m \times n}$$, where the $$i$$'th row represents the weight vector for the $$i$$'th label.

With this new formulation, softmax regression can be defined as $$\mathrm{y} = \mathrm{softmax}(\mathrm{x} \cdot \mathrm{W}^T)$$, and the optimal prediction can be achieved as $$\mathrm{argmax}(\mathrm{y})$$, which returns a set of labels with the highest probabilities.

:::info
What are the limitations of the softmax regression model?
:::

## Multilayer Perceptron

A **multilayer perceptron** (MLP) is a type of [Feedforward Neural Networks](https://en.wikipedia.org/wiki/Feedforward_neural_network) consisting of multiple layers of neurons, where all neurons from one layer are fully connected to all neurons in its adjecent layers. Given an input vector $$\mathrm{x} \in \mathbb{R}^{1 \times n}$$ and an output vector $$\mathrm{y} \in \mathbb{R}^{1 \times m}$$, the model allows zero to many hidden layers to generate intermediate representations of the input.

Let $$\mathrm{h} \in \mathbb{R}^{1 \times d}$$ be a hidden layer between $$\mathrm{x}$$ and $$\mathrm{y}$$. To connect $$\mathrm{x}$$ and $$\mathrm{h}$$, we need a weight matrix $$\mathrm{W}_x \in \mathbb{R}^{n \times d}$$ such that $$\mathrm{h} = \mathrm{activation}(\mathrm{x} \cdot \mathrm{W}_x)$$, where $$\mathrm{activation}()$$ is an **activation function** applied to the output of each neuron; it introduces non-linearity into the network, allowing it to learn complex patterns and relationships in the data. [Activation functions](https://en.wikipedia.org/wiki/Activation_function) determine whether a neuron should be activated or not, implying whether or not the neuron's output should be passed on to the next layer.

$$
\mathrm{h} = \mathrm{activation}(\mathrm{x} \cdot \mathrm{W}_x)
$$

Similarly, to connect $$\mathrm{h}$$ and $$\mathrm{y}$$, we need a weight matrix $$\mathrm{W}_h \in \mathbb{R}^{m \times d}$$ such that $$\mathrm{y} = \mathrm{softmax}(\mathrm{h} \cdot \mathrm{W}_h^T)$$. Thus, a multilayer perceptron with one hidden layer can be represented as:

$$
\mathrm{y} = \mathrm{softmax}[\mathrm{activation}(\mathrm{x} \cdot \mathrm{W}_x) \cdot \mathrm{W}_h^T] = \mathrm{softmax}(\mathrm{h} \cdot \mathrm{W}_h^T)
$$

<figure>
<img src={require('/img/distributional_semantics/neural-layers.png').default} alt="Types of decision regions that can be formed by different layers of MLP" />
<figcaption>Types of decision regions that can be formed by different layers of MLP [1]</figcaption>
</figure>

:::warning
**Q10**: Notice that the above equation for MLP does not include bias terms. How are **biases** handled in light of this formulation?
:::

Consider a corpus comprising the following five sentences the corresponding labels ($$\Rightarrow$$):

> D1: I love this movie $$\Rightarrow$$ postive
>
> D2: I hate this movie $$\Rightarrow$$ negative
>
> D3: I watched this movie $$\Rightarrow$$ neutral
>
> D4: I truly love this movie $$\Rightarrow$$ very positive
>
> D5: I truly hate this movie $$\Rightarrow$$ very negative

The input vectors $$\mathrm{x}_{1..5}$$ can be created using the [bag-of-words model](../vector-space-models/bag-of-words-model.md):

```python
X = {0: "I", 1: "love", 2: "hate", 3: "this", 4: "movie", 5: "watched", 6: "truly"}
Y = {0: "positive", 1: "negative", 2: "neutral", 3: "very positive", 4: "very negative"}

x1 = [1, 1, 0, 1, 1, 0, 0]
x2 = [1, 0, 1, 1, 1, 0, 0]
x3 = [1, 0, 0, 1, 1, 1, 0]
x4 = [1, 1, 0, 1, 1, 0, 1]
x5 = [1, 0, 1, 1, 1, 0, 1]

y1, y2, y3, y4, y5 = 0, 1, 2, 3, 4
```

:::warning
**Q11**: What would be the weight assigned to the **feature "**_**truly**_**"** learned by softmax regression for the above example?
:::

The first weight matrix $$\mathrm{W}_x \in \mathbb{R}^{7 \times 5}$$ can be trained by an MLP as follows:

```python
Wx = [
  [0.0, 0.0, 0.0, 0.0, 0.0],
  [1.0, 0.0, 0.0, 0.5, 0.0],
  [0.0, 1.0, 0.0, 0.0, 0.5],
  [0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 0.0, 1.0, 0.0, 0.0],
  [0.0, 0.0, 0.0, 0.5, 0.5]
]
```

Given the values in $$\mathrm{W}_x$$, we can infer that the first, second, and third columns represent "_love_", '_hate_", and "_watch_", while the fourth and fifth columns learn combined features such as {"_truly_", "_love_"} and {"_truly_", "_hate_"}, respectively.

Each of $$\mathrm{x}_{1..5}$$ is multiplied by $$\mathrm{W}_x$$ to achieve the hiddner layer $$\mathrm{h}_{1..5}$$, respectively, where the activation function is designed as follow:

$$
\mathrm{activation}(x) = \left\{
\begin{array}{ll}
  x & \text{if}\: x > 0.5\\
  0 & \text{otherwise}
\end{array}
\right.
$$

```python title="Before Activation"
g1 = [1.0, 0.0, 0.0, 0.5, 0.0]
g2 = [0.0, 1.0, 0.0, 0.0, 0.5]
g3 = [0.0, 0.0, 1.0, 0.0, 0.0]
g4 = [1.0, 0.0, 0.0, 1.0, 0.5]
g5 = [0.0, 1.0, 0.0, 0.5, 1.0]
```

```python title="After Activation"
h1 = activation(g1) = [1.0, 0.0, 0.0, 0.0, 0.0]
h2 = activation(g2) = [0.0, 1.0, 0.0, 0.0, 0.0]
h3 = activation(g3) = [0.0, 0.0, 1.0, 0.0, 0.0]
h4 = activation(g4) = [1.0, 0.0, 0.0, 1.0, 0.0]
h5 = activation(g5) = [0.0, 1.0, 0.0, 0.0, 1.0]
```

The second weight matrix $$\mathrm{W}_h \in \mathbb{R}^{5 \times 5}$$ can also be trained by an MLP as follows:

```python
Wh = [
  [ 1.0, -1.0, 0.0, -0.5, -1.0],
  [-1.0,  1.0, 0.0, -1.0, -0.5],
  [-1.0, -1.0, 1.0, -1.0, -1.0],
  [ 0.0, -1.0, 0.0,  1.0, -1.0],
  [-1.0,  0.0, 0.0, -1.0,  1.0]
]
```

By applying the softmax function to each $$\mathrm{h}_i \cdot \mathrm{W}^T_h$$, we achieve the corresponding output vector $$\mathrm{y}_i$$:

```python title="Before Softmax"
o1 = [ 1.0, -1.0, -1.0,  0.0, -1.0]
o2 = [-1.0,  1.0, -1.0, -1.0,  0.0]
o3 = [ 0.0,  0.0,  1.0,  0.0,  0.0]
o4 = [ 0.5, -2.0, -2.0,  1.0, -2.0]
o5 = [-2.0,  0.5, -2.0, -2.0,  1.0]
```

```python title="After Softmax"
y1 = softmax(o1) = [0.56, 0.08, 0.08, 0.21, 0.08]
y2 = softmax(o2) = [0.08, 0.56, 0.08, 0.08, 0.21]
y3 = softmax(o3) = [0.15, 0.15, 0.40, 0.15, 0.15]
y4 = softmax(o4) = [0.35, 0.03, 0.03, 0.57, 0.03]
y5 = softmax(o5) = [0.03, 0.35, 0.03, 0.03, 0.57]
```

The prediction can be made by taking the argmax of each $$\mathrm{y}_i$$.

:::warning
**Q12**: What are the limitations of a **multilayer perceptron**?
:::

## References

1. [Neural Network Methodologies and their Potential Application to Cloud Pattern Recognition](https://www.google.com/url?sa=t\&source=web\&rct=j\&opi=89978449\&url=https://apps.dtic.mil/sti/tr/pdf/ADA239214.pdf\&ved=2ahUKEwjM1eCt9pSFAxVEw8kDHfkxDYsQFnoECA8QAQ\&usg=AOvVaw1gpvevcnMSAIEFzg0D8CAX), J. E. Peak, Defense Technical Information Center, ADA239214, 1991.
