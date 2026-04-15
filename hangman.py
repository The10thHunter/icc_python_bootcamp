answer = input("What's the word?")
winner = False
guess = input("What is the letter you want to guess?")
guess_list = []
while not winner:
    guess = input("What is the letter you want to guess?")
    for letter in answer:
        if guess == letter and letter not in guess_list:
            guess_list.append(guess)
        if letter in guess_list:
            print(guess_list)
        else: 
            print("Bad guess")
        #Tells us if our win condition is right or not:
        #print(set(list(answer)) == set(guess_list))
        if set(list(answer)) == set(guess_list):
            winner = True
            print("You win!")
            break



