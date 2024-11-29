# Write your code here
sale = {
	"Bubblegum": 202,
	"Toffee": 118,
	"Ice cream": 2250,
	"Milk chocolate": 1680,
	"Doughnut": 1075,
	"Pancake": 80
}

revenue = 0

print("Earned amount:")


for item in sale:
	print(f"{item}: ${sale[item]}")

for item in sale:
	revenue += sale[item]

print(f"Income: ${revenue}")
staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))

income = revenue - staff_expenses - other_expenses

print(f"\nNet income: ${income}")
