# ft_package

A sample test package created for Python piscine.

## Building the Package

(Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required build tools:

```bash
pip install -r requirements.txt
```

Build the package:

```bash
python -m build
```

You should now see:

```
dist/
├── ft_package-0.0.1-py3-none-any.whl
└── ft_package-0.0.1.tar.gz
```

## Installation

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
