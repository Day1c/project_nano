import random,os,time, tkinter, customtkinter
from datetime import datetime

def return_main():
    times = 0
    print("\nYou will be directed to the main menu!")
    time.sleep(1)
    os.system('clear')
    for x in range(4):
        times += 1
        print("Returning to \u001b[33m\u001b[1mPlay2Day!\u001b[0m!\n\n" +"." * times)
        time.sleep(1)
        os.system('clear')
    
def hidden_word(word_completion):
    print(" ".join(word_completion))
    
def hangman_pics():
    figure = ['''
    +---+
        |
        |
        |
        |
        |
    =========''','''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    return figure

def get_time():
    format_time = datetime.now()
    date = format_time.strftime('%d/%m/%Y')
    current_time = format_time.strftime('%H:%M:%S')
    return date,current_time

def user_log(attempts, passed):
    print("You can now put your score with your name in a log if you dont want to give ur name you can press enter to be unknown.")
    while True:
        user_name = input("Please give ur name: ").capitalize()
        if user_name.strip() == "":
            user_name = "Unknown"
            break
        if not user_name.isalpha():
            os.system("clear")
            print("This is not a valid name")
            continue
        break
    with open("/Users/dewan/School/project nano/logs/galgje_log.txt","a") as f:
        f.write(f"\nUser name: {user_name}, guessed the word: {passed}, times guessed: {attempts}, date: {get_time()[0]}")

def players():
    while True:
        print(f"""\u001b[1m{get_time()[0]} {get_time()[1]}\u001b[0m
\u001b[32m  ______ __             __                          _                                        
 /_  __// /_   ___     / /_   ____ _ ____   ____ _ (_)____   ____ _   ____ ___   ____ _ ____ 
  / /  / __ \ / _ \   / __ \ / __ `// __ \ / __ `// // __ \ / __ `/  / __ `__ \ / __ `// __ \\
 / /  / / / //  __/  / / / // /_/ // / / // /_/ // // / / // /_/ /  / / / / / // /_/ // / / /
/_/  /_/ /_/ \___/  /_/ /_/ \__,_//_/ /_/ \__, //_//_/ /_/ \__, /  /_/ /_/ /_/ \__,_//_/ /_/ 
                                         /____/           /____/\u001b[0m
Welcome to '\u001b[42mThe hanging man\u001b[0m' """)
        player_count = input("(1) solo\n(2) duo\n\nWith how many people would you like to play 'The hanging man' (press q to quit)? ")
        if player_count == "q":
            return_main()
            return "quit"
        if not player_count.isdigit():
            print("Please give a number")
            continue
        if player_count <1 or player_count >2:
            os.system('clear')
            print("This was not an option.\n")
            continue
        player_count = int(player_count)
        break
    os.system("clear")
    if player_count == 1:
        print("You chose to play '\u001b[42mThe hanging man\u001b[0m' alone!\n")
        return "solo"
    else:
        print("You chose to play '\u001b[42mThe hanging man\u001b[0m' with someone else!\n")
        return "duo"
    
def difficulty():
    while True:
        user_difficulty = input("(1) easy\n(2) medium\n(3) hard\n\nWhat diffuculty level would you like to play (press q to quit): ")
        if user_difficulty == "q":
            return_main()
            return "quit"
        try:
            user_difficulty = int(user_difficulty)
            if user_difficulty <1 or user_difficulty >3:
                os.system('clear')
                print("This was not an option.\n")
                continue
            break

        except ValueError:
            os.system('clear')
            print("You did not give a valid answer. Try again!\n")
        
    if user_difficulty == 1:
        os.system('clear')
        print("You chose 'easy' difficulty!\n")
        return "easy"
        
    elif user_difficulty == 2:
        os.system('clear')
        print("You chose 'medium' difficulty!\n")
        return "medium"
    else:
        os.system('clear')
        print("You chose 'hard' difficulty!\n")
        return "hard"
    
def duo():
    
    while True:
        player_word = input("Please give a word for the other player to guess longer or equal to 5 letters: ")
        if not player_word.isalpha() or len(player_word) <5:
            os.system("clear")
            print("Please give a valid word thats longer than 5 letters.\n")
            continue
        else:
            os.system("clear")
            player_word = player_word.lower()
            print(f"""The word you chose for the other player to guess is '{player_word}'.
In 5 seconds you can give the laptop to the other player.""")
            time.sleep(5)
            os.system("clear")
            break

    random_word = player_word
    play_hangman(random_word)

def easy():                             #1000 words

    with open('/Users/dewan/School/project nano/galgje_words/easy_words.txt') as ab:
        from_list =[line.strip() for line in ab]
    random_word = random.choice(from_list).lower()
    play_hangman(random_word)

def medium():                            #1371 words

    with open('/Users/dewan/School/project nano/galgje_words/medium_words.txt') as ab:
        from_list =[line.strip() for line in ab]
    random_word = random.choice(from_list).lower()
    play_hangman(random_word)

def hard():                              #222 words

    with open('/Users/dewan/School/project nano/galgje_words/hard_words.txt') as ab:
        from_list =[line.strip() for line in ab]
    random_word = random.choice(from_list).lower()
    play_hangman(random_word)

def play_hangman(random_word):

    word_completion = (len(random_word)) * ["_"] 
    attempts = 0
    max_tries = 7
    guessed = []
    while attempts < max_tries:
        while True:
            print (hangman_pics()[attempts])
            hidden_word(word_completion)
            # print(random_word) ##test code and show the word
            guess = input("Guess a letter or a word: ").lower()
            os.system("clear")
            if not guess.isalpha():
                print(f"""\u001b[31mPlease give a valid guess\u001b[0m\n
You have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.""")
                continue
            if guess == random_word:
                print(f"\u001b[32mCongratulations you guessed the word '{random_word}' with {attempts} mistake(s)!!\u001b[0m\n")
                passed = "yes"
                user_log(attempts, passed)
                return "play_again"
            if len(guess) != 1 and len(guess) != len(random_word):    
                print(f"""\u001b[31mYou need to guess a letter or a word that has the length of {len(random_word)}\u001b[0m\n
You have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.\n""")
                continue
            if guess in guessed:
                print(f"""\u001b[31mYou have already guessed the letter {guess}\u001b[0m\n
You have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.\n""")
                continue
            if guess in random_word:
                print(f"\u001b[32mNice the letter '{guess}' was in the word!\n\u001b[0m")
                guessed.append(guess)
                print (f"You have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.\n")
                for i in range(len(random_word)):
                    if random_word[i] == guess:
                        word_completion[i] = guess
                        continue
            else:
                print(f"\u001b[31mThe letter '{guess}' was not in this word.\u001b[0m\n")
                attempts += 1
                break
            word = "".join(word_completion).lower()
            if word == random_word:
                print(f"\u001b[32mCongratulations, you guessed all the letters in {random_word} and it was correct!! You did this with {max_tries - attempts} attempt(s) left\u001b[0m\n")
                passed = "yes"
                user_log(attempts, passed)
                return "play_again"
        guessed.append(guess)
        guessed.sort()
        print (f"You have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.")
            

    if attempts >= max_tries:
        os.system("clear")
        passed = "no"
        print(f"""\nThe word was '{random_word}'. You killed the hanging man??

    +---+
    |   |
    \u001b[31m0\u001b[0m   |
   \u001b[31m/|\ \u001b[0m |
   \u001b[31m/ \ \u001b[0m |
        |
    =========\n""")
        user_log(attempts, passed)
        return "play_again"

if __name__ == ("__main__"):
    players()