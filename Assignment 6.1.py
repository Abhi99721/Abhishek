import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read employee information from JSON file
with open("employee.json", "r") as file:
    employee_data = json.load(file)

# Create a list of Employee objects
employee_list = []
for employee in employee_data:
    name = employee["Name"]
    dob = employee["DOB"]
    height = employee["Height"]
    city = employee["City"]
    state = employee["State"]
    emp = Employee(name, dob, height, city, state)
    employee_list.append(emp)

# Print the list of Employee objects
for emp in employee_list:
    print("Name:", emp.name)
    print("DOB:", emp.dob)
    print("Height:", emp.height)
    print("City:", emp.city)
    print("State:", emp.state)
    print()

import json

# Dictionary of Indian states and capitals
states_and_capitals = {
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur",
    "West Bengal": "Kolkata",
    "Punjab": "Chandigarh"
}

# Write the dictionary to a JSON file
with open("states.json", "w") as file:
    json.dump(states_and_capitals, file)