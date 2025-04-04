# Combining input with while loop and a flag
responses = {}
active_polling = True
while active_polling:
    name = input("What is your name? ")
    mountain = input("What is the mountain you like to climb? ")
    responses[name] = mountain

    continue_polling = input("Would you like to continue polling (y/n)? ")
    if continue_polling.lower() == "n":
        active_polling = False

print(f"Here is your responses: {responses}")