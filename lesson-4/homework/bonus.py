import random
l = ["Rock", "Paper", "Scissors"]
score_r = 0
score_p = 0
while True:
    r = random.choice(l)
    p = input("Enter your choice: ")
    if r == p:
        print("Tie")
        print ("Your score:", score_p)
        print("Computer's score:", score_r)
    elif (r == l[0] and p == l[1]) or (r == l[1] and p == l[2]) or (r == l[2] and p == l[0]):
        score_p += 1
        print("You won!")
        print ("Your score:", score_p)
        print("Computer's score:", score_r)
    elif (p == l[0] and r == l[1]) or (p == l[1] and r == l[2]) or (p == l[2] and r == l[0]):
        score_r += 1
        print("You lose")
        print ("Your score:", score_p)
        print("Computer's score:", score_r)
    
    if score_p == 5:
        print('''Congrats!!!
               You won the game!''')
        break
    elif score_r == 5:
        print("You loose the game")
        break

