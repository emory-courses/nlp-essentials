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

from collections import Counter
from typing import TypeAlias

Document: TypeAlias = list[str]
Vocab: TypeAlias = dict[str, int]
SparceVector: TypeAlias = dict[int, int]


def vocabulary(documents: list[Document]) -> Vocab:
    vocab = set()

    for document in documents:
        vocab.update(document)

    return {word: i for i, word in enumerate(sorted(list(vocab)))}


def bag_of_words(vocab: Vocab, document: Document) -> SparceVector:
    counts = Counter(document)
    return {vocab[word]: count for word, count in sorted(counts.items()) if word in vocab}


if __name__ == '__main__':
    documents = [
        ['John', 'bought', 'a', 'book', '.', 'The', 'book', 'was', 'funny', '.'],
        ['Mary', 'liked', 'the', 'book', '.', 'John', 'gave', 'it', 'to', 'Mary', '.']
    ]

    vocab = vocabulary(documents)
    print(vocab)

    print(bag_of_words(vocab, documents[0]))
    print(bag_of_words(vocab, documents[1]))
