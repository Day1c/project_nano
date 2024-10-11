import os, random, time
from datetime import datetime

def display_hand_player():

    hands = ["""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    """
        _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """]
    return hands

def display_hand_npc():
    hands = ["""
        _______
       (____   '---
      (_____)
      (_____)
       (____)
        (___)__.---
    """,

    """
        _______
   ____(____    '---
  (______
 (_______
  (_______
     (__________.---
    """,

    """
        _______
   ____(____    '---
  (______
 (___________
       (____)
        (___)__.---
    """]
    return hands

def get_time():
    format_time = datetime.now()
    return format_time.strftime('%Y-%m-%d'), format_time.strftime('%H:%M:%S')

def user_log(score_player, score_npc, won):
    user_name = input("Please give ur name to log ur score (or press enter to be unknown): ").capitalize()
    if user_name.strip() == "":
        user_name = "Unknown"
    with open("/Users/dewan/School/project nano/logs/rock_paper_scissors_log.txt","a") as f:
        f.write(f"\nUser name: {user_name}, won the game: {won}, player score: {score_player}, npc score: {score_npc}, date: {get_time()[0]}")

def return_main():
    times = 0
    os.system("clear")
    for x in range(4):
        times += 1
        print(f"Returning to \u001b[33m\u001b[1m2Day's Apps!\u001b[0m!\n\n{"." * times}")
        time.sleep(1)
        os.system('clear')

def main_rps():
    score_player = 0
    score_npc = 0
    answers = {"rock" : 0, "paper" : 1, "scissors" : 2}

    print(f"""\u001b[1m{get_time()[0]} {get_time()[1]}\u001b[0m
\u001b[31m    ____             __                                                   _                          
   / __ \____  _____/ /__     ____  ____ _____  ___  _____     __________(_)_____________  __________
  / /_/ / __ \/ ___/ //_/    / __ \/ __ `/ __ \/ _ \/ ___/    / ___/ ___/ / ___/ ___/ __ \/ ___/ ___/
 / _, _/ /_/ / /__/ ,< _    / /_/ / /_/ / /_/ /  __/ /     _ (__  ) /__/ (__  |__  ) /_/ / /  (__  ) 
/_/ |_|\____/\___/_/|_( )  / .___/\__,_/ .___/\___/_/     ( )____/\___/_/____/____/\____/_/  /____/  
                      |/  /_/         /_/                 |/\u001b[0m                                         

Welcome to the game '\u001b[41mRock, paper ,scissors\u001b[0m'\n """)
    while score_player <2 and score_npc <2:

        npc_choice = random.choice(list(answers.keys()))
        npc_answer = answers[npc_choice]
        player_choice = input("What would you like to choose? rock/paper/scissors (press q to quit): ").lower()
        os.system("clear")
        if player_choice == "q":                    
                return_main()
                return "quit"
        if not player_choice in answers:
            print("\u001b[31mPlease choose between 'rock', 'paper' or 'scissors'.\u001b[0m\n")
            print(f"The score is player: {score_player} opponent: {score_npc}\n")
            continue
        os.system("clear")

        player_answer = answers[player_choice]

        if eval("player_answer == npc_answer"):
            print(f"You chose {player_choice} and so did the oponent. Its a draw!\n")
        elif player_answer == 0 and npc_answer == 1 or player_answer == 1 and npc_answer == 2 or player_answer == 2 and npc_answer == 0:
            print(f"\u001b[31mYou chose {player_choice} and the opponent chose {npc_choice}. You lost this round.\u001b[0m\n")
            score_npc += 1
        else:
            print (f"\u001b[32mYou chose {player_choice} and the opponent chose {npc_choice}. You won this round.\u001b[0m\n")
            score_player +=1

        print(f"The score is player: {score_player} opponent: {score_npc}\n")

        player_hand = display_hand_player()[player_answer].splitlines()
        npc_hand = display_hand_npc()[npc_answer].splitlines()

        for player_line, npc_line in zip(player_hand, npc_hand):
            print(f"{player_line:23} {npc_line}")
    if score_npc == 2:
        print("You lost the game of '\u001b[41mRock, paper ,scissors\u001b[0m'. Try again if you think you can beat me hehehe.")
        user_log(score_player, score_npc, "no")
    else:
        print(f"Congratulations you won '\u001b[41mRock, paper ,scissors\u001b[0m' against me.")
        user_log(score_player, score_npc, "yes")
    return "play_again"

if __name__ == "__main__":
    main_rps()