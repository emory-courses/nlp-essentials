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

if __name__ == '__main__':
    # Word Count
    corpus = 'dat/text_processing/emory-wiki.txt'
    words = open(corpus).read().split()
    word_counts = Counter(words)

    print('# of word tokens: {}'.format(len(words)))
    print('# of word types: {}'.format(len(word_counts)))

    # Top-k Frequent Words
    wc_des = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in wc_des[:10]: print(word, count)

    wc_asc = sorted(word_counts.items(), key=lambda x: x[1])
    for word, count in wc_asc[:10]: print(word, count)

    # Save Output
    fout = open('dat/text_processing/word_types.txt', 'w')
    for key in sorted(word_counts.keys()): fout.write('{}\n'.format(key))
    fout.close()