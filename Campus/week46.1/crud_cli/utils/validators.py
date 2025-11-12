

# A function that gets and validates user input

def get_valid_input(prompt, input_type='str', allow_empty=False):
    try:
        value = input(prompt).strip()

        if input_type == "str":
            if not allow_empty and not value:
                print("Input cannot be empty")
                return None
            return value

        elif input_type == "int":
            return int(value)


    except ValueError:
        print("Invalid input! please enter a valid number" )
        return None

