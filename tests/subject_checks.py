"""Run every exercise tester and compare its output with the subject PDFs."""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def repository_root():
    """Return the repository root directory."""
    return Path(__file__).resolve().parents[1]


def normalise(text):
    """Return meaningful lines with consistent line endings."""
    return [line.rstrip() for line in text.replace("\r", "\n").splitlines()]


def run(command, directory, stdin=None, env=None):
    """Run a command in a directory and capture its output."""
    environment = os.environ.copy()
    environment["MPLBACKEND"] = "Agg"
    if env:
        environment.update(env)
    return subprocess.run(
        command,
        cwd=str(directory),
        input=stdin,
        text=True,
        capture_output=True,
        env=environment,
    )


def script(name, directory, *arguments, stdin=None, patch_show=False):
    """Run an exercise script with optional PIL show() patching."""
    if patch_show:
        command = [
            sys.executable,
            "-c",
            "import runpy; from PIL import Image; "
            "Image.Image.show = lambda self, *a, **k: None; "
            "runpy.run_path(" + repr(name) + ", run_name='__main__')",
        ]
    else:
        command = [sys.executable, name, *arguments]
    return run(command, directory, stdin=stdin)


class Checks:
    """Collect output comparison failures."""

    def __init__(self):
        """Initialise an empty failure list."""
        self.failures = []

    def exact(self, name, actual, expected):
        """Compare two blocks of output line by line."""
        actual_lines = normalise(actual)
        expected_lines = normalise(expected)
        if actual_lines != expected_lines:
            self.failures.append(
                f"{name}\n  expected: {expected_lines}\n"
                f"  actual:   {actual_lines}"
            )

    def contains(self, name, text, fragment):
        """Require a fragment to appear in output."""
        if fragment not in text:
            self.failures.append(f"{name}\n  missing: {fragment!r}")

    def pattern(self, name, text, expression):
        """Require a regular expression to match output."""
        if re.search(expression, text, re.MULTILINE) is None:
            self.failures.append(
                f"{name}\n  pattern: {expression}\n"
                f"  actual: {text!r}"
            )

    def report(self):
        """Print all failures and return the process exit status."""
        if not self.failures:
            print("All subject output checks passed.")
            return 0
        for failure in self.failures:
            print(f"FAIL: {failure}")
        print(f"{len(self.failures)} check(s) failed.")
        return 1


def check_package(checks):
    """Build and smoke-test the module 00 package."""
    base = repository_root() / "module00" / "ex09"
    with tempfile.TemporaryDirectory() as temporary:
        build = run(
            [sys.executable, "-m", "build", "--outdir", temporary], base
        )
        if build.returncode != 0:
            checks.failures.append(f"00/ex09 build failed:\n{build.stderr}")
            return

        wheels = list(Path(temporary).glob("*.whl"))
        if len(wheels) != 1:
            checks.failures.append(
                f"00/ex09 expected one wheel, found {len(wheels)}"
            )
            return

        site = Path(temporary) / "site"
        install = run(
            [
                sys.executable, "-m", "pip", "install", "--quiet",
                "--no-deps", "--target", str(site), str(wheels[0]),
            ],
            base,
        )
        if install.returncode != 0:
            checks.failures.append(
                "00/ex09 install failed:\n" + install.stderr
            )
            return

        environment = {"PYTHONPATH": str(site)}
        smoke = run(
            [
                sys.executable, "-c",
                "from ft_package import count_in_list; "
                "print(count_in_list(['toto', 'tata', 'toto'], 'toto'), "
                "count_in_list(['toto', 'tata', 'toto'], 'tutu'))",
            ],
            base,
            env=environment,
        )
        checks.exact("00/ex09 count_in_list", smoke.stdout, "2 0\n")

        show = run(
            [sys.executable, "-m", "pip", "show", "-v", "ft_package"],
            base,
            env=environment,
        )
        for fragment in (
            "Name: ft_package",
            "Version: 0.0.1",
            "Summary: A sample test package",
            "License: MIT",
            "Home-page:",
        ):
            checks.contains(f"00/ex09 pip show {fragment}", show.stdout,
                            fragment)


