def fact(a):
    if a==1:
        return 1
    return a*fact(a-1)

a = int(input())
print("fact of",a,"is",fact(a))