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
    embeddings = {}
    for line in open(filepath, 'r'):
        parts = line.strip().split()
        word = parts[0]
        vector = np.array([float(x) for x in parts[1:]], dtype=np.float32)
        embeddings[word] = vector
    return embeddings

def cosine_similarity(u: np.array, v: np.array) -> float:
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    if norm_u == 0 or norm_v == 0:
        return 0.0
    return dot_product / (norm_u * norm_v)
def similar_words(word_embeddings: dict[str, np.array], target_word: str, threshold: float = 0.8) -> list[tuple[str, float]]:
    if target_word not in word_embeddings:
        return []
    target_embedding = word_embeddings[target_word]
    similarities = []

    for word, embedding in word_embeddings.items():
        if word != target_word:
            sim = cosine_similarity(target_embedding, embedding)
            if sim >= threshold:
                similarities.append((word, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities


def document_embedding(word_embeddings: dict[str, np.array], document: str) -> np.array:
    embeddings = []
    for word in document.split():
        if word in word_embeddings:
            embeddings.append(word_embeddings[word])
    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
       return np.zeros_like(next(iter(word_embeddings.values())))


def document_similarity(word_embeddings: dict[str, np.array], d1: str, d2: str) -> float:
    doc1_embedding = document_embedding(word_embeddings, d1)
    doc2_embedding = document_embedding(word_embeddings, d2)

    return cosine_similarity(doc1_embedding, doc2_embedding)


if __name__ == '__main__':
    filepath = 'dat/word_embeddings.txt'
    word_embeddings = read_word_embeddings(filepath)
    print(similar_words(word_embeddings, 'America', 0.8))
    d1 = 'I love this movie'
    d2 = 'I hate this movie'
    document_similarity(word_embeddings, d1, d2)