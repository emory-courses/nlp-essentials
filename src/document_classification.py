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

import glob
import os
from collections import Counter

from src.bag_of_words_model import vocabulary
from src.document_similarity import cosine_similarity
from src.term_weighing import document_frequencies, tf_idf
from src.types import Document, SparseVector, Vocab


def collect(dirpath: str) -> dict[int, list[Document]]:
    books = dict()

    for filename in glob.glob(os.path.join(dirpath, '*.txt')):
        t = os.path.basename(filename).split('_')
        book_id = int(t[0])
        fin = open((filename))
        books.setdefault(book_id, list()).append(fin.read().split())

    return books


def join_documents(dataset: dict[int, list[Document]]) -> list[Document]:
    return [document for documents in dataset.values() for document in documents]


def vectorize(vocab: Vocab, dfs: SparseVector, D: int, docset: dict[int, list[Document]]) -> list[tuple[int, SparseVector]]:
    vs = []

    for book_id, documents in docset.items():
        for document in documents:
            vs.append((book_id, tf_idf(vocab, dfs, D, document)))

    return vs


def knn(trn_vs: list[tuple[int, SparseVector]], document: SparseVector, k: int = 1) -> tuple[int, float]:
    sims = [(book_id, cosine_similarity(document, v)) for book_id, v in trn_vs]
    sims.sort(key=lambda x: x[1], reverse=True)
    return Counter(sims[:k]).most_common(1)[0][0]


if __name__ == '__main__':
    trn = collect('dat/document_classification/trn')
    dev = collect('dat/document_classification/dev')
    tst = collect('dat/document_classification/tst')
    print(len(join_documents(trn)), len(join_documents(dev)), len(join_documents(tst)))

    corpus = join_documents(trn)
    vocab = vocabulary(join_documents(trn))
    dfs = document_frequencies(vocab, corpus)
    D = len(corpus)

    trn_vs = vectorize(vocab, dfs, D, trn)
    dev_vs = vectorize(vocab, dfs, D, dev)
    tst_vs = vectorize(vocab, dfs, D, tst)

    correct = 0
    for g_book_id, document in dev_vs:
        p_book_id, p_score = knn(trn_vs, document)
        print('Gold: {}, Auto: {}, Score: {:.2f}'.format(g_book_id, p_book_id, p_score))
        if g_book_id == p_book_id: correct += 1
    print('Accuracy: {} ({}/{})'.format(100 * correct / len(dev_vs), correct, len(dev_vs)))
