def is_substring(sub, main):
    return sub in main

def count_occurrences(char, s):
    return s.count(char)

def replace_substring(s, old, new):
    return s.replace(old, new)

def to_capital_letters(s):
    return s.upper()

def menu():
    print("String Operations Menu:")
    print("1. Check if the String is a Substring of Another String")
    print("2. Count Occurrences of a Character")
    print("3. Replace a Substring with Another Substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the program. Goodbye!")
            break

        if choice == '1':
            main_str = input("Enter the main string: ")
            sub_str = input("Enter the substring to check: ")
            if is_substring(sub_str, main_str):
                print(f"'{sub_str}' is a substring of '{main_str}'.")
            else:
                print(f"'{sub_str}' is not a substring of '{main_str}'.")

        elif choice == '2':
            s = input("Enter a string: ")
            char = input("Enter the character to count: ")
            count = count_occurrences(char, s)
            print(f"The character '{char}' occurs {count} times in the string.")

        elif choice == '3':
            s = input("Enter the original string: ")
            old_sub = input("Enter the substring to replace: ")
            new_sub = input("Enter the new substring: ")
            new_string = replace_substring(s, old_sub, new_sub)
            print(f"The new string is: {new_string}")

        elif choice == '4':
            s = input("Enter a string: ")
            capitalized_string = to_capital_letters(s)
            print(f"The string in capital letters is: {capitalized_string}")

        else:
            print("Invalid choice. Please try again.")
        print()

if __name__ == "__main__":
    main()
