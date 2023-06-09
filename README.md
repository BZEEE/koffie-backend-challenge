# Koffie Backend App

## First time setup

### Install Python 3.8

#### OSX

Use [homebrew](https://brew.sh):

```
$ brew install pyenv
$ brew install make
$ pyenv install 3.8.14
```

#### Windows

Go to <https://www.python.org/downloads/windows/> and follow the instructions.

### Install Pipenv

Install `Pipenv` with `pip` (the Python package manager):

```
$ python3 -m pip install --user pipenv # On Windows this may be `python` instead of `python3`
```

Once `pipenv` is installed, you may need to make sure that it is in your `PATH`.
If not, running the command may result in `pipenv: command not found`.

To do this, run the following command:

```
$ PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
$ export PATH="$PYTHON_BIN_PATH:$PATH

```

You'll also want to add this to the bottom of your `~/.bash_profile` so that
it persists across sessions.

### Create and activate a virtual env

```
$ pipenv install
```

### Install the dependencies

```
$ pipenv sync
```

# Running the app

1. start the server by running the command from the root of the project
```
$ make start-server                        # with Make installed on your machine
```
```
$ uvicorn src.server:app --reload          # without Make installed on your machine
```
2. The app is now running on http://localhost:8000

# Viewing the API routes docs/swagger

1. run the app as stated above
2. navigate to http://localhost:8000/docs to view the docs

## Running the end-to-end tests

Use `make test-{local,preprod}` to quickly run the entire test suite for
the desired environment.

Alternatively, to run a specific set of tests (by file, or tag, or other)
or with custom options, use `pytest` directly:

```
pipenv run pytest [options] [tests]
```

Run `pipenv run pytest --help` for all the possible options, or see the
`pytest` documentation.

## Running linters

Running `make lint` will run `black`, `flake8`, and `yamllint`, all of
which help to keep your test code and data bug-free and consistent in style:

```
$ make lint
pipenv sync --dev
Installing dependencies from Pipfile.lock (b104da)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 45/45 — 00:00:06
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
All dependencies are now up-to-date!
pipenv run black --check .
All done! ✨ 🍰 ✨
1 file would be left unchanged.
pipenv run flake8
pipenv run yamllint .

```

# Adding dependencies

This project uses `pipenv` to manage dependencies, so to add new dependencies
use `pipenv install`:

```
$ pipenv install hypothesis
```

Or to pin a specific version:

```
$ pipenv install hypothesis==4.8.0
```


# Directory Structure

The template contains the following files:

```
.
├── Makefile                 # Contains various handy shortcuts.
├── Pipfile                  # The list of dependencies (like pom.xml or package.json).
├── Pipfile.lock             # Dependency lock file (like package-lock.json).
├── README.md
├── local-config.yaml      # Config file with settings for running against Local environment.
├── preprod-config.yaml      # Config file with settings for running against PreProd environment.
├── prod-config.yaml         # Config file with settings for running against Prod environment.
├── pytest.ini               # Various pytest-specific settings.
├── src                      # source code for API functionality
├── apitests                 # pytests and testdata related to                  

