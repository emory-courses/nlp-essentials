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

from src.types import Unigram


def unigram_estimation_smoothing(filepath: str) -> Unigram:
    unigrams, total = Counter(), 0

    for line in open(filepath):
        words = line.split()
        unigrams.update(words)
        total += len(words)

    return {word: count / total for word, count in unigrams.items()}

if __name__ == '__main__':
    pass
