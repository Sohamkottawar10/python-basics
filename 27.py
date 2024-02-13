
def sort_three_numbers(a, b, c):
    # Create a list with the three input values
    numbers = [a, b, c]
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Return the sorted list
    return numbers

# Example usage:
num1 = int(input())
num2 = int(input())
num3 = int(input())

sorted_numbers = sort_three_numbers(num1, num2, num3)

print("Original Numbers:", num1, num2, num3)
print("Numbers in Ascending Order:", sorted_numbers)
