"""
Print the dynamically typed programming languages, using the Programming Language class to determine typing format and
string formatting.

Languages. Created by Malia, April 2021.
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Use the Programming Language class to print dynamically typed programming languages."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
