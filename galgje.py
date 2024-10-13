import random,os,time
from datetime import datetime

def return_main():
    times = 0
    os.system("clear")
    for x in range(4):
        times += 1
        print(f"Returning to \u001b[33m\u001b[1m2Day's Apps!\u001b[0m!\n\n{"." * times}")
        time.sleep(1)
        os.system('clear')
    
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
    return format_time.strftime('%Y-%m-%d'), format_time.strftime('%H:%M:%S')

def user_log(attempts, passed, mode):
    user_name = input("Please give ur name to log ur score (or press enter to be unknown): ").capitalize()
    if user_name.strip() == "":
        user_name = "Unknown"
    with open("/Users/dewan/School/project nano/logs/galgje_log.txt","a") as f:
        f.write(f"\nUser name: {user_name}, mode: {mode}, guessed the word: {passed}, mistakes: {attempts}, date: {get_time()[0]}")

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
        choice = input("(1) solo\n(2) duo\n\nWith how many people would you like to play 'The hanging man' (press q to quit)? ")
        if choice == "q":
            return_main()
            return "quit"
        if choice == "1" or choice == "2":
            break
        os.system("clear")
        print("\u001b[31mYou did not give a valid answer.\u001b[0m\n")
    os.system("clear")
    if choice == "1":
        print("You chose to play '\u001b[42mThe hanging man\u001b[0m' alone!\n")
        return "solo"
    print("You chose to play '\u001b[42mThe hanging man\u001b[0m' with someone else!\n")
    return "duo"
    
def difficulty():
    while True:
        user_difficulty = input("(1) easy\n(2) medium\n(3) hard\n\nWhat diffuculty level would you like to play (press q to quit): ")
        if user_difficulty == "q":
            return_main()
            return "quit"
        if user_difficulty == "1" or user_difficulty == "2" or user_difficulty == "3" :
            os.system('clear')
            break
        os.system('clear')
        print("\u001b[31mYou did not give a valid answer.\u001b[0m\n")

    if user_difficulty == "1":
        os.system('clear')
        print("You chose 'easy' difficulty!\n")
        return "easy"
    elif user_difficulty == "2":
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
        if player_word.isalpha() and len(player_word) >=5:
            break
        os.system("clear")
        print("\u001b[31mPlease give a valid word thats longer than 5 letters.\u001b[0m\n")
    print(f"""\nThe word you chose for the other player to guess is '{player_word}'. In 5 seconds you can give the laptop to the other player.""")
    time.sleep(5)
    os.system("clear")

    random_word = player_word
    play_hangman(random_word,"duo")

def easy():                             #1000 words

    with open('/Users/dewan/School/project nano/galgje_words/easy_words.txt') as ab:
        from_list =[line.strip() for line in ab]
    random_word = random.choice(from_list).lower()
    play_hangman(random_word,"easy")

def medium():                            #1371 words

    with open('/Users/dewan/School/project nano/galgje_words/medium_words.txt') as ab:
        from_list =[line.strip() for line in ab]
    random_word = random.choice(from_list).lower()
    play_hangman(random_word,"medium")

def hard():                              #222 words

    with open('/Users/dewan/School/project nano/galgje_words/hard_words.txt') as ab:
        from_list =[line.strip() for line in ab]
    random_word = random.choice(from_list).lower()
    play_hangman(random_word,"hard")

def play_hangman(random_word,mode):

    word_completion = (len(random_word)) * ["_"] 
    attempts = 0
    max_tries = 7
    guessed = []
    while attempts < max_tries:
        print (hangman_pics()[attempts])
        print(" ".join(word_completion))
        # print(random_word) ##test code and show the word
        guess = input("Guess a letter or a word: ").lower()
        os.system("clear")

        if not guess.isalpha():
            print(f"\u001b[31mPlease give a valid guess\u001b[0m\n\nYou guessed the letters:{guessed} and have {max_tries - attempts} attempts left.\n")
            continue
        if guess == random_word:
            print(f"\u001b[32mCongratulations you guessed the word '{random_word}' with {attempts} mistake(s)!!\u001b[0m\n")
            user_log(attempts, "yes", mode)
            return "play_again"
        if len(guess) != 1 and len(guess) != len(random_word):    
            print(f"""\u001b[31mYou didn't guess a word with {len(random_word)} letters.\u001b[0m\nYou have guessed the letters {guessed} and have {max_tries - attempts} attempts left.\n""")
            continue
        if guess in guessed:
            print(f"""\u001b[31mYou have already guessed {guess}\u001b[0m\n\nYou have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.\n""")
            continue

        guessed.append(guess)
        guessed.sort()

        if guess in random_word:
            print(f"\u001b[32mNice the letter '{guess}' was in the word!\n\u001b[0m")
            print (f"You have guessed the letters {guessed} and you have {max_tries - attempts} attempts left.\n")
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    word_completion[i] = guess
                    continue
        else:
            print(f"\u001b[31mThe letter '{guess}' was not in this word.\u001b[0m\n\nYou have guessed the letters {guessed} and you have {max_tries - attempts} attempts left\n")
            attempts += 1
            
        word = "".join(word_completion).lower()
        if word == random_word:
            print(f"\u001b[32mCongratulations, you guessed all the letters in {random_word} and it was correct!! You did this with {max_tries - attempts} attempt(s) left\u001b[0m\n")
            user_log(attempts, "yes",mode)
            return "play_again"
    os.system("clear")
    print(f"""\nThe word was '{random_word}'. You killed the hanging man??
          
    +---+
    |   |
    \u001b[31m0 \u001b[0m  |
   \u001b[31m/|\ \u001b[0m |
   \u001b[31m/ \ \u001b[0m |
        |
    =========\n""")
    user_log(attempts, "no", mode)
    return "play_again"

if __name__ == ("__main__"):
    players()