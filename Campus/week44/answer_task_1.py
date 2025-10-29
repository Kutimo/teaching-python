def count_file_stats(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        # Count stats
        lines = content.splitlines()
        num_lines = len(lines)
        num_words = len(content.split())
        num_chars = len(content)

        # Display results
        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    count_file_stats("large_example.txt")
