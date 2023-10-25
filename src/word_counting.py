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

CORPUS = 'dat/text_processing/emory-wiki.txt'


def top_k_words(word_counts: dict[str, int], k: int, top=True):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=top)[:k]


if __name__ == '__main__':
    words = open(CORPUS).read().split()
    word_counts = Counter(words)

    print('# of word tokens: {}'.format(len(words)))
    print('# of word types: {}'.format(len(word_counts)))

    topk = top_k_words(word_counts, 10)
    for word, count in topk: print(word, count)

    topk = top_k_words(word_counts, 10, False)
    for word, count in topk: print(word, count)

    fout = open('dat/text_processing/word_types.txt', 'w')
    for key in sorted(word_counts.keys()): fout.write('{}\n'.format(key))
