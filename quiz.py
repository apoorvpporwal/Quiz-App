import random

print("welcome to the quiz")

# n = random.choice([1,2,3,4,5])
# m = set()
# while (n not in m):
#     m.add(n)
#     return m
# else:
#     random.choice([1,2,3,4,5])

# print(n)
selected = set()
def fun():
    if len(selected) == 5:
        return None
    numbers = random.choice([1, 2, 3, 4, 5])
    if numbers in selected:
        return fun()
    else:
        selected.add(numbers)
        return numbers



qns = {"What does CPU stand for?" : " Central Processing Unit",
       "Which of the following is not an operating system?" : " Python",
       "What is the time complexity of binary search in the worst case?" : "O(log n)",
       "Which data structure uses LIFO (Last In, First Out) order?" : "Stack",
       "Which protocol is used to transfer files between computers on the Internet?" : " FTP"}
while (True):
    n = fun()
    if (n==1):
        print("What does CPU stand for?")
        print('''1.Central Processing Unit
        2.Central Programming Unit
        3.Computer Processing Unit
        4.Control Processing Unit''')
        ans = input("Enter your answer: ")
        if (ans == "1"):
            print("Correct")
        else:
            print("incorrect answer")
            print(f"correct answer is :{qns["What does CPU stand for?"]}")
    elif(n==2):
        print("Which of the following is not an operating system?")
        print('''1.Windows
            2.Linux
            3.Python
            4.macOS''')
        ans = input("Enter your answer: ")
        if (ans == "3"):
            print("Correct")
        else:
            print("incorrect answer")
            print(f"correct answer is :{qns["Which of the following is not an operating system?"]}")
    elif(n==3):
        print("What is the time complexity of binary search in the worst case?")
        print('''
            1.O(n)
            2.O(log n)
            3.O(n^2)
            4.O(1)''')
        ans = input("Enter your answer: ")
        if (ans == "2"):
            print("Correct")
        else:
            print("incorrect answer")
            print(f"correct answer is :{qns["What is the time complexity of binary search in the worst case?"]}")
    elif(n==4):
        print("Which data structure uses LIFO (Last In, First Out) order?")
        print(''' 
            1.Queue
            2.Stack
            3.Array
            4.Linked List''')
        ans = input("Enter your answer: ")
        if (ans == "2"):
            print("Correct")
        else:
            print("incorrect answer")
            print(f"correct answer is :{qns["Which data structure uses LIFO (Last In, First Out) order?"]}")
    elif(n==5):
        print("Which protocol is used to transfer files between computers on the Internet?")
        print('''
            1.HTTP
            2.FTP
            3.SMTP
            4.TCP''')
        ans = input("Enter your answer: ")
        if (ans == "2"):
            print("Correct")
        else:
            print("incorrect answer")
            print(f"correct answer is :{qns["Which protocol is used to transfer files between computers on the Internet?"]}")



            