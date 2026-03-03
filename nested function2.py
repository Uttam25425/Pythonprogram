def outer():
    def inner():
        print("This is a inner function")
    inner()
outer()
