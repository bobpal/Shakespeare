import random
import time
#This program generates a string of random letters and matches it with the user's string
#It does this until it's guess is the same as the user's string
#It also displays closest guess so far and time it took to guess


def generate():
    # generate random letter for each char of string
    for c in range(size):
        guess[c] = random.choice(alpha)


def count():
    # count how many letters match
    same = 0
    for c in range(size):
        if guess[c] == solution[c]:
            same += 1
    return same


print("They say if you lock a monkey in a room with a typewriter and enough time,")
print("the monkey would eventually type a work of Shakespeare by random key presses.")
print("Let's see how well a python does...'")

user = ""
bad_input = True
while bad_input:
    # Make sure user only inputs letters
    user = input("Enter a word\n(5 letters or less is recommended)\n")
    if user.isalpha():
        bad_input = False

solution = list(user.lower())
size = len(solution)
guess = [""] * size
alpha = list("abcdefghijklmnopqrstuvwxyz")
random.seed()
success = False
best = 0    # largest number of correct letters so far
start = time.time()    # start timer

while not success:
    # if number of correct letters = length of word
    generate()
    correct = count()
    if correct == size:
        success = True
    elif correct > best:
        print("The best guess so far is: ", end="")
        print("".join(guess))
        best = correct  # update best guess so far

finish = time.time()    # stop timer
speed = finish - start

print("Success!")
print("It took " + str(speed) + " seconds for the python to type ", end="")
print("\"" + "".join(guess) + "\"")
print("Press Enter to exit")
input()