# import time
# import sys

# def daily():
#     start = input("Enter 'Days' to access activities:>>> ").strip().capitalize()
#     while start == "Days":
#         username = input("Enter your name: ").strip().lower()
#         time.sleep(1)
#         print(f"WELCOME {username}, to your weekly TO-DO-LIST")
#         # print("Which of the days will you like to have access to?")
#         decide()
#     else:
#         print("Wrong code!")
#         daily()
        
# def decide():
#     print("Which of the days will you like to have access to?")
#     time.sleep(3)
#     print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday")
#     print()
#     choice = input("Enter the number for the day you have chosen:>>> ")
#     if choice == "1":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Make a Smoothie\n2. Hit the Gym\n3. Take a Shower\n4. Code for 5hours\n5. Go out for a drink")
#         print()
#         decision()
#     elif choice == "2":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Make a Smoothie\n2. Hit the Gym\n3. Go to the Bank\n4. See a Friend")
#         print()
#         decision()
#     elif choice == "3":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Make a Smoothie\n2. Hit the Gym\n3. Head to the Library\n4. Go see my Parents")
#         print()
#         decision()
#     elif choice == "4":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Make a Smoothie\n2. Hit the Gym\n3. Go for Cooking lessons\n4. Go to the Cinema")
#         print()
#         decision()
#     elif choice == "5":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Make a Smoothie\n2. Hit the Gym\n3. Go to the Cinema\n4. Travel to Santorini for the weekend\n5. Go Clubbing")
#         print()
#         decision()
#     elif choice == "6":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Hit the Gym\n2. Tour the City\n3. Watch Football\n4. Go out for a Drink")
#         print()
#         decision()
#     elif choice == "7":
#         print()
#         print("Processing...")
#         print()
#         time.sleep(2)
#         print("1. Hit the Gym\n2. Go to Church\n3. Go to the Airport\n4. Go see my Parents\n5. Go home")
#         print()
#         decision()
#     else:
#         sys.exit()

# def decision():
#     global start
#     start = input("Enter 'Days' to access activities or 'stop' to quit:>>> ").strip().capitalize()
#     while start == "Days":
#         time.sleep(2)
#         decide()
#     else:
#         sys.exit()
    

# daily()
