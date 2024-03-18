registration = input("Are you a student of SQI (yes/no): ").strip().lower()
if registration.lower() == "yes":
    status = input("Enter your status\n1. Single\n2. Searching\n3. married: ")
    if status.lower() == "1":
        course = input("Enter your course: ")
        if course.lower() == "datascience":
            print("welcome to class")
        else:
            print("go to front desk")
    elif status.lower() == "2":
        course = input("enter your course: ")
        if course.lower() == "web-development":
            print("go to next class")
        else:
            print("your course is not here")
    elif status.lower() == "3":
        course = input("Enter your course: ")
        if course.lower() == "data-analysis":
            print("go outside!")
        else:
            print("you are not welcome")
    else:
        print("you are not supposed to be here!")
else:
    print("go home")