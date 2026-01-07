---
title: Homework
description: 'HW0: Getting Started'
---

# Homework

## Task 1: Getting Started

In this assignment, you will:

1. Set up your development environment,
2. Install your first Python package using pip within a virtual environment,
3. Run a test program to verify the installation and environment configuration, and
4. Commit your changes and push them to your GitHub repository.

This will ensure your development workspace is properly configured for this course.

### Package Installation

Once you set up the [development environment](development-environment):

1. Open Terminal in PyCharm:
   1. Click the Terminal icon at the bottom left, or
   2. Select the `[View] > [Tool Windows] > [Terminal]` menu).
2. Update [pip](https://pypi.org/project/pip/) to the latest version (if necessary):

   ```bash
   python -m pip install --upgrade pip
   ```

3. Install [setuptools](https://pypi.org/project/setuptools/) (if necessary):

   ```bash
   pip install setuptools
   ```

4. Install the [ELIT Tokenizer](https://github.com/emorynlp/elit-tokenizer):

   ```bash
   pip install elit_tokenizer
   ```

5. You will know the installation is successful when you see "_Successfully installed ..._" messages for each package in the terminal output.

### Test Program

1. Create the project structure:
   1. Create a new Python package called `src` in your **nlp-essentials** directory.
   2. Inside `src`, create a `homework` package.
   3. PyCharm will automatically create **\_\_init\_\_.py** files in both directories to mark them as Python packages.
2. Create your first program:

   1. Create a Python file called **getting\_started.py** inside `homework`.
   2. Copy the following code into the file:

   ```python showLineNumbers
   from elit_tokenizer import EnglishTokenizer

   if __name__ == '__main__':
       text = 'Emory NLP is a research lab in Atlanta, GA. It was founded by Jinho D. Choi in 2014. Dr. Choi is a professor at Emory University.'
       tokenizer = EnglishTokenizer()
       sentence = tokenizer.decode(text)
       print(sentence.tokens)
       print(sentence.offsets)
   ```

3. Run the program:

   1. Choose the `[Run] > [Run 'getting_started']` menu, or
   2. Use the green run button next to the main block.

   ![Run the program](/img/nlp_essentials/pycharm3.png)

4. Verify the output; your program is working correctly if you see this output:

   ```
   ['Emory', 'NLP', 'is', 'a', 'research', 'lab', 'in', 'Atlanta', ',', 'GA', '.', 'It', 'was', 'founded', 'by', 'Jinho', 'D.', 'Choi', 'in', '2014', '.', 'Dr.', 'Choi', 'is', 'a', 'professor', 'at', 'Emory', 'University', '.']
   [(0, 5), (6, 9), (10, 12), (13, 14), (15, 23), (24, 27), (28, 30), (31, 38), (38, 39), (40, 42), (42, 43), (44, 46), (47, 50), (51, 58), (59, 61), (62, 67), (68, 70), (71, 75), (76, 78), (79, 83), (83, 84), (85, 88), (89, 93), (94, 96), (97, 98), (99, 108), (109, 111), (112, 117), (118, 128), (128, 129)]
   ```

### Commit & Push

1. Create a [**.gitignore**](https://github.com/emory-courses/nlp-essentials/blob/main/.gitignore) file:

   1. Create the file in your **nlp-essentials** root directory
   2. Add the following lines to exclude unnecessary files:

   ```bash
   .idea/
   .venv/
   ```

2. Stage your files for commit:
   1. Add the following files to Git by right-clicking them and selecting `[Git] > [Add]`:

      ```
      .gitignore
      src/__init__.py
      src/homework/__init__.py
      src/homework/getting_started.py
      ```

   2. Files should turn green when successfully added. If files do not change color, restart PyCharm and try again.

3. Commit and push your changes:
   1. Right-click the **nlp-essentials** directory.
   2. Select `[Git] > [Commit Directory]`.
   3. Write a descriptive commit message (e.g., "Initial setup and tokenizer test")
   4. Click `[Commit and Push]` (not just `Commit`)
   5. Click `[Push]` in the next dialog to upload to your GitHub repository.

4. Verify your submission:
   1. Visit your GitHub repository in a web browser.
   2. Confirm that all files are properly present and contain the correct content.

### Submission

Submit the URL of your GitHub repository to Canvas.

## Task 2: Project Ideas

Share your team project concept by filling out the form in Canvas (about 100-150 words). Your description will be posted on the Project Ideas page to help classmates discover shared interests and form teams.

## Rubric

* **GitHub Setup** (0.2 points):
  * Private repository created.
  * All instructors added as collaborators.
* **Project Organization** (0.2 points):
  * Correct directory structure.
  * No unnecessary files committed
* **Version Control** (0.3 points):
  * All required files committed and successfully pushed to GitHub.
  * Content of the files are correct.
* **Code Implementation** (0.3 points):
  * The program executes without errors.
  * Produces correct tokenizer output.
* **Project Ideas** (1 point)
  * Is the team project idea well described?
