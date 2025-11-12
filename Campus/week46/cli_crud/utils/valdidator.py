def get_valid_input(prompt, input_type='str', allow_empty=False):
    """
    Get and validate user input.

    Args:
        prompt: Input prompt message
        input_type: Expected type ('str' or 'int')
        allow_empty: Allow empty strings

    Returns:
        Valid input or None if invalid
    """
    try:
        value = input(prompt).strip()

        if input_type == 'str':
            if not allow_empty and not value:
                print("Input cannot be empty!")
                return None
            return value

        elif input_type == 'int':
            return int(value)

    except ValueError:
        print("Invalid input! Please enter a valid number")
        return None