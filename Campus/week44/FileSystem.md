# Python File System Operations:

---

# plan for today:

- File Operations and Error Handling
- File system operations
-

# Fundamentals

## 1.1 Introduction to File Operations 

### What is File I/O?

File Input/Output (I/O) operations allow programs to:

- Read data from files
- Write data to files
- Modify existing files
- Navigate the file system

### Why Proper Error Handling Matters

Files can fail to open, be corrupted, have permission issues, or not exist. Robust error handling prevents crashes and provides meaningful feedback.

---

## 1.2 Basic File Reading 

### Method 1: Using `open()` and `close()`

```python
# Basic file reading - NOT RECOMMENDED (no error handling)
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

**Problems with this approach:**

- File remains open if an error occurs
- No error handling
- Easy to forget `close()`

### Method 2: Using Context Managers (RECOMMENDED)

```python
# Proper way with error handling
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

chmod 000 example.txt to see the Permission error.

**Why this is better:**

- `with` statement automatically closes the file
- Handles specific exceptions
- Catches unexpected errors

---

## Common File Errors in Python

When working with `open()` in Python, several different errors can occur depending on what goes wrong. Below are the most common ones, when they happen, and what they mean.

| Error Type           | When it Happens                              | Meaning (Simple)                |
| -------------------- | -------------------------------------------- | ------------------------------- |
| `FileNotFoundError`  | The file path is wrong or file doesn't exist | Python can't find the file      |
| `PermissionError`    | No read (or write) permissions               | OS blocks you from accessing it |
| `IsADirectoryError`  | A directory is opened instead of a file      | You gave Python a folder path   |
| `NotADirectoryError` | A part of the path is not a directory        | The path structure is invalid   |
| `UnicodeDecodeError` | Reading a binary file as text                | Wrong file type/encoding        |
| `ValueError`         | Using a closed file handle                   | File object is no longer valid  |
| `IOError / OSError`  | Disk / I/O level problems                    | Hardware or low-level OS issue  |

---

## 1.3 File Reading Methods 

### `read()` - Read Entire File

### `encoding = utf-8`

https://en.wikipedia.org/wiki/Character_encoding#Common_character_encodings

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

### `readline()` - Read One Line at a Time

```python
try:
    with open('example.txt', 'r') as file:
        line1 = file.readline()
        line2 = file.readline()
        print(f"Line 1: {line1}")
        print(f"Line 2: {line2}")
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

### `readlines()` - Read All Lines into a List

```python
try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

### Iterating Over a File (Memory Efficient)

