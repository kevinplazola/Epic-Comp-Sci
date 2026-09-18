amount_due = 50
while amount_due > 0:
    print(f"Amount due: {amount_due}")
    payment = int(input("Coin: "))
    if payment in [25, 10, 5]:
        amount_due -= payment
    else:
        print("Invalid coin, please insert a valid coin (25, 10, or 5 cents).")
print("Change owed: 0")
if amount_due < 0:
    change_owed = -amount_due
    print(f"Change owed: {change_owed}")