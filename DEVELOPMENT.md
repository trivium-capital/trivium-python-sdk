# Setup

Using venv on MacOs

1. Install venv in host Python:

   `pip install virtualenv`

2. Download desired Python version from homebrew (for e.g. 3.10):

   `brew install python@3.10`

3. Create virtual environment:

   `/opt/homebrew/bin/python3.10 -m venv env`

4. Activate virtual environment:

   `source env/bin/activate`

5. Install dependencies:

   `env/bin/pip3.10 install -r requirements.txt -r test-requirements.txt`

6. Install dependencies to package and upload to PyPi:

   `env/bin/pip3.10 install build twine`

7. Build package for PyPi (generates files in [dist/]() folder):

   `env/bin/python3.10 -m build`

8. To upload package (uploads **all** files in [dist/]()):

   `env/bin/python3.10 -m twine upload dist/*`

8. To switch back to host Python:

   `deactivate`

# Code Generation

1. Update [docs.yaml]() to newest OpenAPI specification.

2. Run `./generate_from_docs.sh`.

3. Fix code example in [README.md]().