# ========================================================================
# Copyright ${} Emory University
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

import inspect

import streamlit as st

import src.frequency_analysis
from src.utils import output, quiz, code


def z1a_word_counting():
    st.header('Word Counting', anchor='1a-word-counting')
    st.write(
        'Consider the following text from Wikipedia about [Emory University](https://en.wikipedia.org/wiki/Emory_University) (as of 2023-10-18):')
    with open('dat/emory-wiki.txt') as fin:
        output('[dat/emory-wiki.txt](dat/emory-wiki.txt)', fin.read(), True)
    st.write('Our task is to determine the number of word tokens and unique word types in this text.')
    quiz('Q1')
    st.write(
        'A simple way of accomplishing this task is to split the text by whitespace and count the resulting strings:')
    code('from collections import Counter', """
        * L1: Import the [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) class from the [collections](https://docs.python.org/3/library/collections.html) package.
    """)
    code(inspect.getsource(src.frequency_analysis.count_words), """
        * L1: Use [typing](https://docs.python.org/3/library/typing.html) to indicate the parameter type, `str`, and the return type, `Counter`.
        * L2: [open()](https://docs.python.org/3/library/functions.html#open) the corpus file.
        * L3: [read()](https://docs.python.org/3/library/io.html#io.TextIOBase.read) the contents of the file as a string, [split()](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split) it into a [list](https://docs.python.org/3/library/stdtypes.html#list) of words, and store them in `words`.
        * L4: Count the occurrences of each word in `words` and return the results as a Counter, which is a speical type of a [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping).
    """)
    st.write('Let us test `count_words()`:')
    code("""
        corpus = 'dat/emory-wiki.txt'
        counts = count_words(corpus)
        
        n_tokens = sum(counts.values())
        n_types = len(counts)
        
        print(f'# of word tokens: {n_tokens}')
        print(f'# of word types: {n_types}')
    """, """
        * L4: Save the total number of word tokens in the corpus, which is the [sum()](https://docs.python.org/3/library/functions.html#sum) of `counts` values.
        * L5: Save the number of unique word types in the corpus, which is the [len()](https://docs.python.org/3/library/functions.html#len) of `counts`.
        * L7-8: Print the value using the [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).    
    """)

    output('Output:', """
        # of word tokens: 305
        # of word types: 180            
    """)


def z1a_word_frequency():
    st.header('Word Frequency', anchor='1a-word-frequency')
    st.write('In this task, we aim to retrieve the top-_k_ most or least frequently occurring word types in the text:')
    code("""
        des = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        asc = sorted(counts.items(), key=lambda x: x[1])
    
        for word, count in des[:10]: print(word, count)
        for word, count in asc[:10]: print(word, count)
    """, """
        * L1: Sort words in `counts` in descending order ([sorted()](https://docs.python.org/3/library/functions.html#sorted), [items()](https://docs.python.org/3/library/stdtypes.html#dict.items), [lambda](https://docs.python.org/3/reference/expressions.html#lambda)) and save them into `dec` as a list of (word, count) tuples, sorted from the most frequent to the least frequent words.
        * L2: Sort words in `counts` in ascending order and save them into `asc` as a list of (word, count) [tuples](https://docs.python.org/3/library/stdtypes.html#tuples).
        * L4: Iterate over the top _k_ most frequent words in the sorted list using [slice](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) and print each word along with its count.
        * L5: Iterate over the top _k_ least frequent words in the sorted list zand print each word along with its count.
    """)
    output('Output (most frequent):', """
        the 18
        and 15
        of 12
        Emory 11
        in 10
        University 7
        is 7
        university 6
        United 6
        research 5    
    """)
    output('Output (least frequent):', """
        private 1
        Atlanta, 1
        Georgia. 1
        Founded 1
        1836 1
        College 1
        by 1
        Episcopal 1
        Church 1
        named 1
    """)
    st.markdown("""
        Notice that the top-10 least-frequent word list contains unnormalized words such as "_Atlanta,_" (with the comma) and "_Georgia._" (with the period).
        This occurs because the text was split only by whitespaces without considering punctuation.
        Consequently, these words are recognized separately from the word types "_Atlanta_" and "_Georgia_".
        Therefore, the counts of word tokens and types processed above do not necessarily represent the distributions of the text accurately.    
    """)
    quiz('Q2')


def z1a_save_output():
    st.header('Save Output', anchor='1a-save-output')
    st.write('Finally, let us save all word types in alphabetical order to a file:')
    code(inspect.getsource(src.frequency_analysis.save_output), """
        * L2: Open `outfile` in [write](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) mode (`w`).
        * L4: Iterate over unique word types (keys) of `counts` in alphabetical order.
        * L5: Write each word followed by a newline character to `fout`.
        * L7: Close the output stream.    
    """)
    st.write(
        'Running `save_output()` creates the [dat/word_types.txt](dat/word_types.txt) file if it does not exist; otherwise, its previous contents will be completely overwritten:')
    code("save_output(counts, 'dat/word_types.txt')")
