# !/usr/bin/env python3

# created by Hertz Antonella
# created on 25. Apr. 2022
# This program generates a random number, compares
# it to the user number and keeps looping until
# they guess it right.
import random


def main():
    random_num = random.randint(0, 10)
    loop_counter = 0
    while True:
        # ask the user to guess the any number from 0 to 10.
        user_num = input("Guess any number from 0-10: ")
        print("")

        try:
            user_num = int(user_num)

            # compares the user num to random number
            # loops until they get it right
            if user_num >= 0 and user_num <= 10:
                loop_counter = loop_counter + 1

                if user_num == random_num:
                    print("correct , cogrants")
                    break
                else:
                    print(" Incorrect. Please try again.")
            else:
                print("Please enter a number from 0 to 10.")
        # handles the error case
        except Exception:
            print("Invalid input, Please enter numbers(1,2,3..)")


if __name__ == "__main__":
    main()
