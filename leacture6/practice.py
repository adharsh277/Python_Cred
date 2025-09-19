cities = ["delhi", "chennai", "gurugon", "mumbai"]
heroes = ["steve","ironman","shaktiman"]

# def len_city(cities):
#     return len(cities)   # length of the list
# def len_heros(heores):
#     return len (heores)
def print_len(list):
    print((list))
    print(len(list))
print_len(cities)
print_len(heroes)

# print(len_heros(heroes))
# print(len_city(cities))



## write a elemet im list in as simple lien

cities = ["delhi", "chennai", "gurugon", "mumbai"]
heroes = ["steve","ironman","shaktiman"]
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)

## find the fafactroial of n numebr


# for i in range (1,n+1):
#     fact *= i
# print_list
n=5

def calc_fact(n):
    fact =1
    for i in range(1,n+1):
        fact *=i
    print(fact)
calc_fact(6)


#usdt to inr
def converter(usd_val):
    inr_val = usd_val *90
   # print(usd_val,"USD=", inr_val,"INR")
    print(usd_val,"USD=",inr_val,"INR")
converter(5)