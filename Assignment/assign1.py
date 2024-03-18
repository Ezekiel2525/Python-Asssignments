
firstname = input("Enter your first name: ").strip().capitalize()
lastname = input("Enter your last name: ").strip().capitalize() 
state = input("what is the name of your state?: ").strip()
country = input("Which country are you from?: ").strip()
age = int(input("What is your age?: "))
score = int(input("Enter your score: "))
print(f"my name is {firstname} {lastname}, i am from {state}, which is situated in the country {country}, i am {age} years old, i scored {score} goals for {country}")

