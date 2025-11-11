import os

# Get current working dir

# try:
#     current_dir = os.getcwd()
#     print(f"current dir: {current_dir}")
# except IOError as e:
#     print(f"Error: getting current dir: {e}")

# List directory
try:
    files = os.listdir('.')
    print("Files in current dir:")
    for file in files:
        print(f" - {file}")
except IOError as e:
    print(f"error: {e}")
