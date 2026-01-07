---
title: Regular Expressions
---

**Regular expressions**, commonly abbreviated as **regex**, form a language for string matching, enabling operations to search, match, and manipulate text based on specific patterns or rules.

* Online Interpreter: [Regular Expressions 101](https://regex101.com)

## Core Syntax

### Metacharacters

Regex provides **metacharacters** with specific meanings, making it convenient to define patterns:

*   `.`: any single character except a newline character

    > e.g., `M.\.` matches "Mr." and "Ms.", but not "Mrs." (`\` escapes the metacharacter `.`).
*   `[ ]`: a character set matching any character within the brackets

    > e.g., `[aeiou]` matches any vowel.
*   `\d`: any digit, equivalent to `[0-9]`

    > e.g., `\d\d\d` searches for "170" in "CS170".
*   `\D`: any character that is not a digit, equivalent to `[^0-9]`

    > e.g., `\D\D` searches for "kg" in "100kg".
*   `\s`: any whitespace character, equivalent to `[ \t\n\r\f\v]`

    > e.g., `\s` searches for the space " " in "Hello World".
*   `\S`: any character that is not a whitespace character, equivalent to `[^ \t\n\r\f\v]`

    > e.g., `\S` searches for "H" in " Hello".
*   `\w`: any word character (alphanumeric or underscore), equivalent to `[A-Za-z0-9_]`

    > e.g., `\w\w` searches for "1K" in "$1K".
*   `\W`: any character that is not a word character, equivalent to `[^A-Za-z0-9_]`

    > e.g., `\W` searches for "!" in "Hello!".
*   `\b`: a word boundary matching the position between a word character and a non-word character

    > e.g., `\bis\b` matches "is", but does not match "island" nor searches for "is" in "basis".

:::info
☝️ The terms "_match_" and "_search_" in the above examples have different meanings. "**match**" means that the pattern must be found at the beginning of the text, while "**search**" means that the pattern can be located anywhere in the text. We will discuss these two functions in more detail in the [following section](#functions).
:::

### Repetitions

**Repetitions** allow you to define complex patterns that can match multiple occurrences of a character or group of characters:

*   `*`: the preceding character or group appears zero or more times

    > e.g., `\d*` matches "90" in "90s" as well as "" (empty string) in "ABC".
*   `+`: the preceding character or group appears one or more times

    > e.g., `\d+` matches "90" in "90s", but no match in "ABC".
*   `?`: the preceding character or group appears zero or once, making it optional

    > e.g., `https?` matches both "http" and "https".
*   `{m}`: the preceding character or group appears exactly `m` times

    > e.g., `\d{3}` is equivalent to `\d\d\d`.
*   `{m,n}`: the preceding character or group appears at least `m` times but no more than `n` times

    > e.g., `\d{2,4}` matches "12", "123", "1234", but not "1" or "12345".
*   `{m,}`: the preceding character or group appears at least `m` times or more

    > e.g., `\d{2,}` matches "12", "123", "1234", and "12345", but not "1".
*   By default, matches are "greedy" such that patterns match as many characters as possible

    > e.g., `<.+>` matches the entire string of "\<Hello> and \<World>".
*   Matches become "lazy" by adding `?` after the repetition metacharacters, in which case, patterns match as few characters as possible

    > e.g., `<.+?>` matches "\<Hello>" in "\<Hello> and \<World>", and searches for "\<World>" in the text.

### Groupings

**Grouping** allows you to treat multiple characters, subpatterns, or metacharacters as a single unit. It is achieved by placing these characters within parentheses `(` and `)`.

*   `|`: a logical OR, referred to as a "pipe" symbol, allowing you to specify alternatives

    > e.g., `(cat|dog)` matches either "cat" or "dog".
*   `( )`: a capturing group; any text that matches the parenthesized pattern is "captured" and can be extracted or used in various ways

    > e.g., `(\w+)@(\w+.\w+)` has two capturing groups, `(\w+)` and `(\w+.\w+)`, and matches email addresses such as "[john@emory.edu](mailto:john@emory.edu)" where the first and second groups capture "john" and "emory.edu", respectively.
*   `(?: )`: a non-capturing group; any text that matches the parenthesized pattern, while indeed matched, is not "captured" and thus cannot be extracted or used in other ways

    > e.g., `(?:\w+)@(\w+.\w+)` has one non-capturing group `(?:\w+)` and one capturing group `(\w+.\w+)`. It still matches "[john@emory.edu](mailto:john@emory.edu)" but only captures "emory.edu", not "john".
*   `\num`: a backreference that refers back to the most recently matched text by the `num`'th capturing group within the same regex

    > e.g., `(\w+) (\w+) - (\2), (\1)` has four capturing groups, where the third and fourth groups refer to the second and first groups, respectively. It matches "Jinho Choi - Choi, Jinho" where the first and fourth groups capture "Jinho" and the second and third groups capture "Choi".
*   You can nest groups within other groups to create more complex patterns

    > e.g., `(\w+.(edu|org))` has two capturing groups, where the second group is nested in the first group. It matches "emory.edu" or "emorynlp.org", where the first group captures the entire texts while the second group captures "edu" or "org", respectively.

### Assertions

**Assertions** define conditions that must be met for a match to occur. They do not consume characters in the input text but specify the position where a match should happen based on specific criteria.

*   A _positive lookahead assertion_ `(?= )` checks that a specific pattern is present immediately after the current position

    > e.g., `apple(?=[ -]pie)` matches "apple" in "apple pie" or "apple-pie", but not in "apple juice".
*   A _negative lookahead assertion_ `(?! )` checks that a specific pattern is not present immediately after the current position

    > e.g., `do(?!(?: not|n't))` matches "do" in "do it" or "doing", but not in "do not" or "don't".
*   A _positive look-behind assertion_ `(?<= )` checks that a specific pattern is present immediately before the current position

    > e.g., `(?<=\$)\d+` matches "100" in "$100", but not in "100 dollars".
*   A _negative look-behind assertion_ `(?<! )` checks that a specific pattern is not present immediately before the current position

    > e.g., `(?<!not )(happy|sad)` searches for "happy" in "I'm happy", but does not search for "sad" in "I'm not sad".
*   `^` asserts that the pattern following the _caret_ must match at the beginning of the text

    > e.g., `not` searches for "not" in "note" and "cannot", whereas `^not` matches "not" in "note" but not in "cannot".
*   `$` asserts that the pattern preceding the _dollar sign_ must match at the end of the text

    > e.g., `not$` searches for "not" in "cannot" but not in "note".

## Functions

Python provides several functions to make use of regular expressions.

### match()

Let us create a regular expression that matches "Mr." and "Ms.":

```python showLineNumbers title="Run"
import re

re_mr = re.compile(r'M[rs]\.')
m = re_mr.match('Mr. Wayne')

print(m)
if m: print(m.start(), m.end())
```

* L1: [Regular expression operations](https://docs.python.org/3/library/re.html).
* L3: Create a regular expression `re_mr` ([compile()](https://docs.python.org/3/library/re.html?highlight=re#re.compile)). Note that a string indicated by an `r` prefix is considered a regular expression in Python.
  * `r'M'` matches the letter "M".
  * `r'[rs]'` matches either "r" or "s".
  * `r'\.`' matches a period (dot).
* L4: Try to match `re_mr` at the beginning of the string "Mr. Wayne" ([match()](https://docs.python.org/3/library/re.html?highlight=re#re.match)).
* L6: Print the value of `m`. If matched, it prints the [match object](https://docs.python.org/3/library/re.html#match-objects) information; otherwise, `m` is `None`; thus, it prints "None".
* L7: Check if a match was found (`m` is not `None`), and print the start position ([start()](https://docs.python.org/3/library/re.html#re.Match.start)) and end position ([end()](https://docs.python.org/3/library/re.html#re.Match.end)) of the match.

```text title="Output"
<re.Match object; span=(0, 3), match='Mr.'>
0 3
```

### group()

Currently, no group has been specified for `re_mr`:

```python showLineNumbers title="Run"
print(m.groups())
```

* L1: [groups()](https://docs.python.org/3/library/re.html#re.Match.groups)

```text title="Output"
()
```

Let us capture the letters and the period as separate groups:

```python showLineNumbers title="Run"
re_mr = re.compile(r'(M[rs])(\.)')
m = re_mr.match('Ms.')

print(m)
print(m.group())
print(m.groups())
print(m.group(0), m.group(1), m.group(2))
```

* L1: The pattern `re_mr` is looking for the following:
  * 1st group: "M" followed by either "r" or 's'.
  * 2nd group: a period (".")
* L2: Match `re_mr` with the input string "Ms".
* L5: Print the entire matched string ([group()](https://docs.python.org/3/library/re.html#re.Match.group)).
* L6: Print a tuple of all captured groups ([groups()](https://docs.python.org/3/library/re.html#re.Match.groups)).
* L7: Print specific groups by specifying their indexes. Group 0 is the entire match, group 1 is the first capture group, and group 2 is the second capture group.

```text title="Output"
<re.Match object; span=(0, 3), match='Ms.'>
Ms.
('Ms', '.')
Ms. Ms .
```

If the pattern does not find a match, it returns `None`.

```python showLineNumbers title="Run"
m = RE_MR.match('Mrs.')
print(m)
```

```text title="Output"
None
```

### search()

Let us match the following strings with `re_mr`:

```python showLineNumbers title="Run"
s1 = 'Mr. and Ms. Wayne are here'
s2 = 'Here are Mr. and Ms. Wayne'

print(re_mr.match(s1))
print(re_mr.match(s2))
```

```text title="Output"
<re.Match object; span=(0, 3), match='Mr.'>
None
```

`s1` matches "Mr." but not "Ms." while `s2` does not match any pattern. It is because the `match()` function matches patterns only at the beginning of the string. To match patterns anywhere in the string, we need to use `search()` instead:

```python showLineNumbers title="Run"
print(re_mr.search(s1))
print(re_mr.search(s2))
```

* [search()](https://docs.python.org/3/library/re.html#re.Pattern.search)

```text title="Output"
<re.Match object; span=(0, 3), match='Mr.'>
<re.Match object; span=(9, 12), match='Mr.'>
```

### findall()

The `search()` function matches "Mr." in both `s1` and `s2`  but still does not match "Ms.". To match them all, we need to use the `findall()` function:

```python showLineNumbers title="Run"
print(re_mr.findall(s1))
print(re_mr.findall(s2))
```

* [findall()](https://docs.python.org/3/library/re.html?highlight=re#re.findall)

```text title="Output"
[('Mr', '.'), ('Ms', '.')]
[('Mr', '.'), ('Ms', '.')]
```

### finditer()

While the `findall()` function matches all occurrences of the pattern, it does not provide a way to locate the positions of the matched results in the string. To find the locations of the matched results, we need to use the `finditer()` function:

```python showLineNumbers title="Run"
ms = re_mr.finditer(s1)
for m in ms: print(m)

ms = re_mr.finditer(s2)
for m in ms: print(m)
```

* [finditer()](https://docs.python.org/3/library/re.html#re.finditer)

```text title="Output"
<re.Match object; span=(0, 3), match='Mr.'>
<re.Match object; span=(8, 11), match='Ms.'>
<re.Match object; span=(9, 12), match='Mr.'>
<re.Match object; span=(17, 20), match='Ms.'>
```

### sub()

Finally, you can replace the matched results with another string by using the `sub()` function:

```python showLineNumbers title="Run"
print(re_mr.sub('Dr.', 'I met Mr. Wayne and Ms. Kyle.'))
```

* [sub()](https://docs.python.org/3/library/re.html#re.sub)

```text title="Output"
I met Dr. Wayne and Dr. Kyle.
```

## Tokenization

Finally, let us write a simple tokenizer using regular expressions. We will define a regular expression that matches the necessary patterns for tokenization:

```python showLineNumbers
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
```

* L2: Create a regular expression to match delimiters and a special case:
  * Delimiters: `','`, `'.'`, or whitespaces (`'\s+'`).
  * The special case: `'n't'` (e.g., "can't").
* L3: Create an empty list `tokens` to store the resulting tokens, and initialize `prev_idx` to keep track of the previous token's end position.
* L5: Iterate over matches in `text` using the regular expression pattern.
  * L6: Extract the substring between the previous token's end and the current match's start, strip any leading or trailing whitespace, and assign it to `t`.
  * L7: If `t` is not empty (i.e., it is not just whitespace), add it to the `tokens` list.
  * L8: Extract the matched token from the match object strip any leading or trailing whitespace, and assign it to `t`.
  * L10: If `t` is not empty (i.e., the pattern is matched):
    * L11-12: Check if the previous token in `tokens` is "Mr" or "Ms" and the current token is a period ("."), in which case, combine them into a single token.
    * L13-14: Otherwise, add `t` to `tokens`.
* L18-19: After the loop, there might be some text left after the last token. Extract it, strip any leading or trailing whitespace, and add it to `tokens`.

Test cases for the tokenizer:

```python showLineNumbers title="Run"
text = 'Mr. Wayne isn\'t the hero we need, but "the one" we deserve.'
print(tokenize(text))

text = 'Ms. Wayne is "Batgirl" but not "the one".'
print(tokenize(text))
```

```text title="Output"
['Ms.', 'Wayne', 'is', '"', 'Batgirl', '"', 'but', 'not', '"', 'the', 'one', '"']
['Ms.', 'Wayne', 'is', '"', 'Batgirl', '"', 'but', 'not', '"', 'the', 'one', '"', '.']
```

:::warning
**Q10**: What are the benefits and limitations of using **regular expressions** for tokenization vs. the **rule-based tokenization** approach discussed in the [previous section](tokenization)?
:::

## References

1. Source: [regular\_expressions.py](https://github.com/emory-courses/nlp-essentials/blob/main/src/regular_expressions.py)
2. [Regular Expression](https://docs.python.org/3/howto/regex.html), Kuchling, HOWTOs in Python Documentation
