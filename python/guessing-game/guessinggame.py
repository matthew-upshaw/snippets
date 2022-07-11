import random

game_on = True
guess_made = False
asking = True
player_win = False
starting_attempts = 7
answer_choices = ['y','n']

while game_on:
    number = random.randint(1, 100)
    attempts = starting_attempts

    print(f"Welcome to the python number guessing game!\
        \nI'm thinking of a number between 1 and 100, and I'll give you {starting_attempts} attempts to guess it correctly.")
    
    playing = str(input('Would you like to play? Enter y/n: '))

    while asking:
        if playing not in answer_choices:
           playing = str(input('\nPlease enter either y or n only. '))
        else:
            asking = False  
    
    if playing == 'n':
        break

    while attempts > 0:
        if attempts == starting_attempts and not guess_made:
            while True:
                try:
                    player_guess = int(input('\nGreat! Enter your first guess: '))
                except:
                    print('\nThat is not a valid guess!')
                else:
                    break
        else:
            while True:
                try:
                    player_guess = int(input(f'Try again. You have {attempts} attempts remaining. '))
                except:
                    print('\nThat is not a valid guess!')
                else:
                    break

        if player_guess not in range(1,101):
            print('\nThat is not a valid guess!')
            guess_made = True

        elif player_guess == number:
            print('\nYou correctly guessed my number! You win!')
            player_win = True
            break

        elif player_guess > number:
            attempts -= 1
            print('\nToo High!')

        elif player_guess < number:
            attempts -= 1
            print('\nToo Low!')

    if not player_win:
        print(f'I win! My number was {number}. You were only {abs(player_guess-number)} off!')

    play_again = str(input(f'\nWould you like to play again? Enter y/n: '))
    asking = True

    while asking:
        if play_again not in answer_choices:
           play_again = str(input('\nPlease enter either y or n only. '))
        else:
            asking = False

    if play_again == 'n':
        game_on = False


print('\nThanks, see you next time!')