import random
r = random.randint(1, 100)
yes = ['Y', 'YES', 'y', 'yes', 'ok']
cnt = 0
while True:
    n = int(input("Guess a number: "))
    if n > r:
        print("Too high!")
    elif n < r:
        print("Too low!")
    else:
        print("You guessed it right!")

    cnt +=1
    if cnt == 10:
        if input("You lost. Want to play again? ") in yes:
            cnt = 0
            r = random.randint(1, 100)
        else:
            break















