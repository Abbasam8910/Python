import random

word_list = ["apple", "banana", "cat", "dog", "elephant", "flower", "grass", "house", "icecream", "jacket"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
=========''']
chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
lives=6


for position in range(len(chosen_word)):
    placeholder += " _ "
game_over=False

correct_letter=[]

while not game_over:
    guess = input("Guess a Letter: \n").lower()
    print(placeholder)
    display=""
   
    for letter in chosen_word:
        if letter == guess:
            print("Right")
            display=display+guess
            correct_letter+=guess
        elif letter in correct_letter:
            display+=letter
        else:
            print("Wrong")
            display=display+" _ "

    if guess not in chosen_word:
      lives=lives-1
      if lives==0:
        game_over=True


    print(display)

    if " _ " not in display:
        game_over=True
        print("You Win") 

    print(stages[lives])
