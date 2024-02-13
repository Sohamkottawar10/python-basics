def checkIsEmail(email):
    e = "@gmail.com"
    l = len(email)
    l2 = len(e)
    if l <= l2:
        return False
    for i in range(l-1,-1,-1):
        
        if email[i] != e[l2-1]:
            return False
        
        l2 -=1
        if l2 == -1:
            return True

    


email = input("Enter an email : ")
print(checkIsEmail(email))

print("Method 2")
e = "@gmail.com"
email1=email[-10:]
if e in email1:
    print("True")
else:
    print("False")

    

