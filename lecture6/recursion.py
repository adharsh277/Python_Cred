def show(n):
    if n == 0:      # base case (stop when n = 0)
        return
    print(n)        # print current value
    show(n-1)       # recursive call (call function again with smaller n)

show(5)             # function call


## factoiral

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))