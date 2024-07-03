factorial_dict = {}

def factorial_with_cache(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    elif n in factorial_dict:
        return factorial_dict[n]
    else:
        result = n * factorial_with_cache(n - 1)
        factorial_dict[n] = result
        return result

number = 5
print(f"The factorial of {number} is: {factorial_with_cache(number)}")
print("Factorials stored in the dictionary:")
print(factorial_dict)
