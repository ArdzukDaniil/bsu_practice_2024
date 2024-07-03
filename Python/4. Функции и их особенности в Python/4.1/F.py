printed_strings = set()


def modern_print(string):
    if string not in printed_strings:
        print(string)
        printed_strings.add(string)
