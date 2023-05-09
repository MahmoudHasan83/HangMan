import typing
import random


class HangMan:
    """This is the Main Class for The HangMan game"""

    def __init__(self):
        self.possiblewords = [
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
        self.word_to_find = random.choice(self.possiblewords).lower()
        self.lives = 5
        self.correctly_guessed_letters = list("_" * len(self.word_to_find))
        self.wrongly_guessed_letters = []
        self.error_count = 0
        self.turn_count = 1

    def play(self):
        while True:
            char = input(f"Please Enter one letter\n")
            if char.isalpha() == True and len(char) == 1:  # checking if entry is valid
                if char in self.word_to_find:  # condition when character is found
                    for i in range(len(self.word_to_find)):
                        if self.word_to_find[i] == char:
                            self.correctly_guessed_letters[i] = char  # adding letter
                    self.turn_count += 1
                    break

                else:  # condition when there is no match
                    self.wrongly_guessed_letters.append(char)
                    self.error_count += 1
                    self.lives -= 1
                    self.turn_count += 1
                    break

            else:  # If entry were invalid print and reloop
                print(f"Please only one character is acceptable")
                continue

    def game_over(self):
        print("Sorry you couldnt find the word")

    def well_played(self):
        print(
            f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!"
        )

    def start_game(self):
        while True:
            self.play()
            if self.lives == 0:
                self.game_over()
                break
            elif self.correctly_guessed_letters == list(self.word_to_find):
                self.well_played()
                break
            else:
                print(*self.correctly_guessed_letters)
                print(" ".join(self.wrongly_guessed_letters))
                print(f"You are left with {self.lives} lives")
                print(f"You have made {self.error_count} Errors")
                print(f"This is the {self.turn_count} turn")
