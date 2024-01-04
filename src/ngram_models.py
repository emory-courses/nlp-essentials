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
from typing import DefaultDict

from src import types


def unigram_estimation(filepath: str) -> dict[str, float]:
    unigrams, total = Counter(), 0

    for line in open(filepath):
        words = line.split()
        unigrams.update(words)
        total += len(words)

    return {word: count / total for word, count in unigrams.items()}


def bigram_estimation(filepath: str) -> dict[tuple[str, str], float]:
    unigrams, bigrams = Counter(), Counter()

    for line in open(filepath):
        words = line.split()
        unigrams.update(words)
        bigrams.update([(words[i], words[i+1]) for i in range(len(words) - 1)])

    return {(w1, w2): count / unigrams[w1] for (w1, w2), count in bigrams.items()}

if __name__ == '__main__':
    # unigram estimation
    # unigrams = unigram_estimation('dat/chronicles_of_narnia.txt')
    # unigram_list = [(word, prob) for word, prob in sorted(unigrams.items(), key=lambda x: x[1], reverse=True)]
    #
    # for word, prob in unigram_list[:300]:
    #     if word[0].isupper() and word.lower() not in unigrams:
    #         print("{:>10} {:.6f}".format(word, prob))

    # bigram estimation
    bigrams = bigram_estimation('dat/chronicles_of_narnia.txt')
    bigram_list = [(' '.join(bigram), prob) for bigram, prob in sorted(bigrams.items(), key=lambda x: x[1], reverse=True)]

    for bigram, prob in bigram_list[:10]:
        print("{:>20} {:.6f}".format(bigram, prob))