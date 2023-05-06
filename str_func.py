def str_func(string):
    return string.upper()


def capitalize_words(string):
    """new"""
    return ' '.join(word.capitalize() for word in string.split())
