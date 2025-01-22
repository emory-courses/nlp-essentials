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

from src.frequency_analysis import save_output


def delimit(word: str, delimiters: set[str]) -> list[str]:
    i = next((i for i, c in enumerate(word) if c in delimiters), -1)
    if i < 0: return [word]
    tokens = []

    if i > 0: tokens.append(word[:i])
    tokens.append(word[i])

    if i + 1 < len(word):
        tokens.extend(delimit(word[i + 1:], delimiters))

    return tokens


def postprocess(tokens: list[str]) -> list[str]:
    i, new_tokens = 0, []

    while i < len(tokens):
        if i + 1 < len(tokens) and tokens[i] == "'" and tokens[i + 1].lower() == 's':
            new_tokens.append(''.join(tokens[i:i + 2]))
            i += 1
        elif i + 2 < len(tokens) and \
                ((tokens[i] == '[' and tokens[i + 1].isnumeric() and tokens[i + 2] == ']') or
                 (tokens[i].isnumeric() and tokens[i + 1] == ',' and tokens[i + 2].isnumeric())):
            new_tokens.append(''.join(tokens[i:i + 3]))
            i += 2
        elif i + 3 < len(tokens) and ''.join(tokens[i:i + 4]) == 'U.S.':
            new_tokens.append(''.join(tokens[i:i + 4]))
            i += 3
        else:
            new_tokens.append(tokens[i])
        i += 1

    return new_tokens


def tokenize(corpus: str, delimiters: set[str]) -> list[str]:
    with open(corpus) as fin:
        words = fin.read().split()
    return [token for word in words for token in postprocess(delimit(word, delimiters))]


if __name__ == '__main__':
    delims = {'"', "'", '(', ')', '[', ']', ':', '-', ',', '.'}

    input = [
        '"R1:',
        '(R&D)',
        '15th-largest',
        'Atlanta,',
        "Department's",
        'activity"[26]',
        'centers.[21][22]',
        '149,000',
        'U.S.'
    ]

    # Delimiters
    output = [delimit(word, delims) for word in input]

    for word, tokens in zip(input, output):
        print('{:<16} -> {}'.format(word, tokens))

    # Postprocessing
    output = [postprocess(delimit(word, delims)) for word in input]

    for word, tokens in zip(input, output):
        print('{:<16} -> {}'.format(word, tokens))

    # Tokenizing
    corpus = 'dat/emory-wiki.txt'
    output = 'dat/word_types-token.txt'

    words = tokenize(corpus, delims)
    counts = Counter(words)

    print(f'# of word tokens: {len(words)}')
    print(f'# of word types: {len(counts)}')

    save_output(counts, output)
