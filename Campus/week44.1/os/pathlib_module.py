from pathlib import Path


# try:
#     current = Path.cwd()
#     print(f"Current dir: {current}")

#     home = Path.home()
#     print(f"Home dir: {home}")
# except IOError as e:
#     print(f"Error getting paths: {e}")

try:
    path = Path('example.txt')

    if path.exists():
        print(f"{path} exists")

        print(f"Is file: {path.is_file()}")
        print(f"Is dir: {path.is_dir()}")

        print(f" Name: {path.name}")

except IOError as e:
    print(f"Error: {e}")
