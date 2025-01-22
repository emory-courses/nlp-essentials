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


def tokenize(text: str) -> list[str]:
    re_tok = re.compile(r'([",.]|\s+|n\'t)')
    tokens, prev_idx = [], 0

    for m in re_tok.finditer(text):
        t = text[prev_idx:m.start()].strip()
        if t: tokens.append(t)
        t = m.group().strip()

        if t:
            if tokens and tokens[-1] in {'Mr', 'Ms'} and t == '.':
                tokens[-1] = tokens[-1] + t
            else:
                tokens.append(t)

        prev_idx = m.end()

    t = text[prev_idx:]
    if t: tokens.append(t)
    return tokens


if __name__ == '__main__':
    # match()
    re_mr = re.compile(r'M[rs]\.')
    m = re_mr.match('Mr. Wayne')

    print(m)
    if m: print(m.start(), m.end())

    # group()
    print(m.groups())

    re_mr = re.compile(r'(M[rs])(\.)')
    m = re_mr.match('Ms.')

    print(m)
    print(m.group())
    print(m.groups())
    print(m.group(0), m.group(1), m.group(2))

    m = re_mr.match('Mrs.')
    print(m)

    # search()
    s1 = 'Mr. and Ms. Wayne are here'
    s2 = 'Here are Mr. and Ms. Wayne'

    print(re_mr.search(s1))
    print(re_mr.search(s2))

    # findall()
    print(re_mr.findall(s1))
    print(re_mr.findall(s2))

    # finditer()
    ms = re_mr.finditer(s1)
    for m in ms: print(m)

    ms = re_mr.finditer(s2)
    for m in ms: print(m)

    # sub()
    print(re_mr.sub('Dr.', 'I met Mr. Wayne and Ms. Kyle.'))

    # tokenize()
    text = 'Mr. Wayne isn\'t the hero we need, but "the one" we deserve.'
    print(tokenize(text))

    text = 'Ms. Wayne is "Batgirl" but not "the one".'
    print(tokenize(text))