def check_module00(checks):
    """Check module 00 exercises against the subject."""
    base = repository_root() / "module00"

    result = script("Hello.py", base / "ex00")
    checks.contains(
        "00/ex00 Hello.py list", result.stdout, "['Hello', 'World!']"
    )
    checks.contains(
        "00/ex00 Hello.py tuple", result.stdout, "('Hello', 'Morocco!')"
    )
    checks.pattern(
        "00/ex00 Hello.py set",
        result.stdout,
        r"\{(?:'Hello', 'BenGuerir!'|'BenGuerir!', 'Hello')\}",
    )
    checks.contains(
        "00/ex00 Hello.py dict",
        result.stdout,
        "{'Hello': '1337BenGuerir!'}",
    )

    result = script("format_ft_time.py", base / "ex01")
    checks.pattern(
        "00/ex01 timestamp",
        result.stdout,
        r"Seconds since January 1, 1970: [\d,]+\.\d{4} or "
        r"\d+\.\d{2}e\+\d{2} in scientific notation",
    )
    checks.pattern(
        "00/ex01 date", result.stdout, r"^[A-Z][a-z]{2} \d{2} \d{4}$"
    )

    result = script("tester.py", base / "ex02")
    checks.exact(
        "00/ex02 tester.py",
        result.stdout,
        """List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
""",
    )

    result = script("tester.py", base / "ex03")
    checks.exact(
        "00/ex03 tester.py",
        result.stdout,
        """Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
""",
    )

    cases = (
        (("14",), "I'm Even.\n", ""),
        (("-5",), "I'm Odd.\n", ""),
        ((), "", ""),
        (("0",), "I'm Even.\n", ""),
        (("Hi!",), "", "AssertionError: argument is not an integer\n"),
        (
            ("13", "5"),
            "",
            "AssertionError: more than one argument is provided\n",
        ),
    )
    for arguments, expected_out, expected_err in cases:
        result = script("whatis.py", base / "ex04", *arguments)
        label = f"00/ex04 whatis.py {arguments}"
        checks.exact(f"{label} stdout", result.stdout, expected_out)
        checks.exact(f"{label} stderr", result.stderr, expected_err)

    long_text = (
        "Python 3.0, released in 2008, was a major revision that is not "
        "completely backward compatible with earlier versions. Python 2 "
        "was discontinued with version 2.7.18 in 2020."
    )
    expected_long = """The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
"""
    expected_short = """What is the text to count?
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
"""
    result = script("building.py", base / "ex05", long_text)
    checks.exact("00/ex05 argument", result.stdout, expected_long)
    result = script("building.py", base / "ex05", stdin="Hello World!\n")
    checks.exact("00/ex05 stdin", result.stdout, expected_short)
    result = script("building.py", base / "ex05", stdin="")
    checks.exact(
        "00/ex05 EOF",
        result.stdout,
        """What is the text to count?
The text contains 0 characters:
0 upper letters
0 lower letters
0 punctuation marks
0 spaces
0 digits
""",
    )

    result = script("filterstring.py", base / "ex06", "Hello the World", "4")
    checks.exact("00/ex06 filterstring", result.stdout, "['Hello', 'World']\n")
    result = script("filterstring.py", base / "ex06", "Hello the World", "99")
    checks.exact("00/ex06 empty filter", result.stdout, "[]\n")
    for arguments in (("3", "Hello the World"), ()):
        result = script("filterstring.py", base / "ex06", *arguments)
        checks.exact(
            f"00/ex06 bad arguments {arguments}",
            result.stderr,
            "AssertionError: the arguments are bad\n",
        )
    result = run(
        [
            sys.executable, "-c",
            "from ft_filter import ft_filter; "
            "print(ft_filter.__doc__); "
            "print(ft_filter.__doc__ == filter.__doc__); "
            "print(list(ft_filter(lambda x: x > 2, [1, 2, 3, 4])))",
        ],
        base / "ex06",
    )
    output = result.stdout.splitlines()
    doc_line = output[0] if output else ""
    equality_line = output[-2] if len(output) >= 2 else ""
    filter_line = output[-1] if output else ""
    checks.contains(
        "00/ex06 ft_filter docstring",
        doc_line,
        "filter(function or None, iterable) --> filter object",
    )
    if sys.version_info < (3, 12):
        checks.exact(
            "00/ex06 filter.__doc__ equality",
            equality_line + "\n",
            "True\n",
        )
    checks.exact("00/ex06 ft_filter", filter_line + "\n", "[3, 4]\n")

    result = script("sos.py", base / "ex07", "sos")
    checks.exact("00/ex07 sos", result.stdout, "... --- ...\n")
    result = script("sos.py", base / "ex07", "h$llo")
    checks.exact(
        "00/ex07 bad argument",
        result.stderr,
        "AssertionError: the arguments are bad\n",
    )

    result = script("tester.py", base / "ex08")
    lines = [
        line for line in result.stdout.replace("\r", "\n").splitlines()
        if line.startswith("---") or line.startswith("100%")
    ]
    expected_lines = (
        r"--- ft_tqdm ---",
        r"100%\|=+>\| 333/333",
        r"--- tqdm ---",
        r"100%\|█+\| 333/333 \[\d{2}:\d{2}<\d{2}:\d{2}, [\d.]+it/s\]",
        r"--- ft_tqdm_bonus ---",
        r"100%\|█+\| 333/333 \[\d{2}:\d{2}<\d{2}:\d{2}, [\d.]+it/s\]",
    )
    checks.exact(
        "00/ex08 number of progress lines", str(len(lines)), "6\n"
    )
    for index, expression in enumerate(expected_lines):
        line = lines[index] if index < len(lines) else ""
        checks.pattern(f"00/ex08 progress line {index}", line, expression)

    check_package(checks)


