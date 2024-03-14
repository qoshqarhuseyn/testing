



# Task - 1


# height = float(input("Enter your height: "))

# ideal_weight_min = 18.5 * (height ** 2)
# ideal_weight_max = 25 * (height ** 2)

# print(f"Your recommended weight range is {round(ideal_weight_min, 2)} kg to {round(ideal_weight_max, 2)} kg")

                                                                           





# Task - 2



# class ShoppingCart:
#     def _init_(self):
#         self.items = {}
#         self.total_price = 0

#     def add_item(self, item_name, item_price):
#         if item_name in self.items:
#             self.items[item_name] += item_price
#         else:
#             self.items[item_name] = item_price
#         self.total_price += item_price

#     def calculate_total(self):
#         total_with_tax = self.total_price * 1.18  
#         if total_with_tax > 100:
#             return "You've earned a $15 coupon at the end!"
#         elif total_with_tax > 50:
#             return "You've earned a $10 coupon at the end!"
#         return 

# cart = ShoppingCart()


# for _ in range(5):
#     item_name = input("Enter the name of the item: ")
#     item_price = float(input("Enter the price of the item (USD): "))
#     cart.add_item(item_name, item_price)


# total_message = cart.calculate_total()
# print("Total value (including tax): ${:.2f}".format(cart.total_price * 1.18))
# print(total_message)











# Task - 3





# def calculate_trip_cost(distance, vehicle_type):
#     if vehicle_type == "car":
#         cost_per_km = 0.50
#     elif vehicle_type == "truck":
#         cost_per_km = 1.00
#     elif vehicle_type == "bus":
#         cost_per_km = 2.00
#     else:
#         print("Please enter a valid type of vehicle: car, truck, or bus")
#         return

#     total_cost = distance * cost_per_km
#     return total_cost


# distance = float(input("Enter the distance of the trip in kilometers: "))
# vehicle_type = input("Enter the type of vehicle (car, truck, or bus): ")


# total_cost = calculate_trip_cost(distance, vehicle_type)


# if total_cost is not None:
#     print("Total cost of the trip: ${:.2f}".format(total_cost))
















