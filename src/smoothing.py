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

from src.ngram_models import unigram_count
from src.types import Unigram

UNKNOWN = ''


def unigram_smoothing(filepath: str) -> Unigram:
    counts = unigram_count(filepath)
    counts.update(counts.keys())
    total = sum(counts.values())
    unigrams = {word: count / total for word, count in counts.items()}
    unigrams[UNKNOWN] = 1 / total
    return unigrams


if __name__ == '__main__':
    # unigram estimation
    unigrams = unigram_smoothing('dat/chronicles_of_narnia.txt')
    unigram_list = [(word, prob) for word, prob in sorted(unigrams.items(), key=lambda x: x[1], reverse=True)]

    for word, prob in unigram_list[:300]:
        if word[0].isupper() and word.lower() not in unigrams:
            print("{:>10} {:.6f}".format(word, prob))
