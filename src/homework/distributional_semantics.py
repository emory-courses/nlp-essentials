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

__author__ = 'Paige Hendricks'

import numpy as np


def read_word_embeddings(filepath: str) -> dict[str, np.array]:
    # To be filled
    pass


def similar_words(word_embeddings: dict[str, np.array], target_word: str, threshold: float = 0.8) -> list[
    tuple[str, float]]:
    # To be filled
    pass


def document_similarity(word_embeddings: dict[str, np.array], d1: str, d2: str) -> float:
    # To be filled
    pass


if __name__ == '__main__':
    filepath = 'dat/word_embeddings.txt'
    word_embeddings = read_word_embeddings(filepath)
    print(similar_words(word_embeddings, 'America', 0.8))
    d1 = 'I love this movie'
    d2 = 'I hate this movie'
    document_similarity(word_embeddings, d1, d2)