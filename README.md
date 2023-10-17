<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Project-CodeTSR</h1>
<h3>◦ Unleash your coding potential with CodeTSR!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
</p>
<img src="https://img.shields.io/github/license/Abhijith14/Project-CodeTSR?style&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Abhijith14/Project-CodeTSR?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Abhijith14/Project-CodeTSR?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Abhijith14/Project-CodeTSR?style&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running Project-CodeTSR](#-running-Project-CodeTSR)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project consists of a collection of files that serve various purposes. The SmartGitAuto code provides automation functionalities for the Git client SmartGit, streamlining common Git workflows for developers. The davinci.py file utilizes the OpenAI GPT-3 model to generate text based on a given prompt. The main.py file prompts the AI model to generate a response on a Python hack and posts it on LinkedIn using the LinkedIn API integration provided in the linkedin_api.py file. The project's value proposition lies in its ability to automate Git tasks, generate text using AI, and seamlessly post content on LinkedIn, enhancing productivity and efficiency for developers.

---

## 📦 Features

Exception: 

---


## 📂 Repository Structure

```sh
└── Project-CodeTSR/
    ├── .SmartGitAuto
    ├── .github/
    │   └── workflows/
    ├── LICENSE
    ├── davinci.py
    ├── linkedin_api.py
    └── main.py
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                      |
| [.SmartGitAuto](https://github.com/Abhijith14/Project-CodeTSR/blob/main/.SmartGitAuto)     | The.SmartGitAuto code provides automation functionality for SmartGit, a Git client. It streamlines common Git workflows, including repository cloning, branch creation, commits, and pushes. By automating these tasks, it saves time and improves efficiency for developers using SmartGit.                                                                                             |
| [davinci.py](https://github.com/Abhijith14/Project-CodeTSR/blob/main/davinci.py)           | This code defines a function called'output' that uses the OpenAI GPT-3 model (specifically'text-davinci-003') to generate text based on a given prompt. The function handles the limitation of maximum tokens and adjusts the prompt accordingly. The generated text is returned as output.                                                                                              |
| [main.py](https://github.com/Abhijith14/Project-CodeTSR/blob/main/main.py)                 | The code prompts an AI model to generate a response on an interesting Python hack, and then uses another function to post the generated response on LinkedIn.                                                                                                                                                                                                                            |
| [linkedin_api.py](https://github.com/Abhijith14/Project-CodeTSR/blob/main/linkedin_api.py) | This code is a LinkedIn API integration that allows users to create posts on LinkedIn. It supports both text-only posts and posts with images. The code uses the access token to authenticate the user and sends the necessary data to the API endpoint to create the post. If successful, it prints a success message; otherwise, it prints an error message with the relevant details. |

</details>

<details closed><summary>Workflows</summary>

| File                                                                                           | Summary                                                                                                                                                                                                       |
| ---                                                                                            | ---                                                                                                                                                                                                           |
| [main.yml](https://github.com/Abhijith14/Project-CodeTSR/blob/main/.github/workflows/main.yml) | This GitHub Actions workflow installs Python dependencies, sets up Python 3.10, and runs a Python script called main.py. It also includes the necessary environment variables for LinkedIn and OpenAI tokens. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

1. Clone the Project-CodeTSR repository:
```sh
git clone https://github.com/Abhijith14/Project-CodeTSR
```

2. Change to the project directory:
```sh
cd Project-CodeTSR
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running Project-CodeTSR

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```

---


## 🛣 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  LICENSE-TYPE` License. See the [LICENSE-Type](LICENSE) file for additional info.

---

## 👏 Acknowledgments

`- ℹ️ List any resources, contributors, inspiration, etc.`

[↑ Return](#Top)

---
