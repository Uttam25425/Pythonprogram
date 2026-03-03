x=int(input("enter the no of row"))
n=x//2
k=0
for i in range(n+1):
    for j in range(i+1):
        print(chr(80-k),end=" ")
        k=k+1
    print()
for i in range(n):
    for j in range(n-i):
        print(chr(80-k),end=" ")
        k=k+1
    print()