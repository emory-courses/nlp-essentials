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
    """
    Build a bigram language model from text file using Laplace smoothing, normalization, and initial word probabilities.

    :param filepath: Path to a text file.
    :return: Nested dictionary where:
             - Outer key is previous word (including INIT and UNKNOWN)
             - Inner key is current word (including UNKNOWN)
             - Value is P(current|previous) probability
    """
    # TODO: Task 1
    return dict()


def sequence_generator(bigram_probs: Bigram, init_word: str, length: int = 20) -> tuple[list[str], float]:
    """
    Generate a sequence of specified length starting with given word.

    :param bigram_probs: Bigram probabilities from bigram_model().
    :param init_word: First word in sequence.
    :param length: Number of words to generate.
    :return: Tuple containing:
             - list[str]: Generated sequence
             - float: Log probability of sequence using natural log
    """
    # TODO: Task 2
    return ([], 0.0)


def sequence_generator_plus(bigram_probs: Bigram, init_word: str, length: int = 20) -> tuple[list[str], float]:
    """
        Generate a sequence of specified length starting with given word, which generates sequences with
        higher probability scores and better semantic coherence compared to sequence_generator().

        :param bigram_probs: Bigram probabilities from bigram_model().
        :param init_word: First word in sequence.
        :param length: Number of words to generate.
        :return: Tuple containing:
                 - list[str]: Generated sequence
                 - float: Log probability of sequence using natural log
        """
    # TODO: Extra Credit
    return ([], 0.0)


if __name__ == '__main__':
    filepath = 'dat/chronicles_of_narnia.txt'
    bigram_probs = bigram_model(filepath)
    sequence_generator(bigram_probs, 'You')
