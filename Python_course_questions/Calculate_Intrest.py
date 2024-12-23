balance = float(input("Enter the initial balance (K0): "))
rate = float(input("Enter the annual interest rate (as a percentage): "))
K1 = balance * (1 + rate / 100)
print(f"Capital after 1 year (K1): {K1:.2f}")
n = int(input("Enter the number of years (n): "))
current_year = 0
current_balance = balance
while current_year < n:
    current_balance *= (1 + rate / 100)
    current_year += 1
    print(f"Year {current_year}: {current_balance:.2f}")

print(f"Capital after {n} years (Kn): {current_balance:.2f}")
