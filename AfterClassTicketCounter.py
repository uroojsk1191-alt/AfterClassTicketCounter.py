
passenger_name = "Abrar Ahmed"        # str - text
destination = "Cherrapunji"           # str - text
ticket_price = 6500                   # float - decimal number
number_of_tickets = 4                 # int - whole number
is_available = True                   # bool - True or False
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: Rs", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount
