# openaiplayground

The objective of this project is to experiment with OpenAI APIs.

[![Testing](https://github.com/zen-code-symphony/py-basic-scaffold/actions/workflows/test.yml/badge.svg)](https://github.com/zen-code-symphony/py-basic-scaffold/actions/workflows/test.yml)

# Table of Contents
- [Prerequisites](#prerequisites)
  - [Install software](#install-software)
- [Get up and running](#get-up-and-running)
- [Configure VS Code](#configure-vs-code)


## Prerequisites

### Install software
- [git](https://git-scm.com/downloads)
- [pyenv - _optional_](https://github.com/pyenv/pyenv)
- [VS Code - _optional_](https://code.visualstudio.com/download)


## Get up and running

Run the below command to create a project based on this basic scaffold. **NOTE**: It assumes that you have installed Python and configured git. If you are using pyenv, `.python-version` file will be used.

**Option 1**: Create new project from Linux or macOS command shell and stay in the shell:
```sh
# Replace "my_project" with your own project name.
curl -sSL https://raw.githubusercontent.com/zen-code-symphony/openaiplayground/master/create-project.sh | bash -s my_project && cd my_project && source venv/bin/activate
```

**Option 2**: Create new project from Linux or macOS shell and open VS Code editor:
```sh
# Replace "my_project" with your own project name.
curl -sSL https://raw.githubusercontent.com/zen-code-symphony/openaiplayground/master/create-project.sh | bash -s my_project && cd my_project && code .
```

## Config API Key and PYTHONPATH
1. Create a `.env` file in the project root directory.
2. Add `OPENAI_API_KEY=<Your OpenAI secret key>` entry in the file. Replace secret key with your secret key. You can create one at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
3. From terminal, configure the PYTHONPATH:
    ```sh
    export PYTHONPATH="${PYTHONPATH}:./src"
    ```
4. Test if you can run scripts and interact with the OpenAI APIs:
   ```sh
   source venv/bin/activate
   python src/app/principle_clear_and_specific/few_shots.py
   ```

## Configure VS Code
  - As part of VS Code workspace extensions recommendations, the extensions mentioned in [.vscode/extensions.json](./.vscode/extensions.json), should be installed. This includes extensions for flake8, black, isort etc.
  - Make sure that you are using the workspace settings mentioned in repository file [.vscode/settings.json](./.vscode/settings.json). `CTRL+,` and open `Workspace` settings tab to check.
