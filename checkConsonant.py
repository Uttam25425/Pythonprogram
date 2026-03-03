ch=input("enter your character : ")
if ch.isalpha() and ch not in("AEIOUaeiou"):
    print(ch,"is a consonant")
else:
    print(ch,"is not a consonant")