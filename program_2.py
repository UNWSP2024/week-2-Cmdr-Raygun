# Title: Average Age
# Author: Andrew Bittner
# Date: 9/13/2024

def average_age():

    # Get User Input
    friend1 = input("Enter a friend's age: ")
    friend2 = input("Enter another friend's age: ")
    friend3 = input("Enter yet another friend's age: ")
    friend4 = input("Enter a friend's age... again: ")
    friend5 = input("Enter a friend's age... for the last time: ")

    # Sum ages
    sum = int(friend1) + int(friend2) + int(friend3) + int(friend4) + int(friend5)

    # Average the ages
    avg = int(sum / 5)

    # Print the results
    print("Thank you very much! *Beep* *Whir*")
    print("The average age of your friend is", avg, end = ".")

# Line which calls the above function.
average_age()