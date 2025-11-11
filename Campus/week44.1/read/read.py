

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()


# try:
#     with open("example.txt", "r", encoding="utf-8") as file:
#         content = file.read()
#         print(file.content)
# except FileNotFoundError:
#     print("Error: File not found")
# except PermissionError:
#     print("Error: You dont have permission to read this file")
# except Exception as e:
#     print(f"An unexpected error occurred: {e} ")


# try:
#     with open("example.txt", "r", encoding="utf-8") as file:
#         line1 = file.readline()
#         line2 = file.readline()
#         print(f"line 1: {line1}")
#         print(f"line 2: {line2}")
# except FileNotFoundError:
#     print("Error: file not found")
# except IOError as e:
#     print(f"I/O error occurred: {e}")


try:
    with open("example.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: file not found")
except IOError as e:
    print(f"I/O error occurred: {e}")
