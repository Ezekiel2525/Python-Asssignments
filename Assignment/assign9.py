right_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter # btw 0 and 9: "))
    guess_count += 1
    if guess == right_number:
        print('you won')
        break
else:
    print('you have exceeded the limits')

