# Can't do it... This is what assignment asks for, not made into a function.
# It works like this but breaks when I try to section it into functions.

from pathlib import Path
from modules_local.file_management_using_pathlib import create_dir

# IKKE SLETT
# Alt som oppgaven ber om. Ikke delt opp i funksjoner.


def sort_files():
    try:
        base_dir = Path("Files")
        sorted_dir = base_dir / "SortedFiles"

        if base_dir.is_dir():
            for file in base_dir.iterdir():
                print(f"Path and filenames: '{file}'.")

    except FileNotFoundError:
        print("File not found")

    # Create SortedFiles and subfolders:
    create_dir(sorted_dir)
    create_dir(sorted_dir / "txt-files")
    create_dir(sorted_dir / "csv-files")
    create_dir(sorted_dir / "log-files")

    print("\n")
    # Print contents in directory "SortedFiles":
    print("Contents of SortedFiles:")
    for folder in sorted_dir.iterdir():
        print(folder)

    # Define extensions to subfolders:
    extension_to_subfolder = {
        ".txt": "txt-files",
        ".csv": "csv-files",
        ".log": "log-files",
    }

    for file in base_dir.iterdir():
        if file.is_file():
            extension = file.suffix
            if extension in extension_to_subfolder:
                target_folder = sorted_dir / extension_to_subfolder[extension]
                target_folder.mkdir(exist_ok=True)
                target_path = target_folder / file.name
                file.rename(target_path)


if __name__ == "__main__":
    sort_files()