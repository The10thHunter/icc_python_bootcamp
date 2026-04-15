import random 

answer = random.randint(1,100)
winner = False
while(winner == False): 
    guess = int(input("Guess the number!: ")) 
    if guess == answer:
        answer = True
        break
    elif guess > answer: 
        print("Lower!")
    elif guess < answer: 
        print("Higher!")
    else: 
        pass
print("Congrats you finished!")

