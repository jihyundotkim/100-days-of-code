import random
from os import system
logo = '''
 _____                                 
|  __ \                                
| |  \/_   _  ___  ___ ___             
| | __| | | |/ _ \/ __/ __|            
| |_\ \ |_| |  __/\__ \__ \            
 \____/\__,_|\___||___/___/            
                                       
                                       
 _____ _                               
|_   _| |                              
  | | | |__   ___                      
  | | | '_ \ / _ \                     
  | | | | | |  __/                     
  \_/ |_| |_|\___|                     
                                       
                                       
 _   _                 _               
| \ | |               | |              
|  \| |_   _ _ __ ___ | |__   ___ _ __ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |   
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
'''



def number_game():
    print(logo)
    difficulty = input("Choose a difficuly. easy/hard: ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    number = random.randint(0,100)
    guessed_right = False
    remaining_attempts = attempts
    while remaining_attempts>0 and guessed_right == False:
        guess = int(input("Guess a number between 0 and 100: "))
        if guess > number:
            remaining_attempts -= 1
            print(f"Too high. You have {remaining_attempts} guesses left.")
        elif guess < number:
            remaining_attempts -= 1
            print(f"Too low. You have {remaining_attempts} guesses left.")
        else:
            remaining_attempts -=1
            print("You got it!")
            guessed_right = True
    if not guessed_right and remaining_attempts <= 0:
        print("You ran out of attempts. You lose.")
        print(f"The number was {number}")
    else:
        print(f"You guessed it in {attempts - remaining_attempts} guesses. You win!")
    if input("Would you like to go again? y/n: ") == "y":
        _ = system('cls')
        number_game()
number_game()