Problem Statement
-----------------
Hangman is a game where a player guesses letters for a random word. The player wins by guessing all of the correct letters. The player loses by running out of tries for entering incorrect letters.




Requirements
------------
- getting user input: letter
- get a random word
- user interface for user to see and guess for game progression
- lose/win conditions
- instructions/welcome message




Algorithm (Pseudocode)
----------------------
Program chooses a random word from the text file and displays "_" for each letter in the chosen word. Program prints out the game board before each guess. 
Program prompts user to input a letter, if the letter is in the randomly chosen word, program will replace the corresonding "_" with the corresponding letter(s).
If the user's guess is not in the selected word, it will add a part of the hangman to the board.
Program will add all user's guesses to an guess array and display the guesses to the user.
If the user guesses all the letters in the word, the program will end the game.
If the user makes too many wrong guesses and the full hangman is drawn, the program will end the game.


