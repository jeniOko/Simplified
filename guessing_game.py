import random
rules = '''
                 SECRET NUMBER GUESSING GAME
                 
1. You are trying to guess a secret number between 0 and 100
2. "Too high" and "too low" indicates that the difference between your guess and the secret number is more than or less than 20.
3. Lower and higher indicates a difference of less than 20
4. This is a good ice-breaking activity and a lottery winning selection for a token.

   ALL THE BEST!!
   
'''
print(rules)
def guess(x):
    random_number =random.randint(1, x)
    guess = 0
    num_guesses = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        num_guesses += 1
        if guess < random_number and (random_number - guess) < 20:
            print('Your guess is lower ')
        elif guess < random_number and (random_number - guess) > 19:
            print('Your guess is too low ')
        elif guess > random_number and (guess - random_number) < 20:
            print(' Your Guess is higher')
        elif guess > random_number and (guess - random_number) > 20:
            print('Your guess is too high')
    print(f' CONGRATULATIONS !!!! Your guessed it right. The secret number is {random_number} \n It took you {num_guesses} guesses!')
limit = 100
guess(limit)
