#start menu to choose from the games you want to play

from rng import guess_it
from galgje import *
from weather import *
from datetime import datetime
from rock_paper_scissors import main_rps
import os,time

def main_menu():
    os.system('clear')
    while True:
        
        print(f"""\u001b[1m{get_time()[0]} {get_time()[1]}\u001b[0m
\u001b[33m   ___ _             ____     ___            
  / _ \ | __ _ _   _|___ \   /   \__ _ _   _ 
 / /_)/ |/ _` | | | | __) | / /\ / _` | | | |
/ ___/| | (_| | |_| |/ __/ / /_// (_| | |_| |
\/    |_|\__,_|\__, |_____/___,' \__,_|\__, |
               |___/                   |___/ 

Welcome to \u001b[1mPlay2Day!\u001b[0m

Available games:                 Available apps:
(1) \u001b[44mGuess that number\u001b[0m            (2) \u001b[45mThe weather app\u001b[0m 
(3) \u001b[42mThe hanging man\u001b[0m              (4) \u001b[40m...\u001b[0m
(5) \u001b[41mRock, paper ,scissors\u001b[0m        (6) Coming soon...
(7) Coming soon...
"""  
+ "_" * 75)
        play_game = input("\nPlease give the number of the game/ app that you would like to open: ")

        if not play_game.isdigit():
            os.system('clear')
            print("\u001b[31mYou did not give a valid answer.\n\u001b[m")
            continue
        else:
            play_game = int(play_game)
        if play_game < 1 or play_game > 5:
            os.system('clear')
            print(f"\u001b[31mThe game {play_game} does not exist yet. Try another game!\u001b[0m\n")
            continue 

        if play_game == 1:
            os.system('clear')
            print("You chose the game '\u001b[44mGuess that number\u001b[0m'!!!\n")
            time.sleep(1.5)
            os.system("clear")
            while True:
                result = guess_it()
                if result == "quit":
                    break
                again = play_again('\u001b[44mGuess that number\u001b[0m')
                if again == "no":
                    break

        elif play_game == 2:
            os.system('clear')
            print("You chose the app '\u001b[45mThe weather app\u001b[0m'!!!\n")
            time.sleep(1.5)
            os.system("clear")
            main_weather()

        elif play_game == 3:
            os.system('clear')
            print("You chose the game '\u001b[42mThe hanging man\u001b[0m'!!!\n")
            time.sleep(1.5)
            os.system("clear")
            while True:
                result = players()
                if result == "quit":
                    break
                if result == "solo":
                    result2 = difficulty()
                    if result2 == "quit":
                        break
                    elif result2 == "easy":
                        easy()
                        again = play_again('\u001b[42mThe hanging man\u001b[0m')
                        if again == "no":
                            break
                    elif result2 == "medium":
                        medium()
                        again = play_again('\u001b[42mThe hanging man\u001b[0m')
                        if again == "no":
                            break                        
                    hard()
                    again = play_again('\u001b[42mThe hanging man\u001b[0m')
                    if again == "no":
                        break
                duo()
                again = play_again('\u001b[42mThe hanging man\u001b[0m')
                if again == "no":
                    break 

        elif play_game == 4:
            os.system('clear')
            print("You chose the app '\u001b[40m...\u001b[0m'!!!\n")
            time.sleep(1.5)
            os.system("clear")

        elif play_game == 5:
            os.system('clear')
            print("You chose the game '\u001b[41mRock, paper ,scissors\u001b[0m'!!!\n")
            time.sleep(1.5)
            os.system("clear")
            while True:
                result = main_rps()
                if result == "quit":
                    break
                again = play_again('\u001b[41mRock, paper ,scissors\u001b[0m')
                if again == "no":
                    break

def get_time():
    format_time = datetime.now()
    date = format_time.strftime('%d/%m/%Y')
    current_time = format_time.strftime('%H:%M:%S')
    return date,current_time

def play_again(game):
    loading = 0
    while True:
        again = input("\nDo you want to play again? Y/N" ).upper()
        if again == "Y":
            os.system('clear')
            for x in range(4):
                loading += 1
                print(f"Redirecting to another game of {game}!!!\n{"." * loading}")
                time.sleep(1)
                os.system('clear')
            return "yes"
        elif again == "N":
            os.system('clear')
            for x in range(4):
                loading += 1
                print(f"Returning to \u001b[33m\u001b[1mPlay2Day!\u001b[0m!\n\n{"." * loading}")
                time.sleep(1)
                os.system('clear')
            return "no"
        else:
            print("This was not an option. Please choose Y/N.")
            os.system("clear")
            continue

if __name__ == ("__main__"):
    main_menu()