from TaxProfile import TaxProfile
import math
import sys

while True:
    user = None
    salary = -math.inf
    while salary < 0:
        try:
            salary = float(input("Enter salary: "))
        except ValueError:
            print("Must enter floating point values only!: ")
            salary = -math.inf
        if salary < 0:
            print("Cannot enter a value less than 0. Try again.")
    epfContributor = ""
    while epfContributor == "":
        epfContributor = input("Do you contribute to EPF? (Y/N): ").lower()
        if epfContributor == "y":
            user = TaxProfile(salary, True)
        elif epfContributor == "n":
            user = TaxProfile(salary, False)
        else:
            print("Invalid input!")
            epfContributor = ""
    if len(sys.argv) > 1:
        if sys.argv[1] == "r":
            user.reverse(salary)
    print(user)

    choice = ""
    while choice == "":
        choice = input("Do you want to continue? (Y/N): ").lower()
        if choice == 'n':
            print("Thank you for using this program!\nExitting.")
            sys.exit()
        elif choice == 'y':
            print()
            continue
        else:
            choice = ""
            print("Invalid input!")

