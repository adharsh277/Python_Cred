# f= open("lecture7/practice.txt","r ")
# f.write("Hi everyone\nwe are learning file in I/O\n")
# f.write("using java.\nI like programming in java.")

# with open("lecture7/practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "python")
# print(new_data)

# with open("lecture7/practice.txt", "w") as f:
#     f.write(new_data)

word = "learning"
with open ("lecture7/practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

## to find in which line of the files doees the word learning occur print 

def check_for_line():
    word = "python"
    line_no = 1

    with open("lecture7/practice.txt", "r") as f:
        for line in f:
            if word in line:
                return line_no   # return line number if found
            line_no += 1

    return -1   # if not found

print(check_for_line())
