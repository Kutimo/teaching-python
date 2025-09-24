import os

# Read csv file
# Store contents in list


def read_text_file(filename: str) -> list[str]:
    """
    Reads text content of a file and returns it as a list.
    :param filename: The name of the file to read from.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            return [line.strip('\n') for line in f]
    except FileNotFoundError as e:
        print(f"Error in function read_text_file: {e}")
        return []


def parse_csv(filename: str) -> list[dict]:
    file_contents = read_text_file(filename)
    print(file_contents)
    output = []
    errors: list[str] = []

    # Skip header
    # print(list(enumerate(file_contents)))
    for index, line in enumerate(file_contents):
        if index == 0:
            continue

        # Trim leading/trailing whitespace, then split the line on commas
        try:
            # pet_name, race, is_mammal = line.strip().split(',')
            pet_name, race, is_mammal = [item.strip()
                                         for item in line.split(',')]

            bool_is_mammal = parse_bool(is_mammal)
            output.append(
                {
                    'pet_name': pet_name,
                    'race': race,
                    'is_mammal': bool_is_mammal
                })
        except ValueError as e:
            error_message = f"Error in line {index + 1}: {e}. Line content: {line}"
            errors.append(error_message)

    if errors:
        print(f"\nProcessed with {len(errors)} error(s):")
        for error in errors:
            print(error)

    return output


# Validate bool column
def parse_bool(input_str: str, ) -> bool:
    """
    Converts an input string to a boolean based on whether it matches a given 'ja' or 'nei' string.
    :param input_str: The input string to parse.
    :return: True if the input string matches 'ja', False if 'nei'.
    """
    if input_str.lower() == 'yes':
        return True
    elif input_str.lower() == 'no':
        return False
    raise ValueError(
        f"Invalid boolean string: '{input_str}'. Expected 'yes' or 'no'.")


if __name__ == '__main__':
    data = parse_csv('pets.csv')
    print(f"\n{data}")

    # print(data)
