# Small quiz game that asks a series of four questions, tracks score, and displays it in a percentage upon completion.

playing = input("Would you like to play? Y/N: ")

if (playing.upper()) != "Y":
    quit()

print("Welcome!")
score = 0

answer = input("What does GPU stand for? ")
if (answer.upper()) == "GRAPHICS PROCESSING UNIT":
    score += 1
    print("Correct!")
else: print("Incorrect!")

answer = input("What does CPU stand for? ")
if (answer.upper()) == "CENTRAL PROCESSING UNIT":
    score += 1
    print("Correct!")
else: print("Incorrect!")

answer = input("What does RAM stand for? ")
if (answer.upper()) == "RANDOM ACCESS MEMORY":
    score += 1
    print("Correct!")
else: print("Incorrect!")

answer = input("What does PSU stand for? ")
if (answer.upper()) == "POWER SUPPLY UNIT":
    score += 1
    print("Correct!")
else: print("Incorrect!")

print("Your score is: " + str(((score / 4) * 100)) + "%")
print("You got " + str(score) + " out of 4 correct.")