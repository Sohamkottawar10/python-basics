file1 = open('File.txt','w')
file1.write(" Hello guys")
file1.write(" \nHello once again,,,, ")
file1.write(" \nHello once again.......... ")
file1.close()
file = open('File.txt', 'r')
# import os
# print("Current Working Directory:", os.getcwd()), w
# file1 = open('File.txt', 'r')
# for each in file:
#     print(each)
# print (file.read())
# print (file.read(5)) #read 5 charac
data = file.readlines()
for line in data:
    word = line.split()
    print (word)

#we can print file only once in read mode