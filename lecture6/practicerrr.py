###write calculate the sum of recuriseve of 5 n natural number
def calc_sum(n):
    if n == 0:      # base case
        return 0
    return calc_sum(n-1) + n   # recursive call

sum = calc_sum(5)
print(sum)

## write evry recudsieve every element
def print_list(items, idx):
    if idx == len(items):   # base case: stop when index reaches list length
        return
    print(items[idx])       # print current element
    print_list(items, idx+1)  # recursive call for next element

fruits = ["apple", "litchi", "banana", "mango"]
print_list(fruits, 0)   # start with index 0


