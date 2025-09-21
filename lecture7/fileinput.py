# f = open("lecture7/demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))   # shows the datatype of "data"
# f.close()


# f = open("lecture7/demo.txt", "r")

# data = f.readline()
# print(data)


# print(data)
# print(type(data))   # shows the datatype of "data"

# line1=f.readline()
# print(line1)


# f.close()

### writing mode

f = open("lecture7/demo.txt", "a")
#f.write("I want to learn devops \n do some devops project"
f.write("\n I want to learn cloud devops \n do some cloud related devops project")

f.close()