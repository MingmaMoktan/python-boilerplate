# Python Boilerplate

This is a boilerplate for Python (3.9+) projects that contain both documentation generation (utilizing `pdoc`), and unit test generation (utilizing `pytest` and `pytest-cov` for code coverage). The project includes pre-made scripts and template code. Example docstrings are created using the Google-style Python docstring convention.

## Requirements

The following packages should be installed:

- pytest (`pip3 install pytest`)
- pytest-cov (`pip3 install pytest-cov`)
- pdoc  (`pip3 install pdoc`)

## Project Structure

The project contains the following structure:
- `src/`: Contains all source code of the project.
- `tests/`: There are generally two ways to load the test files; Alongside the source code, or in a separate folder. The second approach, where one tests folder is used, is used in this boilerplate. All test files are being mirrored in the same folder structure as the source code.

## Scripts

The project contains the following scripts:
- `run_app`: Runs the application. The main entry point is at `src/main.py`.
- `run_tests`: Runs the tests contained in the `tests/` folder.
- `create_pdoc`: Creates documentation of the `src/` folder. The documentation is outputted as an HTML document in folder `docs`.

## Configuration Files

- `.coveragerc`: Contains the configurations for the code coverage package (`pytest-cov`).
- `conftest.py`: Contains the configurations for the `pytest` package.