try:
    with open("output.txt", "a", encoding="utf-8") as file:
        file.write("This line is appended! \n")
    print("File written successfully.")
except PermissionError:
    print("You dont have permission to write to this file.")
except IOError as e:
    print(f"I/O error occurred: {e}")
