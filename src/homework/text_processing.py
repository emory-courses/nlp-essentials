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

import re

TITLE = 'title'
YEAR = 'year'
CHAPTERS = 'chapters'
NUMBER = 'number'
TOKEN_COUNT = 'token_count'


def chronicles_of_narnia(filepath: str) -> dict:
    """
    Extract structured information from Chronicles of Narnia text file.

    :param filepath: Path to the input text file.
    :return: Dictionary containing book metadata and chapter statistics.
    """
    # TODO: Task 1
    return dict()


EMAIL = 'email'
DATE = 'date'
URL = 'url'
CITE = 'cite'


def regular_expressions(text: str) -> str | None:
    """
    Identifies the type of a given text pattern.

    :param text: String to classify.
    :return: One of "email", "date", "url", "cite"; None, if no pattern matches.
    """
    # TODO: Task 2
    return None


if __name__ == '__main__':
    filepath = 'dat/chronicles_of_narnia.txt'
    d = chronicles_of_narnia(filepath)
    print(d)

    regex_tests = [
        'student@emory.edu',  # email
        '2024/12/25',  # date
        'http://www.emory.edu',  # URL
        'Smith, 2024'  # citation
    ]

    for test in regex_tests:
        print(regular_expressions(test))
