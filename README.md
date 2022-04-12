# JSON Creator

This CLI takes in a series of inputs and writes them to a JSON file.

# Installation

This version of the CLI is backed by `pipenv`

Download the latest version of `pipenv` from [here](https://pypi.org/project/pipenv/)

Install dependencies:

```
pipenv install && pipenv shell
```

This will install the dependnecies and set up the environment for the CLI.

Download the current version of the CLI:

```bash
pip install -e .
```

This will download `json-cli` and you will now be able to run

```bash
json-cli write --help
```

# Development

The main part of the application begins at the `setup.py` file which shows `pip` installations how to install the CLI. This is followed by the `README.md` file which contains the documentation for the CLI. The `main.py` file is the main file for the CLI. It contains the `cli` function which is the entrypoint for the CLI.

Click uses `decorators` to create a CLI. This is a Python decorator that allows you to create a CLI while click handles the command line arguments.

## Schema for the inputs

```json
{
    "name": "",
    "description": "",
    "version": "",
    "author": "",
    "license": "",
    "posts": [
        {
            "title": "",
            "date": "",
            "content": ""
        }
    ]
}
```



