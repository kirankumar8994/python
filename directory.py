import os

directory = "my_directory"

try:
    os.makedirs(directory)
    print(f"Directory '{directory}' created successfully.")
except OSError as e:
    print(f"Failed to create directory '{directory}': {e}")
