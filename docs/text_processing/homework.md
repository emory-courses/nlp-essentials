---
title: Homework
description: 'HW1: Text Processing'
---

# Homework

## Task 1: Chronicles of Narnia

Your goal is to extract and organize structured information from C.S. Lewis's [Chronicles of Narnia](https://en.wikipedia.org/wiki/The_Chronicles_of_Narnia) series, focusing on book metadata and chapter statistics.

### Data Collection

For each book, gather the following details:

* Book Title (preserve exact spacing as shown in text)
* Year of Publishing (indicated in the title)

For each chapter within every book, collect the following information:

* Chapter Number (as Arabic numeral)
* Chapter Title
* Token Count of the Chapter Content
  * Each word, punctuation mark, and symbol counts as a separate token.
  * Count begins after chapter title and ends at next chapter heading or book end. Do not include chapter number and chapter title in count.

### Implementation

1. Download the [**chronicles\_of\_narnia.txt**](https://github.com/emory-courses/nlp-essentials/blob/main/dat/chronicles_of_narnia.txt) file and place it under the [dat/](https://github.com/emory-courses/nlp-essentials/tree/main/dat) directory.
   * The text file is pre-tokenized using the [ELIT Tokenizer](https://github.com/emorynlp/elit-tokenizer).
   * Each token is separated by whitespace.
2. Create a [**text\_processing.py**](https://github.com/emory-courses/nlp-essentials/blob/main/src/homework/text_processing.py) file in the [src/homework/](https://github.com/emory-courses/nlp-essentials/tree/main/src/homework) directory.
3. Define a function named `chronicles_of_narnia()` that takes a file path pointing to the text file and returns a dictionary structured as follows:
   * Takes a file path pointing to the text file.
   * Returns a dictionary with the structure shown below.
   * Books must be stored as key-value pairs in the main dictionary.
   * Chapters must be stored as lists within each book's dictionary/
   * Chapter lists must be sorted by chapter number in ascending order.

```json
{
  'The Lion , the Witch and the Wardrobe': {
    'title': 'The Lion , the Witch and the Wardrobe',
    'year': 1950,
    'chapters': [
      {
        'number': 1,
        'title': 'Lucy Looks into a Wardrobe',
        'token_count': 1915
      },
      {
        'number': 2,
        'title': 'What Lucy Found There',
        'token_count': 2887
      },
      ...
    ]
  },
  'Prince Caspian : The Return to Narnia': {
    'title': 'Prince Caspian : The Return to Narnia',
    'year': 1951,
    'chapters': [
      ...
    ]
  },
  ...
}
```

## Task 2: Regular Expressions

Define a function named `regular_expressions()` in **src/homework/text\_processing.py** that takes a string and returns one the four types, "email", "date", "url", "cite", or `None` if nothing matches:

### Email

* Format:
  * username@hostname.domain
* Username and Hostname:
  * Can contain letters, numbers, period (`.`), underscore (`_`), hyphen (`-`).
  * Must start and end with letter/number.
* Domain:
  * Limited to `com`, `org`, `edu`, and `gov`.

### Date

* Formats:
  * YYYY/MM/DD or YY/MM/DD
  * YYYY-MM-DD or YY-MM-DD
* Year:
  * 4 digits: between 1951 and 2050
  * 2 digits: for 1951 - 2050
* Month:
  * 1 - 12 (can be with/without leading zero)
* Day:
  * 1 - 31 (can be with/without leading zero)
  * Must be valid for the given month.

### URL

* Format:
  * protocol://address
* Protocol:
  * http or https (only)
* Address:
  * Can contain letters, hyphen, dots.
  * Must start with letter/number.
  * Must include at least one dot.

### Cite

* Formats:
  * Single author: Lastname, YYYY (e.g., Smith, 2023)
  * Two authors: Lastname 1 and Lastname 2, YYYY (e.g., Smith and Jones, 2023)
  * Multiple authors: Lastname 1 et al., YYYY (Smith et al., 2023)
* Lastnames must be capitalized and can have multiple
* Year must be between 1900-2024.

## Submission

Commit and push the **text\_processing.py** file to your GitHub repository.

## Rubric

* Task 1: Chronicles of Narnia (7 points)
* Task 2: Regular Expressions (3 points)
* Concept Quiz (2 points)
