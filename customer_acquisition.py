"""
 Ahmed, an EiT Fellow, has been given an amount of GHC 50,000 for his capstone project.
25% of this amount was spent on marketing, 
50% was spent on other operational expenses, 
The remaining 25% on customer acquisition, 
It will cost him GHC 5 to acquire a customer

Your program should calculate the number of customers he can acquire with the budget allocated
"""

total_budget = 50000

marketing_cost = 50000 * 0.25

opex = 50000 * 0.5

cac = total_budget - marketing_cost - opex

number_of_customers = cac / 5

print ("Financial Statement")
print(f"Total budget: {total_budget}")
print(f"Marketing Cost: {marketing_cost}")
print(f"OPEX: {opex}")
print(f"CAC: {cac}")
print(f"Number of customers: {number_of_customers}")



