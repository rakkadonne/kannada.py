# Kannada-to-Python Mappings

This project provides a dictionary that maps Kannada keywords to their equivalent Python syntax. The goal is to allow writing Python code using Kannada constructs.

---

## Features

- **Kannada Syntax**: Write Python logic with Kannada keywords.

---

## Keyword Mappings

### 🔹 Boolean & None
| Kannada | Python |
|---------|--------|
| ಸರಿ     | `True` |
| ತಪ್ಪು    | `False` |
| ಏನಿಲ್ಲ   | `None` |

### 🔹 Logical Operators
| Kannada | Python |
|---------|--------|
| ಮತ್ತೆ    | `and` |
| ಇಲ್ಲಾ   | `or`  |
| ಅಲ್ಲ     | `not` |

### 🔹 Conditional Statements
| Kannada   | Python |
|-----------|--------|
| ಆದರೆ     | `if`   |
| ಇಲ್ಲಂದ್ರೆ  | `elif` |
| ಇಲ್ಲವೇ    | `else` |

### 🔹 Looping Constructs
| Kannada     | Python   |
|-------------|----------|
| ಮಾಡ್ಕೊತಿರು   | `for`     |
| ಇರೋವರೆಗೂ    | `while`   |
| ನಿಲ್ಲು       | `break`   |
| ಮುಂದುವರೆ    | `continue`|
| ಬಿಡು        | `pass`    |

### 🔹 Functions and Lambdas
| Kannada     | Python   |
|-------------|----------|
| ದಗದ         | `def`     |
| ಕಳಿಸು        | `return`  |
| ಹೆಸರಿಲ್ಲದ     | `lambda`  |

### 🔹 Exception Handling
| Kannada      | Python     |
|--------------|------------|
| ಮಾಡು         | `try`       |
| ಆಗದಿದ್ದರೆ     | `except`    |
| ಕೊನೆಗೆ        | `finally`   |
| ಅಡ್ಡಿಮಾಡು     | `raise`     |
| ಮತ್ತೆನೋಡು     | `assert`    |

### 🔹 Importing Modules
| Kannada | Python   |
|---------|----------|
| ತಗೋ     | `import` |
| ಇಂದ     | `from`   |
| ಹಾಗೆ     | `as`     |

### 🔹 Scope and Memory
| Kannada     | Python     |
|-------------|------------|
| ಎಲ್ಲಿಯ       | `global`    |
| ಇಲ್ಲಿಯ       | `nonlocal`  |
| ಕಿತ್ತು        | `del`       |

### 🔹 Classes & Async
| Kannada     | Python     |
|-------------|------------|
| ದಾರಿಗೆ       | `class`     |
| ಕೂಡ         | `with`      |
| ಅಡ್ಡಿಮಾಡದೆ   | `async`     |
| ಅಲ್ಲಿವರೆಗೂ   | `await`     |

### 🔹 Other Keywords
| Kannada | Python |
|---------|--------|
| ಒಳಗೆ    | `in`   |
| ಇದ್ದು     | `is`   |
| ಇಳುವು    | `yield`|

### 🔹 Built-in Functions
| Kannada     | Python     |
|-------------|------------|
| ಇದಿಷ್ಟು     | `range`     |
| ಹೇಳು       | `print`     |
| ಕೊಡು        | `input`     |

---

### How to Write Python in Kannada:

1. Download `kannada.py` or clone the repo at [kannada.py](https://github.com/rakkadonne/kannada.py).
2. Write Kannada Python code using the Kannada dictionary as a manual.
3. Save the file with a `.kaypy` extension.
4. Run the command:

   ```bash
   python <path_to_kannada.py> <path_to_.kaypy_file>
---

### Some Important Details

1. Can **create modules in Kannada Python** and import them in other `.kaypy` files.

2. Can **import from standard or custom Python modules** as usual — the tool does not block or interfere with native imports.

3. This **only replaces Python keywords and native functions**, and does **not touch the namespace** of other classes, methods, or modules, ensuring compatibility with external libraries (from pip) or custom codebases. So, you can use Latin characters for variables, built-in modules, or if you wish, the original keyword also (it would still be valid).
