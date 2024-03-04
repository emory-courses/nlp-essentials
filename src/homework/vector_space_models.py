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


def read(filename: str) -> list[tuple[int, str]]:
    def aux(s: str) -> tuple[int, str]:
        t = s.split('\t')
        return int(t[0]), t[1]

    return [aux(line) for line in open(filename)]


def sentiment_analyzer(trn_dat: list[tuple[int, str]], tst_dat: list[tuple[int, str]]) -> list[tuple[int, float]]:
    # To be filled
    return []


if __name__ == '__main__':
    trn_dat = read('dat/sentiment_treebank/sst_trn.tsv')
    dev_dat = read('dat/sentiment_treebank/sst_dev.tsv')
    preds = sentiment_analyzer(trn_dat, dev_dat)

    correct = 0
    for i, (pred, score) in enumerate(preds):
        if pred == dev_dat[i][0]:
            correct += 1

    print('Accuracy: {} ({}/{})'.format(100 * correct / len(dev_dat), correct, len(dev_dat)))
