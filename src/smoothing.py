# ========================================================================
# Copyright 2024 Emory University
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

from src.ngram_models import unigram_count, test_unigram, bigram_count, test_bigram
from src.types import Unigram, Bigram

UNKNOWN = ''


def unigram_smoothing(filepath: str) -> Unigram:
    counts = unigram_count(filepath)
    total = sum(counts.values()) + len(counts)
    unigrams = {word: (count + 1) / total for word, count in counts.items()}
    unigrams[UNKNOWN] = 1 / total
    return unigrams


def smoothed_unigram(probs: Unigram, word: str) -> float:
    return probs.get(word, probs[UNKNOWN])


def bigram_smoothing(filepath: str) -> Bigram:
    counts = bigram_count(filepath)
    vocab = set(counts.keys())
    for _, css in counts.items():
        vocab.update(css.keys())

    bigrams = dict()
    for prev, ccs in counts.items():
        total = sum(ccs.values()) + len(vocab)
        d = {curr: count / total for curr, count in ccs.items()}
        d[UNKNOWN] = 1 / total
        bigrams[prev] = d

    bigrams[UNKNOWN] = 1 / len(vocab)
    return bigrams


def smoothed_bigram(probs: Bigram, prev: str, curr: str) -> float:
    d = probs.get(prev, None)
    return probs[UNKNOWN] if d is None else d.get(curr, d[UNKNOWN])


if __name__ == '__main__':
    corpus = 'dat/chronicles_of_narnia.txt'

    # unigram
    test_unigram(corpus, unigram_smoothing)
    unigram = unigram_smoothing(corpus)
    for word in ['Aslan', 'Jinho']:
        print("{} {:.6f}".format(word, smoothed_unigram(unigram, word)))

    # bigram
    test_bigram(corpus, bigram_smoothing)
    bigram = bigram_smoothing(corpus)
    for word in [('Aslan', 'is'), ('Aslan', 'Jinho'), ('Jinho', 'is')]:
        print("{} {:.6f}".format(word, smoothed_bigram(bigram, *word)))
