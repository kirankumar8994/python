def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

def reverse_and_add_until_palindrome(n):
    while not is_palindrome(n):
        reversed_num = reverse_number(n)
        n += reversed_num
        print(f"After adding {reversed_num}: {n}")
    return n

number = 123
palindrome = reverse_and_add_until_palindrome(number)
print(f"The palindrome is: {palindrome}")

