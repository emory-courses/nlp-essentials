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


def parse_numeral(numeral: str) -> int:
    vals = {'I': 1, "V": 5, "X": 10}
    prev = numeral[0]
    val = vals[prev]

    for i in numeral[1:]:
        if vals[prev] < vals[i]: val -= vals[prev] * 2
        prev = i
        val += vals[i]

    return val


def chronicles_of_narnia(filepath: str) -> dict:
    file = open(filepath, 'r')
    info = {}
    book, chapter, token_count = None, None, 0
    chapters = []

    re_title = re.compile(r"([\w ,:']+) \( (19\d\d) \)")  # (title, year)
    re_chapter = re.compile(r'Chapter ([IVX]+)', re.IGNORECASE)  # (chapter numeral)

    # helper internal functions
    def close_chapter():
        nonlocal token_count
        nonlocal chapter
        nonlocal chapters
        chapter['token_count'] = token_count
        chapters.append(chapter)
        token_count = 0

    def close_book():
        nonlocal info
        nonlocal book
        nonlocal chapter
        nonlocal chapters
        close_chapter()  # add remaining chapter
        chapters.sort(key=lambda x: x['number'])
        info[book]['chapters'] = chapters
        chapter = None
        chapters = []

    # read line by line
    # if title, add chapters, parse title, parse year, and update current book
    # else if chapter, add previous chapter w/ token count, parse roman numeral, parse title in next line, update token counter
    # else add token count to current token counter
    for line in file:
        title_m = re_title.match(line)

        if title_m:
            if book:
                close_book()

            book = title_m.group(1)
            info[book] = {
                'title': book,
                'year': int(title_m.group(2))
            }
        else:
            chapter_m = re_chapter.match(line)

            if chapter_m:
                if chapter:
                    close_chapter()

                chapter = {
                    'number': parse_numeral(chapter_m.group(1)),
                    'title': file.readline().rstrip('\n')
                }
            else:
                token_count += len(line.split(' '))

    close_book()  # add final book

    file.close()
    return info


RE_Abbreviation = r'[A-Za-z\.]+\.'  # will also match end of sentence but is flexible and will match etc., etc
RE_Apostrophe = r'(?<!\w)\'[\d\w]+'
RE_Concatenation = r'(?i)\w+\'\w+|\b\w+[nmt]{2}[ae]\b|\b\w+[^aeiou][dt]a\b|cannot'  # hard coded cannot because funny/planning would be recognized w/ general
RE_Hyperlink = r'[\w]+://(?:[\d\w]+\.)+\w+[\S]+'
RE_Number = r'(?:\d+[,./\-]?)+'
RE_Unit = r'[$#€£]\d+|(?<!\w)\d+[A-Za-z%]+'

if __name__ == '__main__':
    # txtfile = 'dat/chronicles_of_narnia_abridged.txt'
    txtfile = 'dat/chronicles_of_narnia.txt'
    d = chronicles_of_narnia(txtfile)
    print(d)

    r = re.compile(RE_Abbreviation)
    print(r.match('U.S.A.'))
    print(r.findall('I see Dr. Mike (M.D.) for my conditions while I\'m in the U.S.A.'))
    r = re.compile(RE_Apostrophe)
    print(r.match('\'80s'))
    print(r.findall('I love to listen to \'80s music too, just \'cause! Who\'s your favorite artist?'))
    r = re.compile(RE_Concatenation)
    print(r.match('gonna'))
    print(r.findall('Please don\'t touch that - y\'ardy know I\'m GONNA get mad.'))
    r = re.compile(RE_Hyperlink)
    print(r.match('https://emory.gitbook.io/nlp-essentials'))
    print(r.findall('go to https://emory.gitbook.io/nlp-essentials to see the nlp course!'))
    r = re.compile(RE_Number)
    print(r.match('192.168.2.1'))
    print(r.findall('Call 123-456-7890 or visit us at 20.43.154.3 for 1/2 off our $30 bagels!'))
    r = re.compile(RE_Unit)
    print(r.match('6000kg'))
    print(r.findall('And the prize goes to #20'))