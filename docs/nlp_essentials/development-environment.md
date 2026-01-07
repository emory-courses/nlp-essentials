---
title: Development Environment
---

# Development Environment

This guide will help you set up your **development environment** by installing required tools: Python programming language, GitHub for version control, and PyCharm IDE.

## Python

* Install [Python](https://www.python.org/downloads/) version **3.14.x or higher**. Earlier versions may not be compatible with this course.
* Take some time to familiarize yourself with Python's [new features](https://docs.python.org/3/whatsnew/).

## GitHub

1. Create a [GitHub](https://github.com/) account (if you do not already have one). As a student, you can get [GitHub Pro](https://docs.github.com/en/get-started/learning-about-github/githubs-plans#github-pro) features for free through the [GitHub Student Developer Pack](https://education.github.com/pack).
2. Login to GitHub.
3. Create a new repository named "**nlp-essentials**" and set its visibility to **Private**.

   <img src={require('/img/nlp_essentials/create-repo.png').default} width={550} />

4. Go to `[Settings]` in your repository, and select `[Collaborators]`.
5. Click `[Add people]`, and add each instructor using their GitHub usernames:
   1. Find their GitHub IDs in the "Instructors" section of the [Syllabus](syllabus).
   2. Enter each username and send the collaboration invitation.
6. Verify that all instructors have been added as collaborators.

   <img src={require('/img/nlp_essentials/collaborators.png').default} width={850} />


## PyCharm

1. Install [PyCharm](https://www.jetbrains.com/pycharm/download/) on your local machine:
   1. As a student, you can get [PyCharm Pro](https://www.jetbrains.com/pycharm/editions/) for free by applying for a [JetBrains Educational License](https://www.jetbrains.com/community/education/#students).
   2. The following instructions are based on **PyCharm 2025.3.x**.
2. Configure your GitHub account:
   1. Go to `[Settings] > [Version Control] > [GitHub]`.
   2. Press `[+]`, select `[Log in via GitHub]`, and follow the browser prompts to authorize PyCharm with your GitHub account.
   3. Once connected, you will be able to access GitHub directly from PyCharm for version control operations.

   <img src={require('/img/nlp_essentials/pycharm1.png').default} width={850} />

3. Create a new PyCharm project from GitHub:
   1. On the initial screen, click `[Clone Repository]`.
   2. In the new window, select `[GitHub]` from the left menu, choose your **nlp-essentials** repository, and click `[Clone]` (verify the directory name is "nlp-essentials").
4. Set Up a Python virtual environment:
   1. Go to `[Settings] > [Python] > [Interpreter]`.
   2. Click `[Add Interpreter]` and choose `[Add Local Interpreter]`.
5. In the prompted menu, choose `[Add Local Environment]`, configure as follows, then click `[OK]`:

   <img src={require('/img/nlp_essentials/pycharm2.png').default} width={450} />

   * Environment:  **Generate new**
   * Type: `Virtualenv
   * Base python: the Python version you installed above
   * Location: YOUR_LOCAL_PATH/nlp-essentials/.venv

## References

* [Git](https://docs.github.com/en/get-started/using-git/about-git): a version control system for tracking changes in files.
* [Virtualenv](https://virtualenv.pypa.io): a tool to create isolated Python environment.
