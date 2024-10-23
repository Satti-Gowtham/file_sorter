## File Sorter

This script takes a directory path as input and sorts the files within that directory into different folders based on their file types. The `FileSorter` class in `FileSorter.py` handles the core logic of the sorting process.

### Inputs

- **Directory path:** The path to the directory that needs to be sorted. This can be either an absolute or relative path.

### Outputs

The script doesn't have any direct outputs. Instead, it modifies the file system by:

- Creating new folders for different file types within the input directory if they don't exist already.
- Moving files into their corresponding file type folders.
- If a file with the same name already exists in the destination folder, it appends an underscore and a number to the filename to avoid overwriting.

### How it works

1. **Initialization:** The `FileSorter` class is initialized with the input directory path.
2. **Path Sanitization:** The script ensures that the provided path is an absolute path.
3. **Folder Path Determination:** For each file in the directory, the script determines the appropriate folder based on its file extension using a predefined dictionary of file types.
4. **Folder Creation:** If the folder for a specific file type doesn't exist, it's created.
5. **File Moving:** The file is moved to its corresponding folder.
6. **Duplicate Handling:** In case of duplicate filenames, the script renames the file by appending an underscore and a number.
7. **Error Handling:** If the provided directory path doesn't exist, it prints an error message.
