import os

directory = "my_directory"

try:
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except OSError as e:
    print(f"Failed to list directory '{directory}': {e}")
