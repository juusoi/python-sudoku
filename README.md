# Sudoku Checker

This is a Python project that provides a Sudoku checker utility. It allows you to verify the validity of a Sudoku board.

## Background

Sudoku is a logic-based number placement puzzle that is played on a 9x9 grid. The goal of the puzzle is to fill in the grid with digits from 1 to 9 so that each row, column, and 3x3 subgrid contains the digits 1-9 exactly once. The puzzle typically starts with some digits already filled in, which serve as clues to help the player solve the puzzle. Sudoku puzzles can range in difficulty from very easy to extremely challenging, and they have become a popular pastime around the world.

## Project Structure

The project is structured as follows:

```
sudoku-checker/
├── src/
│ ├── main.py
│ ├── sudoku_checker.py
│ └── tests/
│     └── test_sudoku_checker.py
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── README.md
├── requirements-dev.txt
```

The src directory contains the source code for the project. The sudoku_checker.py file contains the implementation of the Sudoku checker functions. The tests directory contains unit tests for the Sudoku checker functions.

The .gitignore file specifies files and directories that should be ignored by Git. The .pre-commit-config.yaml file specifies pre-commit hooks that are run before each commit to perform code formatting and linting. This helps ensure that the codebase is consistent and adheres to a set of coding standards. The LICENSE file contains the terms under which the code can be used and distributed. The README.md file contains an introduction to the project and instructions for getting started. The requirements-dev.txt file lists the dependencies required to run the project.

## Installation

1. Clone the repository:

```
git clone https://github.com/juusoi/python-sudoku
```

2. Create and activate a virtual environment (venv):

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements-dev.txt
```

## Usage

### Using the Sudoku Checker Utility

The Sudoku checker can be used by importing the `is_valid_sudoku()` function from the `sudoku_checker` module. Here's an example of how to use it:

```python
from sudoku_checker import is_valid_sudoku

# Create a Sudoku board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "."],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Check the validity of the Sudoku board
valid = is_valid_sudoku(board)
if valid:
    print("The Sudoku board is valid.")
else:
    print("The Sudoku board is invalid.")
```

### Running the Example Script

The project also includes an example script (`src/main.py`) that demonstrates the usage of the Sudoku checker utility. To run the example script, execute the following command:

```
python src/main.py
```

The script provides an example Sudoku board and checks its validity using the `is_valid_sudoku()` function from the `sudoku_checker` module.

## Development

1. Install pre-commit hooks:

```
pre-commit install
```

This will set up pre-commit hooks that run before each commit to perform code formatting and linting.

2. Run the unit tests:

```
pytest
```

This will execute the unit tests located in the `src/tests` directory and ensure that the Sudoku checker functions correctly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
