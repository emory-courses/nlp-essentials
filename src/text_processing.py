# ========================================================================
# Copyright 2023 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================

__author__ = 'Jinho D. Choi'

from collections import Counter


def top_k_words(word_counts: Counter[str, int], k: int, top=True):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=top)[:k]


def delimit(token: str, delimiters: set[str]) -> list[str]:
    i = next((i for i, c in enumerate(token) if c in delimiters), -1)
    if i < 0: return [token]
    tokens = []

    if i > 0: tokens.append(token[:i])
    tokens.append(token[i])
    if i + 1 < len(token): tokens.extend(delimit(token[i + 1:], delimiters))
    return tokens


def postprocess(tokens: list[str]) -> list[str]:
    i, new_tokens = 0, []
    while i < len(tokens):
        # apostrophe: 's
        if i + 1 < len(tokens) and tokens[i] == "'" and tokens[i + 1].lower() == 's':
            new_tokens.append(''.join(tokens[i:i + 2]))
            i += 1
        # numbers: [##], ###,###
        elif i + 2 < len(tokens) and \
                ((tokens[i] == '[' and tokens[i + 1].isnumeric() and tokens[i + 2] == ']') or \
                 (tokens[i].isnumeric() and tokens[i + 1] == ',' and tokens[i + 2].isnumeric())):
            new_tokens.append(''.join(tokens[i:i + 3]))
            i += 2
        # acronyms: U.S.
        elif i + 3 < len(tokens) and ''.join(tokens[i:i + 4]) == 'U.S.':
            new_tokens.append(''.join(tokens[i:i + 4]))
            i += 3
        else:
            new_tokens.append(tokens[i])
        i += 1
    return new_tokens


def noun_lemma(word: str, singular_nouns: set[str], irregular_nouns: dict[str, str], plural_rules: dict[str, str]):
    # decapitalize
    word = word.lower()

    # irregular nouns
    lemma = irregular_nouns.get(word, None)
    if lemma is not None: return lemma

    # singularize
    for p, s in plural_rules.items():
        lemma = word[:-len(p)] + s
        if lemma in singular_nouns: return lemma

    return word


def tokenize(corpus: str, delimiters: set[str]) -> list[str]:
    tmp = open(corpus).read().split()
    return [token for t in tmp for token in postprocess(delimit(t, delimiters))]


if __name__ == '__main__':
    corpus = 'dat/text_processing/emory-wiki.txt'
    delimiters = {'"', "'", '(', ')', '[', ']', ':', '-', ',', '.'}

    # # Word Counting
    # words = open(corpus).read().split()
    # word_counts = Counter(words)
    # print('# of word tokens: {}'.format(len(words)))
    # print('# of word types: {}'.format(len(word_counts)))
    #
    # topk = top_k_words(word_counts, 10)
    # for word, count in topk: print(word, count)
    #
    # topk = top_k_words(word_counts, 10, False)
    # for word, count in topk: print(word, count)
    #
    # Tokenization
    # fout = open('dat/text_processing/word_types.txt', 'w')
    # for key in sorted(word_counts.keys()): fout.write('{}\n'.format(key))
    #
    # tests = ['"R1:', '(R&D)', '15th-largest', 'Atlanta,', "Department's", 'activity"[26]', 'centers.[21][22]', '149,000', 'U.S.']
    # for test in tests:
    #     print('{} -> {}'.format(test, postprocess(delimit(test, delimiters))))
    #
    # words = tokenize(corpus, delimiters)
    # word_counts = Counter(words)
    # print('# of word tokens: {}'.format(len(words)))
    # print('# of word types: {}'.format(len(word_counts)))
    #
    # fout = open('dat/text_processing/word_types-token.txt', 'w')
    # for key in sorted(word_counts.keys()): fout.write('{}\n'.format(key))

    # Lemmatization
    singular_nouns = {noun.strip() for noun in open('dat/text_processing/nouns.txt')}
    irregular_nouns = {'children': 'child', 'mice': 'mouse', 'crises': 'crisis'}
    plural_rules = {'ies': 'y', 'es': '', 's': '', 'men': 'man', 'i': 'us'}

    tests = ['studies', 'crosses', 'areas', 'gentlemen', 'alumni', 'children', 'crises']
    for test in tests:
        print('{} -> {}'.format(test, noun_lemma(test, singular_nouns, irregular_nouns, plural_rules)))

