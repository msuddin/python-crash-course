age = 1
# In an if/elif/else, only one condition runs, the first one that is true
if age <= 5:
    print("Free entry")
elif age <= 10:
    print("Charge of £10 for ticket")
elif age <= 20:
    print("Charge of £20 for ticket")
else:
    print("You can go in for free")