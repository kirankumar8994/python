import os

file_to_remove = "D:\\DOCS\\S1 BA ENGLISH ATTENDANCE.xlsx"

try:
    os.remove(file_to_remove)
    print(f"File '{file_to_remove}' removed successfully.")
except OSError as e:
    print(f"Error removing file '{file_to_remove}': {e}")
