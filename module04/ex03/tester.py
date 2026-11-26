from new_student import Student


def main() -> None:
    """Display a freshly created student."""
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
