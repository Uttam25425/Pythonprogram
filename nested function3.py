def outer():
    x=7
    y=5
    def swap():
        nonlocal x,y
        x,y=y,x
        print("value of x after swapping",x)
        print("value of y after swapping",y)
    swap()
outer()
