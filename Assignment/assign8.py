import random

Bio_details = {}
command = input('Enter serial number to register or stop to quit: ').strip().lower()
while command != "stop":
    print("Welcome to NEECORP BANK!")
    customer = []
    info = ['first_name', 'middle_name', 'last_name', 'age', 'gender', 'address', 'phone_number']
    for i in info:
        information = input(f"Enter your {i}:  ")
        while i == "phone_number" and len(information) != 11:
             information = input(f"Enter your {i}:  ")
        customer.append(information)
    account_number = customer[6]
    customer.append(account_number)
    Bvn = random.randrange(1234567894500, 1234567898500)
    customer.append(Bvn)
    Bio_details.update({command : customer})
    command = input('Enter serial number to register or stop to quit: ').strip().lower()
else:
    print("Thanks for checking up on us")
print(Bio_details)