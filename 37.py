# using slicing
def reverse_string(input_str):
    reversed_str = ""
    
    # Iterate through the characters in reverse order
    """
    The first colon : specifies the starting index of the slice. When omitted, as in [::-1], it defaults to the beginning of the sequence.
    The second colon : specifies the ending index of the slice. When omitted, it defaults to the end of the sequence.
    The -1 after the second colon indicates the step value. In this case, it means to move through the sequence in steps of -1, which effectively reverses the sequence.
    """
    for char in input_str[::-1]: 
        reversed_str += char
    
    return reversed_str

# Example usage:
original_string = "Hello, World!"
reversed_result = reverse_string(original_string)

print("Original String:", original_string)
print("Reversed String:", reversed_result)

# without slicing
print("Without slicing : ")
def reverse_string2(input_str):
    reversed_str = ""
    
    # Iterate through the characters in reverse order
    l = len(input_str)
    for i in range(l-1,-1,-1): #l-1 is the start index, -1 is the end l=index which is not included, -1 is the step value i.e. every time the indes is decremented by -1.
        reversed_str += input_str[i]
    
    return reversed_str

# Example usage:
original_string = "Hello, World!"
reversed_result = reverse_string2(original_string)

print("Original String:", original_string)
print("Reversed String:", reversed_result)
