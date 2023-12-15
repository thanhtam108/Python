# 1. **Array Operations:**
#     - Write a function to find the maximum element in an array.
#     - Implement a function to reverse an array in-place.

import random

# def findMax(arr):
#     max = float('-inf')
#     for x in arr:
#         if x > max:
#             max = x
#     return max

# def reverseArr(arr):
#     arr1 = []
#     for x in range(len(arr) - 1, -1, -1):
#         arr1.append(arr[x])
#     return arr1

# List = []
# min_range = 1
# max_range = 100
# num_of_numbers = 69
# for _ in range(num_of_numbers):
#     random_number = random.randint(min_range, max_range)
#     List.append(random_number)
# print(List)
# print("Max value of first array: " + str(findMax(List)))
# print(reverseArr(List))

# 2. **Stack Operations:**
#     - Implement a stack data structure from scratch and perform push and pop operations.
#     - Check if a given string of parentheses is balanced using a stack.

# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return len(self.items) == 0
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print("Stack is empty. Cannot pop.")
#             return None
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             print("Stack is empty. Cannot peek.")
#             return None
#     def size(self):
#         return len(self.items)

# def checkBalance (str):
#     st = Stack()
#     for char in str:
#         if char is "(":
#             st.push(char)
#         elif char is ")":
#             if st.is_empty():
#                 return False
#             st.pop()
#     return st.is_empty()

# st = Stack()
# st.push(random.randint(0,100))
# st.push(random.randint(0,100))
# st.push(random.randint(0,100))
# st.push(random.randint(0,100))
# st.push(random.randint(0,100))

# print ("Stack: " , st.items)
# print ("Pop: " , st.pop())

# str = "(a+b) * (a-b)"
# print("Is the string balanced?" ,checkBalance(str))

# 3. **Queue Operations:**
#     - Implement a queue data structure and perform enqueue and dequeue operations.
#     - Simulate a line of people waiting and serving customers using a queue.

# class Queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.isEmpty():
#             return self.items.pop(0)
#         else:
#             print("Queue is empty. Cannot dequeue")
#             return
#     def size(self):
#         return len(self.items)

# qu = Queue()
# qu.enqueue(random.randint(0,69))
# qu.enqueue(random.randint(0,69))
# qu.enqueue(random.randint(0,69))
# qu.enqueue(random.randint(0,69))
# qu.enqueue(random.randint(0,69))

# print ("First queue: ", qu.items)

# qu.dequeue()
# qu.dequeue()

# print("Second queue:", qu.items)

# def simulate_line():
#     line = Queue()

#     line.enqueue("Person 1")
#     line.enqueue("Person 2")
#     line.enqueue("Person 3")
#     line.enqueue("Person 4")

#     print("Initial Line:", line.items)

#     served_customer = line.dequeue()
#     print(f"Serving {served_customer}")

#     line.enqueue("Person 5")

#     print("Updated Line:", line.items)

#     for _ in range(line.size()):
#         served_customer = line.dequeue()
#         print(f"Serving {served_customer}")

#     served_customer = line.dequeue()
#     print(f"Serving {served_customer}")

# simulate_line()

# 4. **Linked List:**
#     - Create a singly linked list and write functions to insert, delete, and traverse it.
#     - Write a function to find the middle element of a linked list.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head is None

#     def append(self, data):
#         new_node = Node(data)
#         if self.is_empty():
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node

#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, data):
#         if self.is_empty():
#             print("List is empty. Cannot delete.")
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return

#         current_node = self.head
#         while current_node.next and current_node.next.data != data:
#             current_node = current_node.next

#         if current_node.next:
#             current_node.next = current_node.next.next
#         else:
#             print(f"{data} not found in the list. Cannot delete.")

#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")
#     def midFinding (self):
#         if self.is_empty():
#             print ("List is empty.")
#             return
#         pivot1 = self.head
#         pivot2 = self.head
#         while pivot2 is not None and pivot2.next is not None:
#             pivot1 = pivot1.next
#             pivot2 = pivot2.next.next
#         return pivot1.data

# my_linked_list = LinkedList()
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.prepend(0)
# my_linked_list.print_list()

# my_linked_list.delete(2)
# my_linked_list.print_list()

# print(my_linked_list.midFinding())

# 5. **Searching:**
#     - Implement linear search to find an element in an array.
#     - Implement binary search for a sorted array.


# def linearSearch(arr, item):
#     for x in arr:
#         if str(x) == item:
#             return True
#     return False


# def binSearch(arr, item):
#     arr = sorted(map(str, arr))
#     low = 0
#     high = len(arr) - 1 
#     while low <= high:
#         mid = (low + high) // 2
#         mid_val = arr[mid]
        
#         if mid_val == item:
#             return True
#         elif mid_val < item:
#             low = mid + 1
#         else: high = mid - 1
#     return False

# arr = [1, 2, 3, 5, 88, 96, 4, 12, "str", 0.12, -98]
# inp = input("Enter the element for linear search: ")
# print("Linear:")
# if linearSearch(arr, inp):
#     print(f"{inp} is in the array.")
# else:
#     print(f"{inp} is not in the array.")

# print("Binary:")
# if binSearch(arr, inp):
#     print(f"{inp} is in the array.")
# else:
#     print(f"{inp} is not in the array.")

# 6. **Sorting:**
#     - Implement a simple sorting algorithm like Bubble Sort or Selection Sort.
#     - Sort an array of integers in ascending and descending order.

def AscInsertionSort (arr):
    for x in range(0, len(arr)):
        temp = arr[x]
        y = x - 1
        while y >= 0 and arr[y] > temp:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = temp
    return arr

def DscInsertionSort (arr):
    for x in range(0, len(arr) - 1):
        temp = arr[x]
        y = x - 1
        while y >= 0 and arr[y] < temp:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = temp
    return arr

arr = [9, 4, 155, 6, 24, 67, 11, 109]
asc_sorted = AscInsertionSort(arr.copy())
print("Ascending order:", asc_sorted)

desc_sorted = DscInsertionSort(arr.copy())
print("Descending order:", desc_sorted)


# 7. **Recursion:**
#     - Write a recursive function to calculate the factorial of a number.
#     - Implement a recursive function to compute the nth Fibonacci number.
# 8. **String Operations:**
#     - Write a function to check if a string is a palindrome.
#     - Implement a function to reverse a string.
# 9. **Basic Tree Operations:**
#     - Create a binary tree and write functions to perform in-order, pre-order, and post-order traversals.
#     - Calculate the height (depth) of a binary tree.
# 10. **Basic Graph Operations:**
#     - Implement an adjacency matrix or adjacency list for a simple graph.
#     - Write a function to perform a depth-first search (DFS) or breadth-first search (BFS) on a graph.
# 11. **Hashing:**
#     - Implement a simple hash table to store key-value pairs.
#     - Write a function to compute the hash value of a string.
# 12. **Basic Algorithm Problems:**
#     - Solve simple algorithmic problems like finding the sum of an array, finding the largest element, or reversing an array.
# 13. **Bit Manipulation:**
#     - Write functions to perform basic bit manipulation operations like setting, clearing, and toggling bits.
#     - Check if a number is even or odd using bitwise operators.
# 14. **Basic Sorting Problems:**
#     - Find the minimum and maximum elements in an array without sorting it.
#     - Write a function to check if an array is sorted in ascending or descending order.
# 15. **Basic Searching Problems:**
#     - Find the first occurrence of a given element in an array.
#     - Count the number of occurrences of a specific element in an array.
