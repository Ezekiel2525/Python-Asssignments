
import random
import time

def register():
    global student  #student was made global in order to be able to be accessible in other functions
    student = []
    info = ["First_name", "Last_name", "Age", "Gender", "Address", "phone_number", "password"]
    for x in info:
        information = input(f"Enter your {x}: ").strip()
        while x == "phone_number" and len(information) != 11:
             information = input(f"Enter your {x}: ")
        student.append(information)
    matric_num = random.randrange(200250, 480450)
    new_matric_num = "SQI/2019/" + str(matric_num)
    student.append(new_matric_num)
    print(f"You have successfully registered and your matric number is {new_matric_num}")
    time.sleep(2)
    login()  #REASON: this was used here because after registration, the site should take u to the login section


def login():
    user_matric = input("Enter your matric number ")
    user_pass = input("Enter your password ")
    if user_matric == student[7] and user_pass == student[6]:
        print("You have successfully logged in")
        time.sleep(1)
        home() # REASON: after logging in, you should be able to access the homepage
    else:
        print("Invalid login details. Try again")
        login()  #REASON: failure to give in correct login details, you should be able to try again


def home():
    print("""What Operation would you like to perform?
            1. CBT
            2. Calculator
            3. Exit
            """)
    decision = input(">>> ")
    if decision == '1':
        cbt()
    elif decision == '2':
        calculator()
    elif decision == '3':
        print("GOODBYE!")



def cbt():
    score = 0            
    questions = ["Where is SQI located in Ibadan?\n", "Where is oyo located in the geo-political zone\n",
                        "Which of these is a colour?\n"]
    options = ["a). Oke - ado b). Mokola c). Dugbe\n",
                    "a). South-West b). South-East c). South-South\n",
                    "a). Red b). Water c). Eba\n"]
    answers = ["c", "a", "a"]

    for i in range(len(questions)):
        print(questions[i])
        print(options[i])
        student_answer = input("enter your answer: ")
        if student_answer == answers[i]:
            print("good!")
            score += 10
        else:
            print("bad")
            score -= 5
    print(f"Hello {student[0]} {student[1]}, you scored {score}")
    print("Enter 1 to take the exam again or 2 to go back home")
    decision = input(">>> ")
    if decision == "1":
        cbt()
    elif decision == "2":
        home() #REASON: Incase you dont want to take the exam, you should be able to perform a new task in the homepage

def calculator():
    print("Enter 1 to perform calculation and 2 to go back home")
    decision = input(">>> ")
    if decision == "1":
        val1 = float(input("Enter the first value: "))
        operation = input("""
                        Enter 1 to perform addition
                        Enter 2 to perform subtraction
                        Enter 3 to perform multiplication
                        Enter 4 to perform division: """)
        val2 = float(input("Enter the second value: "))
        if operation == "1":
            print(val1 + val2)
            calculator() #REASON; You should be able to perform another operation after carrying out your preferred opt.
        elif operation == "2":
            print(val1 - val2)
            calculator()  #REASON; You should be able to perform another operation after carrying out your preferred opt.
        elif operation == "3":
            print(val1 * val2)
            calculator()  #REASON; You should be able to perform another operation after carrying out your preferred opt.
        elif operation == "4":
            print(val1 / val2)
            calculator()  #REASON; You should be able to perform another operation after carrying out your preferred opt.
        else:
            print("Invalid Operation")
        
    elif decision == "2":
        home()  #REASON: Incase you dont want to  perform the task, you should be able to perform a new task in the homepage
    


register()
