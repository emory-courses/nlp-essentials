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

import math
from collections import Counter
from string import punctuation
from typing import Callable

from elit_tokenizer import EnglishTokenizer

from src.bag_of_words_model import vocabulary, bag_of_words, Document, Vocab, SparseVector


def read_corpus(filename: str, tokenizer: Callable[[str], list[str]] | None = None) -> list[Document]:
    fin = open(filename)
    if tokenizer is None: tokenizer = lambda s: s.split()
    return [tokenizer(line) for line in fin]


def print_tfs(vocab: Vocab, documents: list[Document]):
    tfs = [bag_of_words(vocab, document) for document in documents]
    words = [word for word, _ in sorted(vocab.items(), key=lambda x: x[1])]
    for tf in tfs:
        print([(words[index], count) for index, count in sorted(tf.items(), key=lambda x: x[1], reverse=True)])


def document_frequencies(vocab: Vocab, corpus: list[Document]) -> SparseVector:
    counts = Counter()
    for document in corpus:
        counts.update(set(document))
    return {vocab[word]: count for word, count in sorted(counts.items()) if word in vocab}


def tf_idf(vocab: Vocab, dfs: SparseVector, D: int, document: Document) -> SparseVector:
    tf = lambda count: count / len(document)
    idf = lambda tid: math.log(D / dfs[tid])
    return {tid: tf(count) * idf(tid) for tid, count in bag_of_words(vocab, document).items()}


if __name__ == '__main__':
    # Term Frequency
    corpus = read_corpus('dat/chronicles_of_narnia.txt')
    vocab = vocabulary(corpus)
    ds = [
        "As dawn broke, the first light kissed the golden mane of Aslan, the rightful king of Narnia.",
        "The White Witch's icy breath froze the once lush meadows, casting a shadow over Narnia.",
        "Lucy's footsteps echoed in the halls of Cair Paravel, where legends were born."
    ]

    etok = EnglishTokenizer()
    documents = [etok.decode(d).tokens for d in ds]
    print_tfs(vocab, documents)

    # Stop Words
    stopwords = {line.strip().lower() for line in open('dat/stopwords.txt')}
    is_stopwords = lambda w: w.lower() in stopwords or w in punctuation

    sw_tokenizer = lambda s: [word for word in s.split() if not is_stopwords(word)]
    corpus = read_corpus('dat/chronicles_of_narnia.txt', sw_tokenizer)
    vocab = vocabulary(corpus)
    print_tfs(vocab, documents)

    # Document Frequency
    corpus = read_corpus('dat/chronicles_of_narnia.txt')
    vocab = vocabulary(corpus)
    words = [word for word, _ in sorted(vocab.items(), key=lambda x: x[1])]

    dfs = document_frequencies(vocab, corpus)
    for document in documents:
        bow = bag_of_words(vocab, document)
        tf_df = [(words[tid], tf, dfs[tid]) for tid, tf in sorted(bow.items())]
        tf_df = sorted(tf_df, key=lambda x: (-x[1], x[2]))
        print(' '.join(document))
        print('\n'.join(['{:>10}  {}  {:>5}'.format(*t) for t in tf_df]))

    # TF-IDF
    for document in documents:
        tfidf = tf_idf(vocab, dfs, len(corpus), document)
        print(' '.join(document))
        print('\n'.join(['{:>10}  {:.2f}'.format(words[tid], score) for tid, score in sorted(tfidf.items(), key=lambda x: x[1], reverse=True)]))
