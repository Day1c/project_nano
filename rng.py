import random,os,time  
from datetime import datetime

def return_main():
    times = 0
    os.system('clear')
    for x in range(4):
        times += 1
        print(f"Returning to \u001b[33m\u001b[1m2Day's Apps!\u001b[0m!\n\n{"." * times}")
        time.sleep(1)
        os.system('clear')

def get_time():
    format_time = datetime.now()
    return format_time.strftime('%Y-%m-%d'), format_time.strftime('%H:%M:%S')

def user_log(attempts,passed):
    user_name = input("\nPlease give ur name to log ur score (or press enter to be unknown): ").capitalize()
    if user_name.strip() == "":
        user_name = "Unknown"
    with open("/Users/dewan/School/project nano/logs/rng_log.txt","a") as f:
        f.write(f"\nUser name: {user_name}, times guessed: {attempts}, guessed the number: {passed}, date: {get_time()[0]}")

def guess_it():               
    print(f"""\u001b[1m{get_time()[0]} {get_time()[1]}\u001b[0m
\u001b[34m   ______                            __   __            __                              __               
  / ____/__  __ ___   _____ _____   / /_ / /_   ____ _ / /_   ____   __  __ ____ ___   / /_   ___   _____
 / / __ / / / // _ \ / ___// ___/  / __// __ \ / __ `// __/  / __ \ / / / // __ `__ \ / __ \ / _ \ / ___/
/ /_/ // /_/ //  __/(__  )(__  )  / /_ / / / // /_/ // /_   / / / // /_/ // / / / / // /_/ //  __// /    
\____/ \__,_/ \___//____//____/   \__//_/ /_/ \__,_/ \__/  /_/ /_/ \__,_//_/ /_/ /_//_.___/ \___//_/\u001b[0m

Welcome to the game '\u001b[44mGuess that number\u001b[0m'\n                                                                          
 """)    
    number = random.randint(0,100)         
    max_tries = 10                          
    attempts = 0                                         
    guessed_numbers = []     
    while attempts < max_tries:                   
        guess = input("Try to guess the number from 0-100 (press q to quit): ")
        if guess == "q":                    
            return_main()
            return "quit"
        try:
            guess = int(guess)
            if guess <0 or guess >100:
                os.system('clear')
                print("\u001b[31mThis number is out of range. Try again!\u001b[0m\n")
                print(f"You guessed the numbers {guessed_numbers} and still got {max_tries-attempts} tries left.\n")
                continue
        except ValueError:
            os.system('clear')
            print("\u001b[31mYou did not give a valid answer. Try again!\u001b[0m\n")
            continue
        if guess in guessed_numbers:
            os.system('clear')
            print("\u001b[31mYou already guessed this number. Please try a different number.\u001b[0m\n")
            continue
        guessed_numbers.append(guess)
        guessed_numbers.sort()
        if guess > number:
            os.system('clear')
            print("The number you guessed was too high. Try again!")
            attempts += 1
        elif guess < number:
            os.system('clear')
            print("The number you guessed was too low. Try again!")
            attempts += 1
        else:
            os.system('clear')
            print(f"""\u001b[32mCongratulations, you guessed {guess} and it was correct!! You did this with {max_tries - attempts -1 } attempt(s)\u001b[0m""")
            user_log(attempts,"yes")
            return "play_again"
        print(f"\nYou guessed the numbers {guessed_numbers} and still got {max_tries-attempts} tries left.\n")
    print("You have no more tries left ggs! If you want to try ur luck play again!")
    user_log(attempts,"no")
    return "play_again"

if __name__ == ("__main__"):
    guess_it()