# Program 1:

"""
x: int: This part specifies that the parameter x is expected to be of type int. It serves as a hint to developers and tools that the function expects an integer argument.
-> int:: This part specifies that the function is expected to return a value of type int. Again, it's a hint about the expected return type
"""

def function1(x: int) -> int:
 print("Inside the function: The initial value of x =", x)
 x +=5
 print("Inside the function: The value of x after the operation is ", x)
#Driver code
x = 0
x = int(input("Enter a value for x: "))
print("The value of x you have entered :", x)
function1(x) #Call the function with argument x
print("The value of x after function is called :", x)
print("The value of x remain unchanged after function call due to call by reference")