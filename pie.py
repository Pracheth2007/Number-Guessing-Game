low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
guesses1 = 1

while low != high:
    guess = low + (high - low) / 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l or c if my guess was correct ".format(guess)).casefold()

    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        if guesses1 == 1:
            print("I got it in {} guess!".format(guesses1))
        else:
            print("I got it in {} guesses!".format(guesses1))
        break

    else:
        print("Please enter h, l or c")

    guesses1 += 1
else:
    print("Your number is {}".format(low))
    print("I got it in {} guesses".format(guesses1))