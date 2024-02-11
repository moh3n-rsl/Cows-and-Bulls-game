import random

#####
def bullsAndCows(num_str, guess_str):
    new_guess_str = ''
    
    bulls = 0
    for i in range(len(num_str)):
        if num_str[i] == guess_str[i]:
            bulls+=1
        else:
            new_guess_str += guess_str[i]
    
    cows = 0
    for i in range(len(new_guess_str)):
        if new_guess_str[i] in num_str:
            cows+=1

    return [bulls, cows]    
#####

#####
def startGame():
    num = random.randint(1000, 10_000)

    #print('Secret Code:', num)

    while True: 
        guess = ''
        while True:
            if guess.isdecimal() and len(guess) == 4: break
            guess = input('Guess: ')
        
        if int(guess) == num:
            print('You guessed right!')
            break

        arr = bullsAndCows(str(num), guess)
        print('Response:', arr[0], 'bulls', ',', arr[1], 'cows')
#####

startGame()