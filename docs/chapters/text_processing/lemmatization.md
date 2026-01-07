---
title: Lemmatization
---

Sometimes, it is more appropriate to consider the canonical forms as tokens instead of their variations. For example, if you want to analyze the usage of the word "_transformer_" in NLP literature for each year, you want to count both "_transformer_" and '_transformers_' as a single item.

**Lemmatization** is a task that simplifies words into their base or dictionary forms, known as **lemmas**, to simplify the interpretation of their core meaning.

:::warning
**Q7**: What is the difference between a **lemmatizer** and a **stemmer** \[3]?
:::

When analyzing [dat/word\_types-token.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/word_types-token.txt) obtained by the tokenizer in the previous section, the following tokens are recognized as separate word types:

* _Universities_
* _University_
* _universities_
* _university_

Two variations are applied to the noun "_university_" - **capitalization**, generally used for proper nouns or initial words, and **pluralization**, which indicates multiple instances of the term. On the other hand, verbs can also take several variations regarding **tense** and **aspect**:

* _study_
* _studies_
* _studied_
* _studying_

We want to develop a lemmatizer that normalizes all variations into their respective lemmas.

## Lemma Lexica

Let us create lexica for lemmatization:

```python showLineNumbers
import json
import os
from types import SimpleNamespace
```

