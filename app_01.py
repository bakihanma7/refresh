# Restaurant Bill Splitter

# Step 1: Store the bill total and number of people
bill_total = 1200  # ETB
people = 4

# List of friends
friends = ["Almaz", "Dawit", "Tigist", "Bereket"]

# Step 2: Create the function
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

# Step 3: Compute the per-person amount
share = split_bill(bill_total, people)

# Step 4: Loop over the names and print each person's share
print("Restaurant Bill Splitter")
print("-" * 30)

for name in friends:
    print(f"{name} pays: {share:.0f} ETB")