import random

high_range = input("Type a number ")
if high_range.isdigit():
    high_range = int(high_range)
    if high_range <= 0:
        print('Please type a number larger than 0')
        quit()
else:
    print('please type a number next time.')
    quit()
num = random.randint(0, high_range)
trials = 0

while True:
    trials +=  1
    guess_num = input("Make guess: ")
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("please type a number next time.")
        continue

    if guess_num == num:
        print("You got it right")
        break
    elif guess_num > num:
        print('You were above the number!!!')
    else:
        print('Yow were below the number')
print('You got it in', trials, "trials")
