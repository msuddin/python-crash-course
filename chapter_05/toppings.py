available_toppings = ['mushrooms', 'pineapple', 'peppers', 'sweetcorn']

requested_topping = ['mushrooms', 'sweetcorn']

for requested_topping in requested_topping:
    if requested_topping in available_toppings:
        print(f"{requested_topping} is available.")

print("Completed Pizza")