```python
try:
    with open('large_file.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

---

## 1.4 Basic File Writing 

### Writing Modes

- `'r'` - Read
- `'w'` - Write (overwrites existing content)
- `'a'` - Append (adds to end of file)
- `'x'` - Exclusive creation (fails if file exists)

### Write Mode

```python
try:
    with open('output.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a new line.\n")
    print("File written successfully.")
except PermissionError:
    print("Error: You don't have permission to write to this file.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

### Append Mode

```python
try:
    with open('output.txt', 'a') as file:
        file.write("This line is appended.\n")
    print("Content appended successfully.")
except PermissionError:
    print("Error: You don't have permission to write to this file.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

### Exclusive Creation Mode

```python
try:
    with open('new_file.txt', 'x') as file:
        file.write("This file is brand new.\n")
    print("New file created successfully.")
except FileExistsError:
    print("Error: File already exists.")
except PermissionError:
    print("Error: You don't have permission to create this file.")
except IOError as e:
    print(f"I/O error occurred: {e}")
```

### Task 1: File Reader with Statistics

**Objective**: Read a text file and display statistics about it.

**Requirements**:

- Read a text file
- Count the number of lines, words, and characters
- Display the results
- Handle file not found errors
- Handle permission errors

**Output**
Lines: 84  
Words: 906  
Characters: 5502  

---

## 2.05

### command line commands.

```bash
# List files in current directory
ls

# Create a new directory
mkdir new_directory

# Move to a different directory
cd new_directory

# Copy a file
cp file1.txt file2.txt

# Rename a file
mv file1.txt file2.txt

# Delete a file
rm file.txt

# Delete a directory
rm -r directory

```

## 2.1 Working with Paths - `os` Module

### Basic Path Operations

```python
import os

# Get current working directory
try:
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
except Exception as e:
    print(f"Error getting current directory: {e}")

# List directory contents
try:
    files = os.listdir('.')
    print("Files in current directory:")
    for file in files:
        print(f"  - {file}")
except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error listing directory: {e}")
```

### Path Manipulation

```python
import os

# Join paths (works across operating systems)
try:
    path = os.path.join('folder', 'subfolder', 'file.txt')
    print(f"Joined path: {path}")
except Exception as e:
    print(f"Error joining paths: {e}")

# Split path into directory and filename
try:
    directory, filename = os.path.split('/home/user/document.txt')
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
except Exception as e:
    print(f"Error splitting path: {e}")

# Get absolute path
try:
    abs_path = os.path.abspath('file.txt')
    print(f"Absolute path: {abs_path}")
except Exception as e:
    print(f"Error getting absolute path: {e}")
```

### Checking Path Properties

```python
import os

path = 'example.txt'

try:
    # Check if path exists
    if os.path.exists(path):
        print(f"{path} exists")

        # Check if it's a file
        if os.path.isfile(path):
            print(f"{path} is a file")

        # Check if it's a directory
        if os.path.isdir(path):
            print(f"{path} is a directory")

        # Get file size
        size = os.path.getsize(path)
        print(f"File size: {size} bytes")
    else:
        print(f"{path} does not exist")
except PermissionError:
    print(f"Permission denied when accessing {path}")
except Exception as e:
    print(f"Error checking path: {e}")
```

---

## 2.2 Modern Path Handling - `pathlib` 

### Introduction to `pathlib.Path`

`pathlib` is the modern, object-oriented way to handle paths in Python 3.4+.

```python
from pathlib import Path

# Create Path objects
try:
    current = Path.cwd()
    print(f"Current directory: {current}")

    home = Path.home()
    print(f"Home directory: {home}")
except Exception as e:
    print(f"Error getting paths: {e}")

# Create a path to a file
try:
    file_path = Path('documents') / 'reports' / 'report.txt'
    print(f"File path: {file_path}")
except Exception as e:
    print(f"Error creating path: {e}")
```

### Path Properties and Methods

```python
from pathlib import Path

try:
    path = Path('example.txt')

    # Check existence
    if path.exists():
        print(f"{path} exists")

        # Check type
        print(f"Is file: {path.is_file()}")
        print(f"Is directory: {path.is_dir()}")

        # Get properties
        print(f"Name: {path.name}")
        print(f"Stem (without extension): {path.stem}")
        print(f"Suffix (extension): {path.suffix}")
        print(f"Parent directory: {path.parent}")
        print(f"Absolute path: {path.absolute()}")

        # Get file size
        print(f"Size: {path.stat().st_size} bytes")
    else:
        print(f"{path} does not exist")
except PermissionError:
    print(f"Permission denied when accessing {path}")
except Exception as e:
    print(f"Error: {e}")
```

### Reading and Writing with `pathlib`

```python
from pathlib import Path

# Reading a file
try:
    path = Path('example.txt')
    content = path.read_text()
    print(content)
except FileNotFoundError:
    print(f"File {path} not found.")
except PermissionError:
    print(f"Permission denied reading {path}")
except Exception as e:
    print(f"Error reading file: {e}")

# Writing to a file
try:
    path = Path('output.txt')
    path.write_text("Hello from pathlib!\n")
    print("File written successfully.")
except PermissionError:
    print(f"Permission denied writing to {path}")
except Exception as e:
    print(f"Error writing file: {e}")

```

---

## 2.3 Directory Operations

### Creating Directories

```python
import os
from pathlib import Path

# Using os module
try:
    os.mkdir('new_folder')
    print("Directory 'new_folder' created.")
except FileExistsError:
    print("Directory already exists.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error creating directory: {e}")

# Create nested directories
try:
    os.makedirs('parent/child/grandchild', exist_ok=True)
    print("Nested directories created.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error creating nested directories: {e}")

# Using pathlib
try:
    path = Path('new_folder_pathlib')
    path.mkdir(exist_ok=True)
    print(f"Directory {path} created.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error creating directory: {e}")

# Create parent directories automatically
try:
    path = Path('parent/child/grandchild')
    path.mkdir(parents=True, exist_ok=True)
    print(f"Nested directories created: {path}")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error creating nested directories: {e}")
```

### Removing Files and Directories

```python
import os
from pathlib import Path

# Remove a file using os
try:
    os.remove('file_to_delete.txt')
    print("File deleted.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except IsADirectoryError:
    print("Cannot remove a directory with os.remove().")
except Exception as e:
    print(f"Error deleting file: {e}")

# Remove empty directory
try:
    os.rmdir('empty_folder')
    print("Empty directory removed.")
except FileNotFoundError:
    print("Directory not found.")
except OSError:
    print("Directory is not empty.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error removing directory: {e}")

```

---

# Hour 3: Advanced Topics

## 3.1 Working with CSV Files 

### Reading CSV Files

```python
import csv

# Basic CSV reading
try:
    with open('data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
except csv.Error as e:
    print(f"CSV error: {e}")
except Exception as e:
    print(f"Error reading CSV: {e}")

# Reading CSV with headers
try:
    with open('data.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")
except FileNotFoundError:
    print("CSV file not found.")
except KeyError as e:
    print(f"Column {e} not found in CSV.")
except csv.Error as e:
    print(f"CSV error: {e}")
except Exception as e:
    print(f"Error reading CSV: {e}")
```

### Writing CSV Files

```python
import csv

# Basic CSV writing
try:
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ]

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("CSV file written successfully.")
except PermissionError:
    print("Permission denied writing CSV.")
except csv.Error as e:
    print(f"CSV error: {e}")
except Exception as e:
    print(f"Error writing CSV: {e}")

# Writing CSV with DictWriter
try:
    data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]

    with open('output_dict.csv', 'w', newline='') as file:
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
    print("CSV file with headers written successfully.")
except PermissionError:
    print("Permission denied writing CSV.")
except csv.Error as e:
    print(f"CSV error: {e}")
except Exception as e:
    print(f"Error writing CSV: {e}")
```

---

## 3.2 Working with JSON Files 

### Reading JSON Files

```python
import json

# Read JSON file
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("JSON file not found.")
except json.JSONDecodeError as e:
    print(f"Invalid JSON format: {e}")
except PermissionError:
    print("Permission denied reading JSON.")
except Exception as e:
    print(f"Error reading JSON: {e}")

# Parse JSON string
try:
    json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
    data = json.loads(json_string)
    print(f"Name: {data['name']}, Age: {data['age']}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON format: {e}")
except Exception as e:
    print(f"Error parsing JSON: {e}")
```

### Writing JSON Files

```python
import json

# Write JSON file
try:
    data = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York',
        'hobbies': ['reading', 'cycling', 'photography']
    }

    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("JSON file written successfully.")
except PermissionError:
    print("Permission denied writing JSON.")
except TypeError as e:
    print(f"Data cannot be serialized to JSON: {e}")
except Exception as e:
    print(f"Error writing JSON: {e}")

# Convert to JSON string
try:
    data = {'name': 'Bob', 'age': 25}
    json_string = json.dumps(data, indent=2)
    print(json_string)
except TypeError as e:
    print(f"Data cannot be serialized to JSON: {e}")
except Exception as e:
    print(f"Error converting to JSON string: {e}")
```

## 3.3 File Operations with `shutil`

### Copying Files and Directories

```python
import shutil
from pathlib import Path

# Copy a file
try:
    shutil.copy('source.txt', 'destination.txt')
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error copying file: {e}")


```

### Moving and Renaming

```python
import shutil

# Move/rename a file
try:
    shutil.move('old_name.txt', 'new_name.txt')
    print("File moved/renamed successfully.")
except FileNotFoundError:
    print("Source file not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error moving file: {e}")

# Move file to different directory
try:
    shutil.move('file.txt', 'destination_folder/file.txt')
    print("File moved to new directory.")
except FileNotFoundError:
    print("Source file or destination folder not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error moving file: {e}")
```

### Disk Usage Information

```python
import shutil

# Get disk usage statistics
try:
    usage = shutil.disk_usage('/')
    print(f"Total space: {usage.total / (1024**3):.2f} GB")
    print(f"Used space: {usage.used / (1024**3):.2f} GB")
    print(f"Free space: {usage.free / (1024**3):.2f} GB")
except Exception as e:
    print(f"Error getting disk usage: {e}")
```

---

## 3.7 Advanced File Searching and Filtering

### Using `glob` for Pattern Matching

```python
from pathlib import Path

# Find all Python files in current directory
try:
    python_files = list(Path('.').glob('*.py'))
    print("Python files found:")
    for file in python_files:
        print(f"  - {file}")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error searching files: {e}")

# Recursive search for all text files
try:
    text_files = list(Path('.').rglob('*.txt'))
    print(f"\nFound {len(text_files)} text files:")
    for file in text_files:
        print(f"  - {file}")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error searching files: {e}")


```


### Task 5: CSV Grade Analyzer

**Objective**: Read a CSV file containing student grades and generate a report.

**Requirements**:

- Read a CSV file with columns: Name, Math, Science, English
- Calculate average grade for each student
- Find highest and lowest scoring students
- Write a summary report to a new file
- Handle CSV errors and missing data

```python
import csv

def analyze_grades(input_csv, output_file):
    """
    Analyze student grades from CSV and create a report.
    CSV format: Name,Math,Science,English
    """
    # TODO: Implement this function
    pass

# Test your function
analyze_grades('grades.csv', 'grade_report.txt')
```

**Sample input CSV**:

```
Name,Math,Science,English
Alice,85,90,88
Bob,92,88,85
Charlie,78,85,90
```

**Expected output**:

```
Grade Report
============
Alice: Average = 87.67
Bob: Average = 88.33
Charlie: Average = 84.33

Highest Average: Bob (88.33)
Lowest Average: Charlie (84.33)
```

---

## Additional Resources

- Python Official Documentation: https://docs.python.org/3/library/filesys.html
- Real Python File Handling: https://realpython.com/working-with-files-in-python/
- PEP 8 Style Guide: https://pep8.org/
- pathlib Documentation: https://docs.python.org/3/library/pathlib.html

---

## Conclusion

This lecture has covered:

- Basic file reading/writing, context managers, error handling
- Path manipulation (os/pathlib), directory operations, CSV/JSON

Remember: **Always use proper error handling** when working with files. Files can be missing, locked, corrupted, or inaccessible. Robust error handling makes your code production-ready.
