def capitalize_words(input_str: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence.

    :param sentence: string to capitalize
    :return: capitalized string
    """
    return " ".join([word.capitalize() for word in input_str.split()])
