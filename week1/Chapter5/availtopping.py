available_topping = ['mushrooms', 'olive', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in request_toppings:
    if requested_topping in available_topping:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")