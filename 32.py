def recursive_sum(numbers):
    # Base case: If the list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: Add the first element to the sum of the rest of the elements
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# Example usage:
my_numbers = [1, 2, 3, 4, 6]

result = recursive_sum(my_numbers)
print("Sum of the numbers:", result)
