# Author   : Minh Truong
# Email    : qtruong@umass.edu
# Spire ID : 35727586

apple = int(input("Enter the total apples: "))
basket = int(input("Enter the total baskets: "))
apb = apple//basket
leftapp = apple%basket

print(f"{basket} baskets can be divided as:\n{apb} apples per basket, and\n{leftapp} leftover apples. ")