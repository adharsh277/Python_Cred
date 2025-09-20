###write calculate the sum of recuriseve of 5 n natural number
def calc_sum(n):
    if n == 0:      # base case
        return 0
    return calc_sum(n-1) + n   # recursive call

sum = calc_sum(5)
print(sum)