* L1: [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* L2: [Common pathname manipulations](https://docs.python.org/3/library/os.path.html#module-os.path)
* L3: [SimpleNamespace](https://docs.python.org/es/3.5/library/types.html#types.SimpleNamespace)

```python showLineNumbers
def get_lexica(res_dir: str) -> SimpleNamespace:
    with open(os.path.join(res_dir, 'nouns.txt')) as fin: nouns = {noun.strip() for noun in fin}
    with open(os.path.join(res_dir, 'verbs.txt')) as fin: verbs = {verb.strip() for verb in fin}
    with open(os.path.join(res_dir, 'nouns_irregular.json')) as fin: nouns_irregular = json.load(fin)
    with open(os.path.join(res_dir, 'verbs_irregular.json')) as fin: verbs_irregular = json.load(fin)
    with open(os.path.join(res_dir, 'nouns_rules.json')) as fin: nouns_rules = json.load(fin)
    with open(os.path.join(res_dir, 'verbs_rules.json')) as fin: verbs_rules = json.load(fin)

    return SimpleNamespace(
        nouns=nouns,
        verbs=verbs,
        nouns_irregular=nouns_irregular,
        verbs_irregular=verbs_irregular,
        nouns_rules=nouns_rules,
        verbs_rules=verbs_rules
    )
```

* L1: `res_dir`: the path to the root directory where all lexica files are located.
* L2: [nouns.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/nouns.txt): a list of base nouns
* L3: [verbs.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/verbs.txt): a list of base verbs
* L4: [nouns\_irregular.json](https://github.com/emory-courses/nlp-essentials/blob/main/dat/nouns_irregular.json): a dictionary of nouns whose plural forms are irregular (e.g., _mouse_ → _mice_)
* L5: [verbs\_irregular.json](https://github.com/emory-courses/nlp-essentials/blob/main/dat/verbs_irregular.json): a dictionary of verbs whose inflection forms are irregular (e.g., _buy_ → _bought_)
* L6: [nouns\_rules.json](https://github.com/emory-courses/nlp-essentials/blob/main/dat/nouns_rules.json): a list of pluralization rules for nouns
* L7: [verbs\_rules.json](https://github.com/emory-courses/nlp-essentials/blob/main/dat/verbs_rules.json): a list of inflection rules for verbs

We then verify that all lexical resources are loaded correctly:

```python showLineNumbers title="Run"
print(len(lexica.nouns))
print(len(lexica.verbs))
print(lexica.nouns_irregular)
print(lexica.verbs_irregular)
print(lexica.nouns_rules)
print(lexica.verbs_rules)
```

```text title="Output"
91
27
{'children': 'child', 'crises': 'crisis', 'mice': 'mouse'}
{'is': 'be', 'was': 'be', 'has': 'have', 'had': 'have', 'bought': 'buy'}
[['ies', 'y'], ['es', ''], ['s', ''], ['men', 'man'], ['ae', 'a'], ['i', 'us']]
[['ies', 'y'], ['ied', 'y'], ['es', ''], ['ed', ''], ['s', ''], ['d', ''], ['ying', 'ie'], ['ing', ''], ['ing', 'e'], ['n', ''], ['ung', 'ing']]
```

:::warning
**Q8**: What are the key differences between **inflectional** and **derivational** morphology?
:::

## Lemmatizing

Let us write the `lemmatize()` function that takes a word and lemmatizes it using the lexica:

```python showLineNumbers
def lemmatize(lexica: SimpleNamespace, word: str) -> str:
    def aux(word: str, vocabs: dict[str, str], irregular: dict[str, str], rules: list[tuple[str, str]]):
        lemma = irregular.get(word, None)
        if lemma is not None: return lemma

        for p, s in rules:
            lemma = word[:-len(p)] + s
            if lemma in vocabs: return lemma

        return None

    word = word.lower()
    lemma = aux(word, lexica.verbs, lexica.verbs_irregular, lexica.verbs_rules)

    if lemma is None:
        lemma = aux(word, lexica.nouns, lexica.nouns_irregular, lexica.nouns_rules)

    return lemma if lemma else word
```

* L2: Define a nested function `aux` to handle lemmatization.
* L3-4: Check if the word is in the irregular dictionary ([get()](https://docs.python.org/3/library/stdtypes.html#dict.get)), if so, return its lemma.
* L6-7: Try applying each rule in the `rules` list to `word`.
* L8: If the resulting lemma is in the vocabulary, return it.
* L10: If no lemma is found, return `None`.
* L12: Convert the input word to lowercase for case-insensitive processing.
* L13: Try to lemmatize the word using verb-related lexica.
* L15-16: If no lemma is found among verbs, try to lemmatize using noun-related lexica.
* L18: Return the lemma if found or the decapitalized word if no lemmatization occurred.

We now test our lemmatizer for nouns and verbs:

```python showLineNumbers title="Run"
nouns = ['studies', 'crosses', 'areas', 'gentlemen', 'vertebrae', 'alumni', 'children', 'crises']
nouns_lemmatized = [lemmatize(lexica, word) for word in nouns]
for word, lemma in zip(nouns, nouns_lemmatized): print('{} -> {}'.format(word, lemma))

verbs = ['applies', 'cried', 'pushes', 'entered', 'takes', 'heard', 'lying', 'studying', 'taking', 'drawn', 'clung', 'was', 'bought']
verbs_lemmatized = [lemmatize(lexica, word) for word in verbs]
for word, lemma in zip(verbs, verbs_lemmatized): print('{} -> {}'.format(word, lemma))
```

```text title="Output: Nouns"
studies -> study
crosses -> cross
areas -> area
gentlemen -> gentleman
vertebrae -> vertebra
alumni -> alumnus
children -> child
crises -> crisis
```

```text title="Output: Verbs"
applies -> apply
cried -> cry
pushes -> push
entered -> enter
takes -> take
heard -> hear
lying -> lie
studying -> study
taking -> take
drawn -> draw
clung -> cling
was -> be
bought -> buy
```

Finally, let us recount word types in [dat/emory-wiki.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/emory-wiki.txt) using the lemmatizer and save them to [dat/word\_types-token-lemma.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/word_types-token-lemma.txt):

```python showLineNumbers title="Run"
from collections import Counter
from src.tokenization import tokenize

corpus = 'dat/emory-wiki.txt'
delims = {'"', "'", '(', ')', '[', ']', ':', '-', ',', '.'}
words = [lemmatize(lexica, word) for word in tokenize(corpus, delims)]
counts = Counter(words)

print(f'# of word tokens: {len(words)}')
print(f'# of word types: {len(counts)}')

output = 'dat/word_types-token-lemma.txt'
with open(output, 'w') as fout:
    for key in sorted(counts.keys()): fout.write(f'{key}\n')
```

* L2: Import the `tokenize()` function from the [src/tokenization.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/tokenization.py) module.


```text title="Output"
# of word tokens: 363
# of word types: 177
```

* [dat/text\_processing /word\_types-token-lemma.txt](https://github.com/emory-courses/nlp-essentials/blob/main/dat/text_processing/word_types-token-lemma.txt)

When the words are further normalized by lemmatization, the number of word tokens remains the same as without lemmatization, but the number of word types is reduced from 197 to 177.

:::warning
**Q9**: In which tasks can **lemmatization** negatively impact performance?
:::

## References

1. Source: [lemmatization.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/lemmatization.py)
2. [ELIT Morphological Analyzer](https://github.com/emorynlp/elit-morph_analyzer) - A heuristic-based lemmatizer
3. [An Algorithm for Suffix Stripping](https://doi.org/10.1108/eb046814), Porter, Program: Electronic Library and Information Systems, 14(3), 1980 ([PDF](https://www.emerald.com/insight/content/doi/10.1108/00330330610681286/full/pdf))
