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

from collections import Counter, defaultdict
from collections.abc import Callable

from src.types import Unigram, Bigram


def unigram_count(filepath: str) -> Counter:
    unigrams = Counter()

    for line in open(filepath):
        words = line.split()
        unigrams.update(words)

    return unigrams


def unigram_estimation(filepath: str) -> Unigram:
    counts = unigram_count(filepath)
    total = sum(counts.values())
    return {word: count / total for word, count in counts.items()}


def bigram_count(filepath: str) -> dict[str, Counter]:
    bigrams = defaultdict(Counter)

    for line in open(filepath):
        words = line.split()
        for i in range(1, len(words)):
            bigrams[words[i - 1]].update([words[i]])

    return bigrams


def bigram_estimation(filepath: str) -> Bigram:
    counts = bigram_count(filepath)
    bigrams = dict()

    for prev, ccs in counts.items():
        total = sum(ccs.values())
        bigrams[prev] = {curr: count / total for curr, count in ccs.items()}

    return bigrams


def test_unigram(filepath: str, estimator: Callable[[str], Unigram]):
    unigrams = estimator(filepath)
    unigram_list = [(word, prob) for word, prob in sorted(unigrams.items(), key=lambda x: x[1], reverse=True)]

    for word, prob in unigram_list[:300]:
        if word[0].isupper() and word.lower() not in unigrams:
            print("{:>10} {:.6f}".format(word, prob))


def test_bigram(filepath: str, estimator: Callable[[str], Bigram]):
    bigrams = bigram_estimation(filepath)
    for prev in ['I', 'the', 'said']:
        print(prev)
        bigram_list = [(curr, prob) for curr, prob in sorted(bigrams[prev].items(), key=lambda x: x[1], reverse=True)]
        for curr, prob in bigram_list[:10]:
            print("{:>10} {:.6f}".format(curr, prob))


if __name__ == '__main__':
    corpus = 'dat/chronicles_of_narnia.txt'
    test_unigram(corpus, unigram_estimation)
    test_bigram(corpus, bigram_estimation)
