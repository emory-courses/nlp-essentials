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

from src.types import SparseVector


def collect(dirpath: str) -> dict[int, list[SparseVector]]:
    for filename in glob.glob(os.path.join(dirpath, '*.txt')):
        print(filename)


if __name__ == '__main__':
    trn = collect('dat/vector_space_models/trn')
    dev = collect('dat/vector_space_models/dev')
