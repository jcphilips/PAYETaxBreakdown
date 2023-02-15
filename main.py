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

Upto 100,000									-			Relief
Exceeding 100,000 but not exceeding 141,667		-			6% - 6000
Exceeding 141,667 but not exceeding 183,333		-			12% - 14500
Exceeding 183,333 but not exceeding 225,000		-			18% - 25,500
Exceeding 225,000 but not exceeding 266,667		-			24% - 39,000
Exceeding 266,667 but not exceeding 308,333		-			30% - 55,000
Exceeding 308,333								-			36% - 73,500
"""
