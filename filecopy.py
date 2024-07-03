def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        
        print(f"Contents of {source_file} copied to {destination_file} successfully.")
    
    except FileNotFoundError:
        print("One or both files not found.")
    
    except IOError as e:
        print(f"Error occurred: {e}")

source_file = "C:\\Users\\sherl\\OneDrive\\Desktop\\Sem 1 Notes\\c programs role\\module 1 and 2\\FILECOPY.txt"
destination_file = "C:\\Users\\sherl\\OneDrive\\Desktop\\Sem 1 Notes\\c programs role\\module 1 and 2\\DESTINATION.txt"

copy_file(source_file, destination_file)
