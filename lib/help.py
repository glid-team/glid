"""
Help related functions
main and subcommand helps
"""


def main():
    """
    Just print out the main help document
    """
    help_file = open('./man/main', 'r')
    main_text = help_file.read()
    print main_text
    help_file.close()
