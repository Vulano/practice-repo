import random

top_range_val = input("Pick a number: ")
if (top_range_val.isdigit()):
    top_range_val = int(top_range_val)

    if top_range_val <= 0:
        print('Please type a number greater than 0.')
        quit()
else:
    print("Please type a number next time.")
    quit()

rand_number = random.randint(0, top_range_val)
counter = 0

while True:
    guess_value = input("Guess the number: ")
    if (guess_value.isdigit()):
        guess_value= int(guess_value)
        if (guess_value <  rand_number):
            print("Too low. Guess higher!")
            counter += 1
        elif (guess_value > rand_number):
            print("Too high. Guess lower!")
            counter += 1
        elif (guess_value == rand_number):
            counter +=1
            print("That's correct!")
            print("It took", counter, "guesses.")
            break
    else:
        print("Please pick a number next time.")
        continue