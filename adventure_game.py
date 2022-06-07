import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(4)


def intro(item, option):
    print_pause("----Mission:  Take control of ship "
                f"so you can find the {option} on planet ZITION ----\n"
                "You have been captured after a century long, "
                "galactic battle..\n"
                "You find yourself in an hyperbaric chamber weak \n"
                "in an unknown ship."
                "The ship you are in seems to be out of control,\n"
                "drifting around the cold planet Ziton.\n")
    print_pause(f"Rumor has it that a {option} "
                "is somewhere around on planet ZITION \n"
                " and can help get the shipback on course.\n")
    print_pause("..You use your strength to lift up "
                "your head to look around.")
    print_pause("On the table near by you spot your\n")
    print_pause("handy lazer ring that you "
                "never leave or do anything without.\n")
    print_pause("You also see some emergency CHAMICAL Z near by..\n")
    print_pause("Emergency CHEMICAL Z is known "
                "to make you heal in seconds.\n")


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def cover(item, option):
    if "ring" in item:
        print_pause("\nYou sneakout of the hyperbaric chamber")
        print_pause("\nAfter a few moments of catching your breath"
                    " you hear somthing trying to open the door"
                    " and immediately administer yourself the CHEMICAL Z."
                    " with only seconds to spare ")
        print_pause("\nYou run and hide back in your hyperbaric chamber.\n")
    else:
        print_pause("\nYou  sneakout of the hyperbaric chamber,")
        print_pause("\nAllthough dizzy and seeing doubles, "
                    "you make a quick choice.")
        print_pause("\nYou run towards the table where your lazer ring lays."
                    "You use all your energy to find it and put it on.")
        print_pause("\nYou were not quiet and made alot of noise doing so!")
        print_pause("\nTheres somthing trying to get into the room."
                    "It sounds angry!")
        print_pause("\nYou run and hide in the hyperbaric chamber.\n")
        item.append("ring")
    find(item, option)


def hyper(item, option):
    print_pause("\nYou knock on the glass of the hyperbaric chamber.")
    print_pause("\nA creature walks in and administures you the CHEMICAL Z.\n"
                "You remember the creature knocked you out earlier.")
    print_pause("\nYikes! He wants you awake to question and torture you!")
    print_pause("\nThe creature grabs you by the sholders!\n")
    if "ring" not in item:
        print_pause("You have your strength back but not your ring, "
                    "your ring is all the way across the room on the table.\n")

    choice2 = valid_input("Would you like to (1) fight or (2) "
                          "try and get run towards your ring?",
                          ["1", "2"])
    if choice2 == "1":
        if "ring" in item:
            print_pause("\nAs the creature moves to attack, "
                        "you point out your ring and yell .")
            print_pause("\nThe ring begins to glow as it hypercharges "
                        "and becomes ready to be used.")

            print_pause("\nThe creature faints from the hyponotizing "
                        "glow of the ring.")
            print_pause("\nYou are victorious!"
                        "Well done! now tou can focuse on"
                        f"saving ship by finding the '{option}'."
                        ". You are victorious!\n")
        else:
            print_pause("\nYou do your best to knock it out...")
            print_pause("but the creature can only be stopped by the lazer. ")
            print_pause("\nYou have been defeated!\n")
        play_again()

    if choice2 == "2":
        print_pause("\nYou run and get your ring. "
                    "\nLuckily, you manage to get it in "
                    "time with your strength! "
                    "You are now fully equipted to protect yourself :).\n")
        find(item, option)


def find(item, option):
    print_pause("Enter 1 to knock on your hyperbaric glass chamber.")
    print_pause("Enter 2 to try and sneak out of the chamber yourself.")
    print_pause("What would you like to do?")

    choice1 = valid_input("(Please enter 1 or 2.)\n", ["1", "2"])
    if choice1 == "1":
        hyper(item, option)

    elif choice1 == "2":
        cover(item, option)


def play_again():
    again = valid_input("Play again? (y/n)", ["y", "n"]).lower()
    if again == "y":
        print_pause("\n\n\nFantastic! Restarting the system controls...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThe galaxy thanks you for playing!.\n\n\n")


def play_game():
    item = []
    option = random.choice([
        "abandond ship",
        "energy generator",
        "galatic connection tower",
        "unidentified species",
        "crystal"
    ])
    intro(item, option)
    find(item, option)


play_game()