def check_module01(checks):
    """Check module 01 exercises against the subject."""
    base = repository_root() / "module01"

    result = script("tester.py", base / "ex00")
    checks.exact(
        "01/ex00 tester.py",
        result.stdout,
        """[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
""",
    )

    result = script("tester.py", base / "ex01")
    checks.exact(
        "01/ex01 tester.py",
        result.stdout,
        """My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
""",
    )

    result = script("tester.py", base / "ex02")
    checks.pattern(
        "01/ex02 shape",
        result.stdout,
        r"The shape of image is: \(257, 450, 3\)",
    )
    checks.contains("01/ex02 pixels", result.stdout, "[[[19 42 83]")

    result = script("zoom.py", base / "ex03")
    checks.pattern(
        "01/ex03 original shape",
        result.stdout,
        r"The shape of image is: \(768, 1024, 3\)",
    )
    checks.contains(
        "01/ex03 zoomed shape",
        result.stdout,
        "New shape after slicing: (400, 400, 1)",
    )

    result = script("rotate.py", base / "ex04")
    checks.contains(
        "01/ex04 cropped shape",
        result.stdout,
        "The shape of image is: (400, 400)",
    )
    checks.contains(
        "01/ex04 transposed shape",
        result.stdout,
        "New shape after Transpose: (400, 400)",
    )

    result = script("tester.py", base / "ex05", patch_show=True)
    checks.pattern(
        "01/ex05 shape",
        result.stdout,
        r"The shape of image is: \(257, 450, 3\)",
    )
    checks.contains(
        "01/ex05 docstring",
        result.stdout,
        "Inverts the color of the image received.",
    )


def check_module02(checks):
    """Check module 02 exercises against the subject."""
    base = repository_root() / "module02"

    result = script("tester.py", base / "ex00")
    checks.contains(
        "02/ex00 dimensions",
        result.stdout,
        "Loading dataset of dimensions (195, 302)",
    )
    checks.contains("02/ex00 None", result.stdout, "None")
    checks.contains(
        "02/ex00 error",
        result.stderr,
        "Error: File 'invalid_file.csv' not found.",
    )

    result = script("aff_life.py", base / "ex01")
    checks.pattern(
        "02/ex01 dimensions",
        result.stdout,
        r"Loading dataset of dimensions \(195, 302\)",
    )

    result = script("aff_pop.py", base / "ex02")
    checks.pattern(
        "02/ex02 dimensions",
        result.stdout,
        r"Loading dataset of dimensions \(197, 302\)",
    )

    result = script("projection_life.py", base / "ex03")
    checks.pattern(
        "02/ex03 gdp dimensions",
        result.stdout,
        r"Loading dataset of dimensions \(195, 252\)",
    )
    checks.pattern(
        "02/ex03 life dimensions",
        result.stdout,
        r"Loading dataset of dimensions \(195, 302\)",
    )
    checks.contains(
        "02/ex03 countries",
        result.stdout,
        "Number of countries with data in 1900: 186",
    )


