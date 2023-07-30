import time
import random


class GameDescription:
    @staticmethod
    def print_delay(text, delay=1):
        print(text)
        time.sleep(delay)

    @staticmethod
    def magical_forest():
        GameDescription.print_delay("You find yourself in a magical forest, "
                                    "surrounded by vibrant flowers and "
                                    " talking animals.")
        GameDescription.print_delay("As you explore the forest, you encounter "
                                    " a small, blue smurf looking "
                                    "lost and confused.")
        GameDescription.print_delay("The smurf tells you that they are a new "
                                    "university student in this"
                                    " enchanted world, "
                                    " but they have lost their way.")
        GameDescription.print_delay("You decide to help the smurf navigate "
                                    "through this mystical realm and make "
                                    "their journey easier.")

    @staticmethod
    def university():
        GameDescription.print_delay("You and the smurf arrive at the magical "
                                    "university, where they will learn to "
                                    "master their smurf powers.")
        GameDescription.print_delay("The university is bustling with students "
                                    "from various magical species, each "
                                    "learning unique abilities.")
        GameDescription.print_delay("The smurf is excited to begin their "
                                    "studies and thanks you for "
                                    "your assistance.")

    @staticmethod
    def mystical_cave():
        GameDescription.print_delay("You and the smurf "
                                    "stumble upon a mystical "
                                    "cave filled with glowing crystals.")
        GameDescription.print_delay("The cave holds ancient "
                                    "knowledge and powerful artifacts.")
        GameDescription.print_delay("You both explore the cave "
                                    "carefully, and the smurf discovers"
                                    " rare magical amulet.")
        GameDescription.print_delay("This amulet will enhance their "
                                    "abilities and aid them on their journey.")

    @staticmethod
    def enchanted_lake():
        GameDescription.print_delay("You and the smurf come across "
                                    "a serene Enchanted Lake shimmering "
                                    "in the moonlight.")
        GameDescription.print_delay("The lake has magical properties "
                                    "that can reveal hidden truths.")
        GameDescription.print_delay("Together, you and the smurf uncover "
                                    "valuable insights about their "
                                    "magical abilities.")

    @staticmethod
    def dragon_lair():
        GameDescription.print_delay("While exploring, you stumble "
                                    "upon the dreaded Dragon's Lair.")
        GameDescription.print_delay("The smurf must summon all their courage "
                                    "to face the mighty dragon guarding "
                                    "a precious treasure.")
        GameDescription.print_delay("The outcome of this encounter will"
                                    " determine the smurf's fate in "
                                    "the magical world.")

    @staticmethod
    def defeat_monster():
        GameDescription.print_delay("While traveling through the forest, "
                                    "a fearsome monster blocks your path.")
        GameDescription.print_delay("The smurf bravely faces the monster "
                                    "with their newfound abilities.")
        GameDescription.print_delay("After a thrilling battle, the smurf "
                                    "emerges victorious, and the "
                                    "monster retreats.")
        GameDescription.print_delay("The smurf's confidence in "
                                    "their abilities "
                                    "grows, thanks to your guidance.")

    @staticmethod
    def win_game():
        GameDescription.print_delay("Congratulations! With your help, the "
                                    "smurf successfully overcame all "
                                    "challenges and became a skilled wizard.")
        GameDescription.print_delay("They are now a renowned member of the "
                                    "magical community, admired for their "
                                    "bravery and kindness.")
        GameDescription.print_delay("You have made a lifelong friend in the "
                                    "smurf, and together, you continue to "
                                    "explore the wonders of the magical "
                                    "world.")

    @staticmethod
    def lose_game():
        GameDescription.print_delay("Unfortunately, the challenges proved to "
                                    "be too much for the smurf to handle "
                                    "alone.")
        GameDescription.print_delay("Feeling disheartened, they decide to "
                                    "return to their village and give up on "
                                    "their magical dreams.")
        GameDescription.print_delay("While their journey ends here, they will "
                                    "always remember the friendship and "
                                    "guidance you offered.")


def play_again():
    while True:
        choice = input("Do you want to continue the game? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no.'")


def game():
    while True:
        GameDescription.magical_forest()
        while True:
            choice = input("What would you like to do?\n(Enter 1 to accompany "
                           "the smurf to the magical university, or 2 to "
                           "explore the mystical cave.)\n")
            if choice == "1":
                GameDescription.university()
                if random.choice([True, False]):
                    GameDescription.defeat_monster()
                    GameDescription.win_game()
                else:
                    GameDescription.lose_game()
            elif choice == "2":
                GameDescription.mystical_cave()
                if random.choice([True, False]):
                    GameDescription.enchanted_lake()
                    GameDescription.win_game()
                else:
                    GameDescription.lose_game()
            else:
                print("Invalid input. Please enter 1 or 2.")
                continue

            if not play_again():
                GameDescription.print_delay("Thank you for playing! Goodbye!")
                return


if __name__ == "__main__":
    game()
