# 1. Create a class representing a bank account. Include attributes like account number, account balance,
#     and account type. Implement methods to deposit and withdraw money from the account.



# class bankAccount:

#     def __init__(self):
#         self.accountNumber = ""
#         self.accountBalance = 0.0
#         self.accountType = ""

#     def input(self):
#         self.accountNumber = input("Enter account number: ")
#         self.accountBalance = float(input("Enter account balance: "))
#         self.accountType = input("Enter account type: ")

#     def deposit(self):
#         amount = float(input("Enter deposit amount: "))
#         self.accountBalance += amount
#         print(
#             f"Deposit of {amount} successful. Updated balance: {self.accountBalance}")

#     def withdraw(self):
#         amount = float(input("Enter withdraw amount: "))
#         if self.accountBalance < 0 or self.accountBalance < amount:
#             print("Account balance is invalid to withdraw.")
#             return
#         else:
#             self.accountBalance -= amount
#             print(
#                 f"Withdrawal of {amount} successful. Updated balance: {self.accountBalance}")
#             # withdrawing things


# bk1 = bankAccount()
# bk1.input()
# bk1.deposit()
# bk1.withdraw()

# 2.  Create a class representing a book. Include attributes like title, author, genre, and publication date.
#     Implement methods to lend and return the book.

# import datetime

# class Book:
#     def __init__(self):
#         self.title = ""
#         self.author = ""
#         self.genre = ""
#         self.pubdate = datetime.datetime.now()
#         self.is_available = True

#     def input(self):
#         self.title = input("Enter title of book: ")
#         self.author = input("Enter author of book: ")
#         self.genre = input("Enter genre of book: ")
#         print("Enter publication date:")
#         year = int(input('Enter a year'))
#         month = int(input('Enter a month'))
#         day = int(input('Enter a day'))
#         self.pubdate = datetime.date(year, month, day)

#     def lend(self):
#         if self.is_available:
#             print(f"The book '{self.title}' by {self.author} has been lent.")
#             self.is_available = False
#         else:
#             print(f"Sorry, the book '{self.title}' is already lent.")

#     def return_book(self):
#         if not self.is_available:
#             print(f"Thanks for returning the book '{self.title}'.")
#             self.is_available = True
#         else:
#             print(
#                 f"The book '{self.title}' is already available in the library.")
# book1 = Book()
# book1.input()
# book1.lend()
# book1.lend()
# book1.return_book()

# 3.  Create a class representing a car. Include attributes like make, model, year, and color.
#     Implement methods to start and stop the car, accelerate, and brake.
# import datetime
# import time

# class Car:
#     def __init__(self):
#         self.brand = ""
#         self.model = ""
#         self.pubyear = datetime.datetime.now()
#         self.color = ""
#         self.velocity = 0
#         self.isBraked = False
#         self.engineIsStarted = False
#     def brake(self):
#         self.isBraked = True
#         print("Braking...")
#         self.decelerate()
#     def releaseBrake (self):
#         self.isBraked = False
#         print("Brake is release")
#     def accelerate(self):
#         if not self.isBraked and self.engineIsStarted == True:
#             self.velocity += 5
#             print(f"{self.velocity} km/h")
#         else:
#             print ("Start the engine or release brakes to accelerate.")
#     def decelerate(self):
#         if self.velocity == 0:
#             print ("Car is not moving.")
#         else:
#             self.velocity -= 5
#             print(f"{self.velocity} km/h")
#     def start (self):
#         if self.engineIsStarted == True or self.velocity > 0:
#             print("Car is moving or already started")
#         else:
#             self.engineIsStarted = True
#             print("Car engine is started.")
#     def stop(self):
#         if self.velocity >= 5:
#             print ("Brake first!")
#             return
#         else:
#             self.brake()
#             self.engineIsStarted = False
#             print("Engine is stopped.")
# car = Car()
# car.accelerate()
# time.sleep(3)
# car.start()
# time.sleep(3)
# car.brake()
# time.sleep(3)
# car.accelerate()
# time.sleep(3)
# car.releaseBrake()
# time.sleep(3)
# car.accelerate()
# time.sleep(3)
# for x in range(1,10):
#     car.accelerate()
#     time.sleep(1)
# car.stop()
# time.sleep(3)
# for x in range(1,10):
#     car.brake()
#     time.sleep(1)
# car.stop()
# car.brake()
# car.stop()

# 4.  Create a class representing a student management system. Include attributes like student name, student ID,
#     and student grades. Implement methods to add and remove students, and to calculate student averages.

class System:
    def __init__(self):
        self.students = {}
    def addStudent(self, ID, name, grades):
        if ID not in self.students:
            self.students[ID]={'name' : name, 'grades' : grades}
            print(f"Student {name} with ID {ID} added successfully.")
        else:
            print(f"Student {name} with ID {ID} already exists")
    def removeStudent(self, ID):
        if ID in self.students:
            del self.students[ID]
            print(f"Student {ID} is deleted.")
        else:
            print(f"Student {ID} does not exists in database.")
    def calculateAvg (self, ID):
        if ID in self.students:
            grades = self.students[ID]['grades']
            if grades:
                average = sum(grades) / len(grades)
                return average
            else:
                return "No grades available for the student."
        else:
            return "Error: No student found"
sys = System()
sys.addStudent("123", "le", [10, 9, 9.5])
print(sys.calculateAvg("123"))
sys.removeStudent("123")

# 5.  Create a class representing a social media platform. Include attributes like user name, user profile,
#     and user posts. Implement methods to create and delete user accounts, and to post and share content.



# 6. Create a class representing a deck of cards. Implement methods to shuffle the deck, draw a card,
#     and add a card back to the deck.
# 7. Create a class representing a binary tree. Implement methods to insert, search, and delete nodes from the tree.
# 8. Create a class representing a linked list. Implement methods to insert, search, and delete nodes from the list.
# 9. Create a class representing a hash table. Implement methods to put, get, and
#     remove key-value pairs from the hash table.
# 10. Create a class representing a web server. Implement methods to handle HTTP requests and to serve web pages.
