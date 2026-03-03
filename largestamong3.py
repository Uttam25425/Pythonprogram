n1=int(input("enter your first number"))
n2=int(input("enter your second number"))
n3=int(input('enter your third number'))
if n1>n2 and n1>n3:
    print(n1,'is largest')
elif(n2>n3):
    print(n2,'is the largest')
else:
    print(n3,"is the largest")