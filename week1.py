import random

# input = int(input("Enter the number to check: "))
# flag = True

# if (input == 1):
#     flag = False
# else:
#     for i in range(1, input-1):
#         if (input % i == 0):
#            flag = False

# if input == 0:
#     print("The number is neither prime nor not prime!")
# elif (flag == True): 
#     print("The number is prime!")
# else:
#     print ("The number is not prime!")

def check(num):
    if (int(num) == 0):
        return "false"
    elif (int(num) % 2 == 0):
        return "even"
    else:
        return "odd"


def inputList():
    List = []
    
    min_range = 1
    max_range = 100
    num_of_numbers = 69

    for _ in range(num_of_numbers):
        random_number = random.randint(min_range, max_range)
        List.append(random_number)
    return List


# number = inputList()
# for x in number:
#     if check(x) == "even":
#         print(x)

Name = "Le Thanh Tam"
for x in range(len(Name) - 1, -1, -1):
    print (Name[x], end="")
        
string = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS-Pneumonoultramicroscopicsilicovolcanoconiosis"
dict = {}
for x in range(0, len(string)):
    count = 0
    if string[x] in dict:
        continue
    else :
        for y in range (x, len(string)):
            if (string[x] == string[y]):
                count += 1
        dict[string[x]] = count

for key,value in dict.items():
    print(f"{key}: {value}")
            