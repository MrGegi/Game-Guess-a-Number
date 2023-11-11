import random
player_name = None
max_number = None
max_attempts = None
attempts_left = None
max_error = None

def randomizer(max_number):
    """Takes an int as a atribute.
    Just generates a random number.
    Simple as fuck."""
    print("Bzzzzz Bzzzzz Bzzzzzzzzzzzzz Random number is being genareted.")
    return random.randrange(0, max_number + 1)   
def get_rules():
    """Starting function.
    Needs no atribute.
    Takes input from user to determine game rules:
    -name
    -max generated number
    -max attempts to guess a number 
    -max acceptable error
    """
    global player_name
    global max_number
    global max_attempts
    global max_error

    player_name = (input("What's your name: "))
    player_name = player_name.lower()
    player_name = player_name.title() # Format string just so it looks good.
    while True:
        try:
            max_number = int(input("Enter max generated number: "))
        except:
            print("Oooops. You didnt enter a proper value. Try again.")
            continue
        break
    while True:
        try:
            max_attempts = int(input("Enter max attempts to quess a number: "))
        except:
            print("Oooops. You didnt enter a proper value. Try again.")
            continue
        break
    while True:
        try:
            max_error = int(input("Enter max acceptable error: "))
        except:
            print("Oooops. You didnt enter a proper value. Try again.")
            continue
        break
    print(f"{player_name} you've set a rules of the game:")
    print(f'Maximum possible generated number: {max_number}')
    print(f'Maximum attempts to guess a number: {max_attempts}')
    print(f'You have to guess a number within range of {max_error}')
def game():
    """Takes no atributes.
    Contains main game."""
    global max_attempts
    global attempts_left
    guess_error = None
    number_to_guess = randomizer(max_number)
    while attempts_left > 0:
        try:
            player_guess = int(input(f'{player_name} you have {attempts_left}/{max_attempts} attempts left. Enter your guess: '))
        except:
            print("You didnt enter a number!")
            continue
        attempts_left -= 1
        guess_error = number_to_guess - player_guess
        if guess_error < 0:
            guess_error *= -1 #guess error needs to be a positive number
        if guess_error == 0:
            print(f'Yes! Generated number was exactly {number_to_guess}! You won! Now go fuck yourself and play a real game.')
            break
        elif guess_error <= max_error:
            print(f'You won! Generated number was {number_to_guess}, and your guess was {player_guess} whitch is within error range of {max_error}!')
            break
        else:
            if player_guess > number_to_guess:
                print(f'Generated number is smaller than {player_guess}')
            else:
                print(f'Generated number is larger then {player_guess}')
    print(f'No more attempts! You lose. Generated number was {number_to_guess}')            
        
 
def main():
    global attempts_left
    get_rules()  
    attempts_left = max_attempts 
    game()        
        

main()
