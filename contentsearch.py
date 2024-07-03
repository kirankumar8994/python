import os

directory = "my_directory"

try:
    files = os.listdir(directory)
    py_files = [file for file in files if file.endswith(".py")]

    if py_files:
        print(f"Python files in directory '{directory}':")
        for file in py_files:
            print(file)
    else:
        print(f"No Python files found in directory '{directory}'.")

except OSError as e:
    print(f"Failed to list files in directory '{directory}': {e}")
