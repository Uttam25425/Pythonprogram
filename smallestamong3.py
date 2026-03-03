n1=int(input('enter your first number'))
n2=int(input('enter your second number'))
n3=int(input('enter your third number'))
if n1<n2 and n1<n3:
    print(n1,'is smallest among three number')
elif n2<n3:
    print(n2,'is smallest among three number')
else:
    print(n3,'is smallest among three number')