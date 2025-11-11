'''
Read a text file
Count the number of lines, words, and characters
Display the results
Handle file not found errors
Handle permission errors
Output Lines: 84
Words: 906
Characters: 5502
'''
def count_file_stats(filename) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
          # Logikk for hvordan man teller i oppgaven
        lines = content.splitlines()
        num_lines = len(lines)
        num_words = len(content.split())
        num_chars = len(content)
        # print result
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")

    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print(f"Error: You do not have permission to read: {filename} ")
    except IOError as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    count_file_stats("large_example.txt")
