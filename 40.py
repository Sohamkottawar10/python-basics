def print_any_non_max(numbers):
    if len(numbers) == 0:
        print("Empty list")
        return
    
    max_value = max(numbers)
    
    for num in numbers:
        if num != max_value:
            print("One non-maximum number:", num)
            return  # Stop after printing one non-maximum number
    print("Non max number doesnt exist")

# Example usage:
number_list = [8, 81,8]
print("Original List:", number_list)
# print("One Non-Maximum Number:")
print_any_non_max(number_list)
