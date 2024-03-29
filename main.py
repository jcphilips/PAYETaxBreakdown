import sys
"""
PAYE Tax Caluculator


Takes a user's salary in LKR as input, after allowances, and returns a breakdown of how the user will be taxed
for PAYE by the Sri Lankan Government.

This will not initially include taxes of non-cash benefits.


Flow:
    1. User asked to input Salary
    2. Ask if EPF/ETF contributor?
    3. Calculate PAYE tax based on salary
    4. Calculate EPF/ETF deductions
    5. Show final take home salary
    6. Show percentage of salary remaining for the month


Tax based on monthly profits from employment:

Upto 100,000                                    -           Relief
Exceeding 100,000 but not exceeding 141,667     -           6% - 6000
Exceeding 141,667 but not exceeding 183,333     -           12% - 14500
Exceeding 183,333 but not exceeding 225,000     -           18% - 25,500
Exceeding 225,000 but not exceeding 266,667     -           24% - 39,000
Exceeding 266,667 but not exceeding 308,333     -           30% - 55,000
Exceeding 308,333                               -           36% - 73,500

TODO: Add tax exemptions
TODO: Create UI
TODO: Allow creation of multiple tax profiles and save to a databse.
"""

import math

class TaxProfile:
    def __init__(self, salary, contributes_epf):
        """
        Initialises instance variables and calls member functions to calculate financial details.

        Args:
            salary (int): Monthly income of user
            contributes_epf (bool): True if user contributes a portion of their salary to EPF
        """
        self.salary = salary
        self.tax = self.calculateTax()
        self.contributes_epf = contributes_epf
        self.epf = self.calculate_epf_contribution()
        self.take_home = self.deduct()
        if self.salary > 0:
            self.take_home_pc = self.take_home/self.salary
        else:
            self.take_home_pc = 1.00
   
    def calculateTax(self):
        """
        Calculates tax based on salary income after bonuses and allowances.

        Returns:
            int: Total PAYE tax applicable
        """
        if self.salary < 100000:
            return 0
        if self.salary < 141667:
            return self.salary * 0.06 - 6000
        if self.salary < 183333:
            return self.salary * 0.12 - 14500
        if self.salary < 225000:
            return self.salary * 0.18 - 25500
        if self.salary < 266667:
            return self.salary * 0.24 - 39000
        if self.salary < 308333:
            return self.salary * 0.30 - 55000
        if self.salary > 308333:
            return self.salary * 0.36 - 73500
        return 0

    def reverseTax(self):
        """
        Calculates tax based on salary income after bonuses and allowances.

        Returns:
            int: Total PAYE tax applicable
        """
        if self.salary + self.epf < 100000:
            return (0, 0)
        if self.salary + self.epf < 139166.04:
            return (6, 6000)
        if self.salary + self.epf < 175833.04:
            return (12, 14500)
        if self.salary + self.epf < 210000:
            return (18, 25500)
        if self.salary + self.epf < 241666.9:
            return (24, 39000)
        if self.salary + self.epf < 270833.1:
            return (30, 55000)
        if self.salary + self.epf > 270833.1:
            return (36, 73500)
        return 0

    def calculate_epf_contribution(self):
        """
        Calculates user's contribution to EPF.

        Returns:
            int: User's EPF contribution
        """ 
        if self.salary > 0 and self.contributes_epf:
            base = -math.inf
            while base < 0:
                try:
                    base = float(input("Enter base salary (Salary not inclusive of bonuses or allowances): "))
                    if base > self.salary:
                        print("Base salary cannot be greater than quoted salary!")
                        base = -math.inf
                except ValueError:
                    print("Must enter floating point values only!")
                    base = -math.inf
            return base * 0.08
        return 0

    def deduct(self):
        """
        Calculates salary after deductions.

        Returns:
            int: Salary after deductions
        """    
        return self.salary - self.tax - self.epf

    def __str__(self):
        profile = f'''
Salary before deductions:   {self.salary:,.2f}
Tax:                        {self.tax:,.2f}
EPF Contribution:           {self.epf:,.2f}
Take home:                  {self.take_home:,.2f} ({self.take_home_pc:.1%})
        '''
        return profile

    def reverse(self, salary):
        self.take_home = self.salary
        (tax_percentage, relief) = self.reverseTax() 
        self.salary = (self.take_home + self.epf - relief) / (1 - tax_percentage * .01)
        self.tax = self.calculateTax()
        self.take_home_pc = self.take_home/self.salary

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
 
