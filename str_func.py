def str_func(string):
    """upper case"""
    return string.upper()


def capitalize_word(string):
    """:return capitalize word"""
    return ' '.join(word.capitalize() for word in string.split())
