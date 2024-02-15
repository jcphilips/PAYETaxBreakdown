from EPF import EPF
from TaxProfile import TaxProfile
import math
import sys

reverse = False
if len(sys.argv) > 1:
    if sys.argv[1] == "r":
        print("Calculating salary before deductions.")
        reverse = True
    else:
        print("Invalid argument entered.")
        print("Enter no arguments to calulcate salary after deductions.")
        print("Enter 'r' to calculate salary before deductions.")
        print("i.e. python3 main.py r")
        sys.exit(1)

epfContributor = ""
while True:
    user = None
    salary = -math.inf

    while salary < 0:
        try:
            if reverse:
                salary = float(input("Enter take home salary: "))
            else:
                salary = float(input("Enter salary: "))
        except ValueError:
            print("Must enter floating point values only!: ")
            salary = -math.inf
        if salary < 0:
            print("Cannot enter a value less than 0. Try again.")

    if epfContributor != "":
        userInput = input("Do you want to continue with the same EPF? (Y/N): ").lower()
        if userInput == 'n':
            epfContributor = ""
        if userInput == 'y':
            user = TaxProfile(salary, epfContributor)

    while epfContributor == "":
        contributes_epf = input("Do you contribute to EPF? (Y/N): ").lower()
        if contributes_epf == "y":
            epfContributor = EPF(salary, True)
        elif contributes_epf == "n":
            epfContributor = EPF(salary, False)
        else:
            print("Invalid input!")
            epfContributor = ""

    user = TaxProfile(salary, epfContributor)
    if reverse:
        user.reverse()
    print(user)

    choice = ""
    while choice == "":
        choice = input("Do you want to continue? (Y/N): ").lower()
        if choice == 'n':
            print("Thank you for using this program!\nExitting.")
            sys.exit()
        elif choice == 'y':
            print("")
            continue
        else:
            choice = ""
            print("Invalid input!")

