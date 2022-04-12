# JSON Creator

This CLI takes in a series of inputs and writes them to a JSON file.

# Installation

This version of the cli is created using `pip` and a virtual environment.

We like to use `pyenv` for the virtual environment. You can install it with `brew install pyenv` or `apt-get install python-pyenv`.


```bash
$ pyenv install 3.8.3 
```

Use the 3.8.3 version of Python.

```bash
pyenv virtualenv --copies 3.8.3 json-creator-pip
```

This will create a virtual environment inside this folder. `pyenv` stores these as shims and then links them to the actual Python version.

```bash
pyenv shell json-creator-pip
```

This will set the virtual environment as the current one. You can now install packages inside the virtual environment.

```bash
$ pip install -r requirements.txt
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



