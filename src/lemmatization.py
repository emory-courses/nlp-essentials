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

import json
from collections import Counter
from types import SimpleNamespace

from src.tokenization import tokenize, DELIMITERS


def get_lemma_lexica() -> SimpleNamespace:
    return SimpleNamespace(
        nouns={noun.strip() for noun in open('dat/text_processing/nouns.txt')},
        verbs={noun.strip() for noun in open('dat/text_processing/verbs.txt')},
        nouns_irregular=json.load(open('dat/text_processing/nouns_irregular.json')),
        verbs_irregular=json.load(open('dat/text_processing/verbs_irregular.json')),
        nouns_rules=json.load(open('dat/text_processing/nouns_rules.json')),
        verbs_rules=json.load(open('dat/text_processing/verbs_rules.json'))
    )


def lemmatize(word: str, lexica: SimpleNamespace) -> str:
    def aux(word: str, vocabs: dict[str, str], irregular: dict[str, str], rules: list[tuple[str, str]]):
        lemma = irregular.get(word, None)
        if lemma is not None: return lemma

        for p, s in rules:
            lemma = word[:-len(p)] + s
            if lemma in vocabs: return lemma

        return None

    word = word.lower()
    lemma = aux(word, lexica.verbs, lexica.verbs_irregular, lexica.verbs_rules)

    if lemma is None:
        lemma = aux(word, lexica.nouns, lexica.nouns_irregular, lexica.nouns_rules)

    return lemma if lemma else word


if __name__ == '__main__':
    lemma_lexica = get_lemma_lexica()

    test_nouns = ['studies', 'crosses', 'areas', 'gentlemen', 'vertebrae', 'alumni', 'children', 'crises']
    for word in test_nouns: print('{} -> {}'.format(word, lemmatize(word, lemma_lexica)))

    test_verbs = ['applies', 'cried', 'pushes', 'entered', 'takes', 'heard', 'lying', 'studying', 'taking', 'drawn', 'clung', 'was', 'bought']
    for word in test_verbs: print('{} -> {}'.format(word, lemmatize(word, lemma_lexica)))

    corpus = 'dat/text_processing/emory-wiki.txt'
    words = [lemmatize(word, lemma_lexica) for word in tokenize(corpus, DELIMITERS)]
    word_counts = Counter(words)

    print('# of word tokens: {}'.format(len(words)))
    print('# of word types: {}'.format(len(word_counts)))

    fout = open('dat/text_processing/word_types-token-lemma.txt', 'w')
    for key in sorted(word_counts.keys()): fout.write('{}\n'.format(key))
