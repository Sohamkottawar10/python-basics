A = int(input("A = "))
B = int(input())
C = int(input())
if A < B:
    if B<C:
        print(A,"<",B,"<",C)
    else:
        if A<C:
            print(A,"<",C,"<",B)
        else:
            print(C,"<",A,"<",B)
else:
    if B>C:
        print(C,"<",B,"<",A)
    else:
        if A>C:
            print(B,"<",C,"<",A)
        else:
            print(B,"<",A,"<",C)
