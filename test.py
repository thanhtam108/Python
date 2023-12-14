input = int(input("Enter the number to check: "))
flag = True

if (input == 1):
    flag = False
else:
    for i in range(1, input-1):
        if (input % i == 0):
           flag = False

if input == 0:
    print("The number is neither prime nor not prime!")
elif (flag == True): 
    print("The number is prime!")
else:
    print ("The number is not prime!")