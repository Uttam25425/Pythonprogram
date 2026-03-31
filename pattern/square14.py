n=int(input("enter number of rows"))
k=0
for i in range (n):
    for j in range(n):
        print(chr(65+k),end=" ")
        k=k+2
    print()