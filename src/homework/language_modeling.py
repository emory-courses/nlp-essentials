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

from src.ngram_models import Bigram

UNKNOWN = ''
INIT = '[INIT]'


def bigram_model(filepath: str) -> Bigram:
    # To be updated
    pass


def sequence_generator(bigram_probs: Bigram, init_word: str, length: int = 20) -> tuple[list[str], float]:
    # To be updated
    pass


def sequence_generator_max(bigram_probs: Bigram, init_word: str, length: int = 20) -> tuple[list[str], float]:
    # To be updated
    pass


if __name__ == '__main__':
    filepath = 'dat/chronicles_of_narnia.txt'
    bigram_probs = bigram_model(filepath)
    sequence_generator(bigram_probs, 'I')
