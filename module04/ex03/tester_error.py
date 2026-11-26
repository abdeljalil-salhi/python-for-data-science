from new_student import Student


def main() -> None:
    """Show that generated fields cannot be initialised."""
    try:
        Student(name="Edward", surname="agle", id="toto")
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
