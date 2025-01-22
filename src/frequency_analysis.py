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


def count_words(corpus: str) -> Counter:
    fin = open(corpus)
    words = fin.read().split()
    return Counter(words)


def save_output(counts: Counter, outfile: str):
    fout = open(outfile, 'w')

    for word in sorted(counts.keys()):
        fout.write(f'{word}\n')

    fout.close()


if __name__ == '__main__':
    corpus = 'dat/emory-wiki.txt'
    counts = count_words(corpus)

    # Word Counting
    n_tokens = sum(counts.values())
    n_types = len(counts)

    print(f'# of word tokens: {n_tokens}')
    print(f'# of word types: {n_types}')

    # Word Frequency
    des = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    asc = sorted(counts.items(), key=lambda x: x[1])

    for word, count in des[:10]: print(word, count)
    for word, count in asc[:10]: print(word, count)

    # Save Output
    save_output(counts, 'dat/word_types.txt')
