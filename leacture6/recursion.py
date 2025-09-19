def show(n):
    if(n == 0):  # base cases
        return
    print(n)
    show(n-1)   # recursion call
show(5)        #func acall