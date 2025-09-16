## practice
## practice numbers from 1 to 100
# i=1
# while i <=100:
#     print(i)
#     i=i+1

    
## print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i=i-1

### print the multiplication table
# 
# n=int(input("enter your number: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

##print the elements of the following list using a loop
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
### print heroes stufff
# heros=["ironman","steve rogers","thor","batman"]
# idx=0
# while idx<len(heros):
#     print(heros[idx])
#     idx+=1

tup = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0

while i < len(tup):
    if tup[i] == x:
        print("Found at idx", i)
        ##break   # stop searching once found
    else:
        print("finding....")
    i += 1

    