def check_module03(checks):
    """Check module 03 exercises against the subject."""
    base = repository_root() / "module03"

    result = script("tester.py", base / "ex00")
    for fragment in (
        "{'first_name': 'Ned', 'is_alive': True}",
        "False",
        "---",
        "{'first_name': 'Lyanna', 'is_alive': False}",
    ):
        checks.contains(f"03/ex00 {fragment}", result.stdout, fragment)
    result = run(
        [
            sys.executable, "-c",
            "from S1E9 import Character; Character('hodor')",
        ],
        base / "ex00",
    )
    checks.contains(
        "03/ex00 abstract",
        result.stderr,
        "Can't instantiate abstract class Character",
    )

    result = script("tester.py", base / "ex01")
    for fragment in (
        "{'first_name': 'Robert', 'is_alive': True, 'family_name': "
        "'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}",
        "<bound method Baratheon.__str__ of Vector: "
        "('Baratheon', 'brown', 'dark')>",
        "<bound method Baratheon.__repr__ of Vector: "
        "('Baratheon', 'brown', 'dark')>",
        "'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'",
        "Name : ('Jaine', 'Lannister'), Alive : True",
    ):
        checks.contains(f"03/ex01 {fragment}", result.stdout, fragment)

    result = script("tester.py", base / "ex02")
    checks.exact(
        "03/ex02 tester.py",
        result.stdout,
        "{'first_name': 'Joffrey', 'is_alive': True, 'family_name': "
        "'Baratheon', 'eyes': 'brown', 'hair': 'dark'}\n"
        "blue\n"
        "light\n"
        "{'first_name': 'Joffrey', 'is_alive': True, 'family_name': "
        "'Baratheon', 'eyes': 'blue', 'hairs': 'light'}\n",
    )

    result = script("tester.py", base / "ex03")
    checks.exact(
        "03/ex03 tester.py",
        result.stdout,
        """[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
""",
    )

    result = script("tester.py", base / "ex04")
    checks.exact(
        "03/ex04 tester.py",
        result.stdout,
        """Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
""",
    )


def check_module04(checks):
    """Check module 04 exercises against the subject."""
    base = repository_root() / "module04"

    result = script("tester.py", base / "ex00")
    checks.exact(
        "04/ex00 tester.py",
        result.stdout,
        """mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
""",
    )

    result = script("tester.py", base / "ex01")
    checks.exact(
        "04/ex01 tester.py",
        result.stdout,
        """9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
""",
    )

    result = script("tester.py", base / "ex02")
    stable = re.sub(r"0x[0-9a-fA-F]+", "0xADDR", result.stdout)
    checks.exact(
        "04/ex02 tester.py",
        stable,
        """f()
g()
f()
Error: <function g at 0xADDR> call too many times
f()
Error: <function g at 0xADDR> call too many times
""",
    )

    result = script("tester.py", base / "ex03")
    stable = re.sub(r"id='[a-z]{15}'", "id='RANDOMID'", result.stdout)
    checks.exact(
        "04/ex03 tester.py",
        stable,
        "Student(name='Edward', surname='agle', active=True, "
        "login='Eagle', id='RANDOMID')\n",
    )

    result = script("tester_error.py", base / "ex03")
    checks.exact(
        "04/ex03 tester_error.py",
        result.stdout,
        "TypeError: Student.__init__() got an unexpected keyword "
        "argument 'id'\n",
    )


def main():
    """Run every subject check and exit with the result."""
    checks = Checks()
    check_module00(checks)
    check_module01(checks)
    check_module02(checks)
    check_module03(checks)
    check_module04(checks)
    sys.exit(checks.report())


if __name__ == "__main__":
    main()
