def recursive_sum(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    else:
        return n + recursive_sum(n - 1)

# Calculate the sum from 0 to 10
result = recursive_sum(10)
print("The sum of numbers from 0 to 10 is:", result)
