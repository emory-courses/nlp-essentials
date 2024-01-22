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


def chronicles_of_narnia(filepath: str) -> dict:
    # To be updated
    pass


RE_Abbreviation = r'to be filled'
RE_Apostrophe = r'to be filled'
RE_Concatenation = r'to be filled'
RE_Hyperlink = r'to be filled'
RE_Number = r'to be filled'
RE_Unit = r'to be filled'

if __name__ == '__main__':
    txtfile = 'dat/chronicles_of_narnia.txt'
    d = chronicles_of_narnia(txtfile)
    print(d)

    r = re.compile(RE_Abbreviation)
    print(r.match('Dr.'))
