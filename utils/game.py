import typing
import random


class HangMan:
    """This is the Main Class for The HangMan game
    Also it has start_game() which initiates the
    play() function and control the outcome.


    """

    def __init__(self):
        """This is the initiation special method for the Hangman object"""
        self.possiblewords: list[str] = [
            "becode",
            "learning",
            "mathematics",
            "sessions",
            "chess",
            "book",
            "artificial",
            "Machine",
            "computer",
            "sunny",
            "windy",
            "beautiful",
        ]
        self.word_to_find: list[str] = list(random.choice(self.possiblewords).lower())
        self.lives: int = 5
        self.correctly_guessed_letters: list[str] = list("_" * len(self.word_to_find))
        self.wrongly_guessed_letters: list[str] = []
        self.error_count: int = 0
        self.turn_count: int = 1

    def play(self):
        """this is the play() function which is the main
        brain for decision making in the game."""
        while True:
            char = input(f"Please Enter one letter\n")
            if char.isalpha() == True and len(char) == 1:  # checking if entry is valid
                if char in self.word_to_find:  # condition when character is found
                    if (
                        char not in self.correctly_guessed_letters
                    ):  # check if char already in the guessed letters list
                        for i in range(len(self.word_to_find)):
                            if self.word_to_find[i] == char:
                                self.correctly_guessed_letters[
                                    i
                                ] = char  # adding letter
                        self.turn_count += 1
                        break
                    else:
                        print("You have already Entered that letter!")
                        break

                else:  # condition when there is no match
                    if char not in self.wrongly_guessed_letters:
                        self.wrongly_guessed_letters.append(char)
                        self.error_count += 1
                        self.lives -= 1
                        self.turn_count += 1
                        break
                    else:
                        print(
                            "For REAAALL! you have already made that error,i'll give you another chance!"
                        )
                        break

            else:  # If entry were invalid print and reloop
                print(f"Please only one character is acceptable")
                continue

    def game_over(self):
        """This method is called when you have no
        lives anymore and the game terminates"""
        print("Sorry you couldnt find the word")

    def well_played(self):
        """This method is called when you guess the
        whole words"""
        print(
            f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!"
        )

    def start_game(self):
        """The method that starts the game and
        control the output after the provoking of
        play() function"""
        while True:
            self.play()
            if self.lives == 0:
                self.game_over()
                break
            elif self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break
            else:
                print(*self.correctly_guessed_letters)
                print(" ".join(self.wrongly_guessed_letters))
                print(f"You are left with {self.lives} lives")
                print(f"You have made {self.error_count} Errors")
                print(f"This is the {self.turn_count} turn")
