



Task - 1


height = float(input("Enter your height: "))

ideal_weight_min = 18.5 * (height ** 2)
ideal_weight_max = 25 * (height ** 2)

print(f"Your recommended weight range is {round(ideal_weight_min, 2)} kg to {round(ideal_weight_max, 2)} kg")

                                                                           





Task - 2




products = {"pen": 2.5, "notebook": 5, "book": 3, "eraser": 1.5, "pant": 7}


prices = list(products.values())


tax_rate = 0.18


total_price = 0


cart = {}


total_items = 0


while total_items < 5:
    print("Products:")
    for product, price in products.items():
        print(f"{product}: {price} $")
    
    product_name = input("Enter the name of the product (Press 'q' to exit): ")
    
    if product_name == 'q':
        break
    
    if product_name in products:
        quantity = int(input(f"Enter the quantity of {product_name}: "))
        cart[product_name] = products[product_name] * quantity
        total_items += 1
    else:
        print("Please enter a valid product name.")


total_price = sum(cart.values())
tax = total_price * tax_rate
total_price += tax

print(f"Total amount (including tax): {total_price} $")


if total_price > 100:
    print("Congratulations! You have earned a 15 $ coupon!")
elif total_price > 50:
    print("Congratulations! You have earned a 10 $ coupon!")








Task - 3






distance = float(input("Enter the  kilometrs: "))
transport_mode = input("Enter the  transport (car, truck, bus): ")


cost_per_km = 0

if transport_mode == "car":
    cost_per_km = 0.50
elif transport_mode == "truck":
    cost_per_km = 1.00
elif transport_mode == "bus":
    cost_per_km = 2.00
else:
    print("Invalid transport mode. Please enter 'car', 'truck', or 'bus'.")


total_cost = distance * cost_per_km

print(f"The total cost of the trip is: ${total_cost:.2f}")













