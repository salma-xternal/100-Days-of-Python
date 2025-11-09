import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages


print(logo)
print("Welcome to Hangman!!\n"
      "The goal of the game is to correctly guess a random word, letter by letter.\n"
      "You start with 6 tries/lives, and you lose one with every wrong guess.\n"
      "Good Luck!\n\n")
chosen_word = random.choice(word_list)
lives_stages = [r'''''', r'''❤
''', '''
❤❤''', '''
❤❤❤''', '''
❤❤❤❤
''', '''
❤❤❤❤❤
''', '''
❤❤❤❤❤❤
''']
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Guess word: " + placeholder)


game_over = False
right_guesses = []
lives = 6
print(f"Lives {lives_stages[lives]}")

while not game_over:
    guess = input("\nGuess a letter\n").lower()
    placeholder = ""

    if guess in right_guesses:
        print(f"You've already guessed \"{guess}\", try another letter.")

    for letter in chosen_word:
        if letter == guess:
            placeholder += letter
            right_guesses.append(guess)
        elif letter in right_guesses:
            placeholder += letter
        else:
            placeholder += "_"


    if guess not in chosen_word:
        lives -= 1
        print(lives_stages[lives])
        if lives == 0:
            game_over = True
            print("GAME OVER!")
        print("Wrong letter, you're down a life.")
        if lives == 0:
            game_over = True
            print(f"GAME OVER! \nThe word was {chosen_word}")
    print(placeholder)
    print(f'Lives: {lives_stages[lives]}')

    if "_" not in placeholder:
        game_over = True
        print("You Win!!")

    print(stages[lives])
