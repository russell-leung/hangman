# russell leung, hangman.py, 

import random

#Prints the blank spaces for the letter inputs
def print_blank(blank):
  for i in range(len(blank)):
    print(blank[i], end=" ")

#Prints the board
def print_board(board):
  for r in range(len(board)):
    for c in range(len(board[0])):
      print(board[r][c], end="")
    print()

#Adds the hangman as the user makes incorrect guesses, counts incorrect answers and adds new parts of the hangman as the user answers more incorrect answers.
def draw(board):
  if(draw.counter == 0):
    board[2][6] = "O"
  if(draw.counter == 1):
    board[3][6] = "|"
  if(draw.counter == 2):
    board[3][5] = "/"
  if(draw.counter == 3):
    board[3][7] = "\\"
  if(draw.counter == 4):
    board[4][5] = "/"
  if(draw.counter == 5):
    board[4][7] = "\\"
  draw.counter += 1

#Takes the user input and finds to see if it is correct, if so it adds the correct letter to the blank spaces
def find(hangman_word, blank):
  guess = input("Take your guess: ")

  #Checks to see if guess is a letter
  if guess.isalpha() == False:
    print("Your guess was invalid.")
    return

  #Checks to see that guess is not already used
  if guess in guesses != False:
    print("You have already guessed this letter.\nGuess again.")
    return
  
  a = guess.lower()
  guesses.append(a)
  for i in range(len(hangman_word)):
    if(a == hangman_word[i]):
      blank[i] = a

  wrong = a in blank
  if(wrong == False):
    draw(board)
  print()
  print_board(board)
  print_blank(blank)
  print("\n")
  print("Guesses:", guesses)

#Takes a random word from the text file of random words
hangman_words = open("words.txt", "r").readlines()
hangman_random = random.randint(0, 851)

hangman_word = hangman_words[hangman_random]
#hangman_word = input("Enter a word: ")

#Finised_board
# [[" ", " ", " ", "_", "_", "_", "_" , " "]
# ,[" ", " ", " ", "|", " ", " ", "|", " "],
#  [" ", " ", " ", "|", " ", " ", "O", " "],
#  [" ", " ", " ", "|", " ", "/", "|", "\\"],
#  [" ", " ", " ", "|", " ", "/", " ", "\\"],
#  [" ", "_", "_", "|", "_", "_", " ", " "]] 

board = [[" ", " ", " ", "_", "_", "_", "_" , " "]
        ,[" ", " ", " ", "|", " ", " ", "|", " "],
         [" ", " ", " ", "|", " ", " ", " ", " "],
         [" ", " ", " ", "|", " ", " ", " ", " "],
         [" ", " ", " ", "|", " ", " ", " ", " "],
         [" ", "_", "_", "|", "_", "_", " ", " "]]

blank = []
guesses = []

print("Hangman\n")
print_board(board)

for i in range(len(hangman_word) - 1):
  blank.append("_")

game = True
draw.counter = 0

print_blank(blank)
print()

#Runs the game while the user has not won or lost
while(game != False):
  print()
  find(hangman_word, blank)

  #If hangman is drawn, it will end the game
  if(board[4][7] == "\\"):
    print("\nYou have lost!")
    print(f"The correct answer was: {hangman_word}")
    game = False

  #If player guesses the word correctly, it will end the game
  game2 = "_" in blank
  if(game2 == False):
    print("\nCongrats, you have guessed the correct word!")
    game = False