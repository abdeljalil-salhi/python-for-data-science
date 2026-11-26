# Python for Data Science

[![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-310/)
[![subject tests](https://img.shields.io/github/actions/workflow/status/abdeljalil-salhi/python-for-data-science/subject-tests.yml?branch=main&style=flat-square&label=subject%20tests)](https://github.com/abdeljalil-salhi/python-for-data-science/actions/workflows/subject-tests.yml)

Solutions for the **Piscine Python for Data Science** modules 00–04. Each
module contains its original `en.subject.pdf`, which is the source of truth,
plus one directory per exercise.

The code follows the conventions used throughout the repository: explicit
imports, no global state, docstrings on functions and classes, and 
flake8-clean style.

## Modules

### [module00](module00/) — Starting

- [`ex00`](module00/ex00/) — First python script
- [`ex01`](module00/ex01/) — First use of package
- [`ex02`](module00/ex02/) — First function python
- [`ex03`](module00/ex03/) — NULL not found
- [`ex04`](module00/ex04/) — The Even and the Odd
- [`ex05`](module00/ex05/) — First standalone program python
- [`ex06`](module00/ex06/) — filter
- [`ex07`](module00/ex07/) — Dictionaries SoS
- [`ex08`](module00/ex08/) — Loading...
- [`ex09`](module00/ex09/) — My first package creation

### [module01](module01/) — Array

- [`ex00`](module01/ex00/) — Give my BMI
- [`ex01`](module01/ex01/) — 2D array
- [`ex02`](module01/ex02/) — load my image
- [`ex03`](module01/ex03/) — zoom on me
- [`ex04`](module01/ex04/) — rotate me
- [`ex05`](module01/ex05/) — Pimp my image

### [module02](module02/) — DataTable

- [`ex00`](module02/ex00/) — Load my Dataset
- [`ex01`](module02/ex01/) — draw my country
- [`ex02`](module02/ex02/) — compare my country
- [`ex03`](module02/ex03/) — draw my year

### [module03](module03/) — Oriented Object Programming

- [`ex00`](module03/ex00/) — GOT S1E9
- [`ex01`](module03/ex01/) — GOT S1E7
- [`ex02`](module03/ex02/) — Now it's weird!
- [`ex03`](module03/ex03/) — Calculate my vector
- [`ex04`](module03/ex04/) — Calculate my dot product

### [module04](module04/) — Data Oriented Design

- [`ex00`](module04/ex00/) — Calculate my statistics
- [`ex01`](module04/ex01/) — Outer_inner
- [`ex02`](module04/ex02/) — my first decorating
- [`ex03`](module04/ex03/) — data class

## Requirements

The subjects target **Python 3.10**. The main third-party dependencies are:

- `numpy`
- `pandas`
- `matplotlib`
- `pillow`
- `tqdm`
- `build` / `setuptools` / `wheel` for the sample package
- `flake8` for linting

They are listed in [`requirements-ci.txt`](requirements-ci.txt), which is used
by CI and can also be used locally.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-ci.txt
```

## Running an exercise

Run the provided tester from inside its exercise directory:

```bash
cd module04/ex00
python tester.py
```

Where no tester is provided, run the script named in the subject, for example:

```bash
cd module00/ex00
python Hello.py
```

`module00/ex08/tester.py` compares three progress bars in one run:
`ft_tqdm`, the original `tqdm`, and the timed `ft_tqdm_bonus` variant.

The sample package in `module00/ex09` can be built with:

```bash
cd module00/ex09
python -m build
```

## Validation

From the repository root:

```bash
python -m flake8 module00 module01 module02 module03 module04 tests --max-line-length=79
python tests/subject_checks.py
```

`tests/subject_checks.py` runs every exercise tester and compares its output
with the corresponding subject PDF. It uses exact comparisons where output is
deterministic and normalizes only genuinely variable values such as:

- set iteration order,
- function memory addresses,
- random student IDs,
- progress-bar speed and ETA.

Plotting is forced to the non-interactive `Agg` backend, and `PIL.Image.show()`
is patched during checks so the suite also works on headless machines.

## CI

[`.github/workflows/subject-tests.yml`](.github/workflows/subject-tests.yml)
runs the lint and subject-output checks with Python 3.10:

- on every `pull_request`,
- on `push` only for `main`.

Python 3.10 is pinned because the built-in `filter.__doc__` text differs on
newer interpreters, and one exercise explicitly compares against it.
