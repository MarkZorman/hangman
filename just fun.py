from random import randint
import time
import os

hangman = ["\n\n\n\n\n\n\n",
           '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
           '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
           '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
           '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
           '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
           '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
           '''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

winner = ['''
  O  
 /|\  
 ( )
''',
          '''
 \O/
  |  
 / \ 
''']

with open('words.txt', 'r') as f:
    words = f.read().split(',')

chosen_word = words[randint(0, len(words) - 1)]
word_length = len(chosen_word)
first_letter = chosen_word[0]

print("Welcome to Hangman!")
print("In this game, you'll guess letters one by one. If you guess correctly, the letter will appear in its correct position. However, if your guess is incorrect, your guesses will be decreased. Be careful with your guesses!")
print(f"The word is {word_length} letters long. The first letter of the word is {first_letter.upper()}.")

game_state = [first_letter.upper()] + ["_" for _ in range(word_length - 1)]
game_state_str = " ".join(game_state)

wrong_letters = []
correct_letters = []
lives = 7
mistakes = 0

if first_letter in chosen_word:
    print(hangman[mistakes])
    
    for i in range(1, word_length):
        if chosen_word[i] == first_letter:
            game_state[i] = first_letter

    game_state_str = " ".join(game_state)
    print(game_state_str)
    correct_letters.append(first_letter)


def check_if_guessed(letter, correct_letters, wrong_letters):
    if letter in correct_letters or letter in wrong_letters:
        print(hangman[mistakes])
        print("This letter was already guessed")
        print(f"The {'correct' if letter in correct_letters else 'wrong'} letters that you input are: {correct_letters if letter in correct_letters else wrong_letters}")
        print(game_state_str)
        return True
    return False

def check_win(game_state):
    if "_" not in game_state:
        print("You win!")
        print(f"The word was {chosen_word}. Good job!")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for i in range(100):
            if i % 2 == 0:
                print(winner[0])
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(winner[1])
                time.sleep(0.25)
                os.system('cls' if os.name == 'nt' else 'clear')
        return True
    return False

while True:
    guess = input("Input a letter: ")

    if check_if_guessed(guess, correct_letters, wrong_letters):
        continue

    if guess in chosen_word:
        print(hangman[mistakes])
        print("-------------------")
        print(f"Letter {guess} is in the secret word.")
        print("-------------------")
        
        for i in range(word_length):
            if chosen_word[i] == guess:
                game_state[i] = guess

        game_state_str = " ".join(game_state)
        print(game_state_str)
        correct_letters.append(guess)
        
        if check_win(game_state):
            break
   
    else:
        mistakes += 1
        print(hangman[mistakes])
        wrong_letters.append(guess)
        print(f"The wrong letters that you inputted are: {wrong_letters}")
        print("-------------------")
        print(f"Letter {guess} is not in the secret word.")
        lives -= 1
        print("-------------------")
        print(f"You have {lives} tries left!")
        print("-------------------")
        print(game_state_str)

        if lives == 0:
            print("You got hanged!")
            print(f"The word was {chosen_word}.")
            break
