# Python code to illustrate append() mode
file = open('test.txt', 'a')
file.write("This will add at the end of the file.")
file.close()
file1 = open('test.txt') 
for each in file1:
 print (each)
