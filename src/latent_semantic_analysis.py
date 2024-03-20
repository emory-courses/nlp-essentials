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

import time

import numpy as np

from src.types import Document, Vocab


def retrieve(filename: str) -> tuple[list[Document], Vocab]:
    documents = [line.split() for line in open(filename)]
    t = {word for document in documents for word in document}
    terms = {term: j for j, term in enumerate(sorted(list(t)))}
    return documents, terms


def document_term_matrix(documents: list[Document], terms: Vocab) -> np.array:
    def doc_vector(document: list[str]) -> list[int]:
        v = [0] * len(terms)
        for term in document:
            v[terms[term]] += 1
        return v

    return np.array([doc_vector(document) for document in documents])


def document_term_matrix_np(documents: list[Document], terms: Vocab) -> np.array:
    X = np.zeros((len(documents), len(terms)), dtype=int)
    for i, document in enumerate(documents):
        for term in document:
            X[i, terms[term]] += 1
    return X


def print_np(matrix: np.array):
    print(matrix.shape)
    for row in matrix:
        print(' '.join(['{:8.4f}'.format(c) for c in row]))


if __name__ == '__main__':
    # D, T = retrieve('dat/chronicles_of_narnia.txt')

    # st = time.time()
    # X = document_term_matrix(D, T)
    # et = time.time()
    # print("|D| = {}, |T| = {}, Process Time (sec) = {:.2f}".format(len(X), len(X[0]), et - st))

    # st = time.time()
    # X = document_term_matrix_np(D, T)
    # et = time.time()
    # print("|D| = {}, |T| = {}, Process Time (sec) = {:.2f}".format(len(X), len(X[0]), et - st))

    D, T = retrieve('dat/latent_semantic_analysis.txt')
    X = document_term_matrix_np(D, T)
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    S = np.diag(S)

    print_np(U)
    print_np(S)
    print_np(Vt)

    # k = 4
    # print_np(np.diag(S)[:k, :k])

    # print(S)
    # k = 6
    # U = U[:, :k]
    # S = np.diag(S[:k])
    # V = Vt[:k, :].transpose()
    #
    # for i, document in enumerate(D):
    #     t = np.dot(U[i], S)
    #     print('{:>10}: {}'.format(' '.join(document), ['{:5.2f}'.format(f) for f in t]))
    #
    # for term, j in sorted(T.items(), key=lambda x: x[1]):
    #     t = np.dot(V[j], S)
    #     print('{:>5}: {}'.format(term, ['{:5.2f}'.format(f) for f in t]))
