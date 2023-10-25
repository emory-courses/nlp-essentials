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

import collections
import re

from src.types import WordCount, PairCount

EOW = '[EOW]'


def initialize(word_counts: WordCount) -> WordCount:
    return {' '.join(list(word) + [EOW]): count for word, count in word_counts.items()}


def expect(vocab: WordCount) -> PairCount:
    pairs = collections.defaultdict(int)

    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i + 1]] += freq

    return pairs


def maximize(vocab: WordCount, pairs: PairCount) -> WordCount:
    best = max(pairs, key=pairs.get)
    p = re.compile(r'(?<!\S)' + re.escape(' '.join(best)) + r'(?!\S)')
    return {p.sub(''.join(best), word): freq for word, freq in vocab.items()}


if __name__ == '__main__':
    word_counts = {'high': 12, 'higher': 14, 'highest': 10, 'low': 12, 'lower': 11, 'lowest': 13}
    vocab = initialize(word_counts)

    for i in range(10):
        pairs = expect(vocab)
        vocab = maximize(vocab, pairs)
        print(vocab)
