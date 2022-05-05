#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The integer finder


def main():
    # this function is a positive or negative finder

    print("The integer finder")

    # input
    number = int(input("enter number: "))

    # process
    if number > 0:
        print("positive number")
    elif number < 0:
        print("negative number")
    else:
        print("Zero")
    print("\nDone.")


if __name__ == "__main__":
    main()
