---
title: Frequency Analysis
---

**Frequency Analysis** examines how often each word appears in a corpus. It helps understand language patterns and structure by measuring how often words appear in text.

## Word Counting

Consider the following text from Wikipedia about "Emory University" ([dat/emory-wiki.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/emory-wiki.txt)):

<details>

<summary>Emory University (as of 2023-10-18)</summary>

<div className="wrap-text">

```
Emory University is a private research university in Atlanta, Georgia. Founded in 1836 as Emory College by the Methodist Episcopal Church and named in honor of Methodist bishop John Emory.[18]

Emory University has nine academic divisions. Emory Healthcare is the largest healthcare system in the state of Georgia[19] and comprises seven major hospitals, including Emory University Hospital and Emory University Hospital Midtown.[20] The university operates the Winship Cancer Institute, Yerkes National Primate Research Center, and many disease and vaccine research centers.[21][22] Emory University is the leading coordinator of the U.S. Health Department's National Ebola Training and Education Center.[23] The university is one of four institutions involved in the NIAID's Tuberculosis Research Units Program.[24] The International Association of National Public Health Institutes is headquartered at the university.[25]

Emory University has the 15th-largest endowment among U.S. colleges and universities.[9] The university is classified among "R1: Doctoral Universities - Very high research activity"[26] and is cited for high scientific performance and citation impact in the CWTS Leiden Ranking.[27] The National Science Foundation ranked the university 36th among academic institutions in the United States for research and development (R&D) expenditures.[28][29] In 1995 Emory University was elected to the Association of American Universities, an association of the 65 leading research universities in the United States and Canada.[5]

Emory faculty and alumni include 2 Prime Ministers, 9 university presidents, 11 members of the United States Congress, 2 Nobel Peace Prize laureates, a Vice President of the United States, a United States Speaker of the House, and a United States Supreme Court Justice. Other notable alumni include 21 Rhodes Scholars and 6 Pulitzer Prize winners, as well as Emmy Award winners, MacArthur Fellows, CEOs of Fortune 500 companies, heads of state and other leaders in foreign government.[30] Emory has more than 149,000 alumni, with 75 alumni clubs established worldwide in 20 countries.[31][32][33]
```

</div>

</details>

Our task is to determine the number of word tokens and unique word types in this text.

:::warning
**Q1**: What is the difference between a **word token** and a **word type**?
:::

A simple way of accomplishing this task is to split the text by whitespace and count the resulting strings:

```python showLineNumbers
from collections import Counter

def count_words(corpus: str) -> Counter:
    fin = open(corpus)
    words = fin.read().split()
    return Counter(words)
```

* L1: Import the [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) class, a special type of a [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping), from the [collections](https://docs.python.org/3/library/collections.html) package.
* L3: Use [typing](https://docs.python.org/3/library/typing.html) to indicate the parameter type (`str`) and the return type (`Counter`).
* L4: [open()](https://docs.python.org/3/library/functions.html#open) the `corpus` file.
* L5: [read()](https://docs.python.org/3/library/io.html#io.TextIOBase.read) the contents of the file as a string, [split()](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split) it into a [list](https://docs.python.org/3/library/stdtypes.html#list) of words, and store them in `words`.
* L6: Count the occurrences of each word and return the results as a Counter.

```python showLineNumbers title="Run"
corpus = 'dat/emory-wiki.txt'
counts = count_words(corpus)

n_tokens = sum(counts.values())
n_types = len(counts)

print(f'# of word tokens: {n_tokens}')
print(f'# of word types: {n_types}')
```

* L1: The corpus can be found [dat/emory-wiki.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/emory-wiki.txt).
* L4: Save the total number of word tokens in the corpus, which is the [sum()](https://docs.python.org/3/library/functions.html#sum) of `counts` values.
* L5: Save the number of unique word types in the corpus, which is the [len()](https://docs.python.org/3/library/functions.html#len) of `counts`.
* L7-8: Print the value using the [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).


```text title="Output"
# of word tokens: 305
# of word types: 180
```

When running this program, you may encounter [FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError). To fix this error, follow these steps to set up your working directory:

1. Go to  `[Run] > [Edit Configurations]` in the menu.
2. Select "frequency\_analysis" from the sidebar.
3. Change the working directory to the top-level "nlp-essentials" directory.
4. Click `[OK]` to save the changes.

![Configure the working directory](/img/text_processing/pycharm3.png)


## Word Frequency

In this task, we aim to retrieve the top-_k_ most or least frequently occurring word types in the text:

```python showLineNumbers title="Run"
des = sorted(counts.items(), key=lambda x: x[1], reverse=True)
asc = sorted(counts.items(), key=lambda x: x[1])

for word, count in des[:10]: print(word, count)
for word, count in asc[:10]: print(word, count)
```

* L1: Sort words in `counts` in descending order and save them into `des` as a list of (word, count) [tuples](https://docs.python.org/3/library/stdtypes.html#tuples), sorted from the most frequent to the least frequent words ([sorted()](https://docs.python.org/3/library/functions.html#sorted), [items()](https://docs.python.org/3/library/stdtypes.html#dict.items), [lambda](https://docs.python.org/3/reference/expressions.html#lambda)).
* L2: Sort words in `counts` in ascending order and save them into `asc` as a list of (word, count) tuples.
* L4: Iterate over the top _k_ most frequent words in the sorted list using [slicing](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations), and print each word along with its count.
* L5: Iterate over the top _k_ least frequent words in the sorted list and print each word along with its count.


```text title="Output: Most Frequent"
the 18
and 15
of 12
Emory 11
in 10
University 7
is 7
university 6
United 6
research 5
```

```text title="Output: Least Frequent"
private 1
Atlanta, 1
Georgia. 1
Founded 1
1836 1
College 1
by 1
Episcopal 1
Church 1
named 1
```

Notice that the top-10 least-frequent word list contains unnormalized words such as "_Atlanta,_" (with the comma) and "_Georgia._" (with the period). This occurs because the text was split only by whitespaces without considering punctuation. Consequently, these words are recognized separately from the word types "_Atlanta_" and "_Georgia_". Therefore, the counts of word tokens and types processed above do not necessarily represent the distributions of the text accurately.

:::warning
**Q2**: How can we interpret the **most frequent** words in a text?
:::

## Save Output

Finally, let us save all word types in alphabetical order to a file:

```python showLineNumbers
def save_output(counts: Counter, outfile: str):
    fout = open(outfile, 'w')

    for word in sorted(counts.keys()):
        fout.write(f'{word}\n')

    fout.close()
```

* L2: Open `outfile` in [write](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) mode (`w`).
* L4: Iterate over unique word types (keys) of `counts` in alphabetical order.
* L5: Write each word followed by a newline character to `fout`.
* L7: Close the output stream.


```python showLineNumbers title="Run"
save_output(counts, 'dat/word_types.txt')
```

* L1: Creates the [dat/word\_types.txt](https://github.com/emory-courses/nlp-essentials/tree/main/dat/word_types.txt) file if it does not exist; otherwise, its previous contents will be completely overwritten.


## References

1. Source: [src/frequency\_analysis.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/frequency_analysis.py)
2. [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range), The Python Standard Library - Built-in Types
3. [Mapping Types](https://docs.python.org/3/library/stdtypes.html#typesmapping), The Python Standard Library - Built-in Types
4. [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html), The Python Tutorial
