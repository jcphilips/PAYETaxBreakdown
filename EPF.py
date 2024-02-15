import math

class EPF:
    def __init__(self, salary, contributes_epf) -> None:
        self.contributes_epf = contributes_epf
        self.salary = salary
        self.epf = self.calculate_epf_contribution()


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

