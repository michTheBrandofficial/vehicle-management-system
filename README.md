# Vehicle Management System

A comprehensive Python application demonstrating Object-Oriented Programming (OOP) principles through a vehicle management system.

## 📋 Overview

This project implements a vehicle management system that showcases key OOP concepts including:
- **Abstraction** - Abstract base class for vehicles
- **Inheritance** - Specialized vehicle types (Car, Motorbike)
- **Encapsulation** - Private attributes with property accessors
- **Polymorphism** - Different behaviors for the same method call

## 🚀 Features

- ✅ Abstract `Vehicle` base class with common attributes
- ✅ `Car` and `Motorbike` subclasses with unique attributes
- ✅ Comprehensive input validation and error handling
- ✅ Vehicle collection management
- ✅ Polymorphism demonstration
- ✅ Well-documented, clean code
- ✅ Type hints for better code clarity

## 📁 Project Structure

```
vehicle-management-system/
│
├── main.py          # Main application file
└── README.md        # Project documentation
```

## 🏗️ Class Architecture

### Vehicle (Abstract Base Class)
**Attributes:**
- `make` (str) - Vehicle manufacturer
- `model` (str) - Vehicle model name
- `year` (int) - Manufacturing year

**Methods:**
- `vehicle_type()` - Abstract method to be implemented by subclasses

### Car (Inherits from Vehicle)
**Additional Attributes:**
- `num_doors` (int) - Number of doors (2-5)

**Methods:**
- `vehicle_type()` - Returns car type with door count

### Motorbike (Inherits from Vehicle)
**Additional Attributes:**
- `has_sidecar` (bool) - Whether the motorbike has a sidecar

**Methods:**
- `vehicle_type()` - Returns motorbike type with sidecar status

### VehicleManagementSystem
**Methods:**
- `add_vehicle(vehicle)` - Add a vehicle to the system
- `display_all_vehicles()` - Display all registered vehicles
- `demonstrate_polymorphism()` - Show polymorphic behavior
- `vehicle_count` - Property returning total vehicle count

## 🔧 Requirements

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

## 💻 Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd vehicle-management-system
```

2. No additional installation needed - uses Python standard library only!

## ▶️ Usage

Run the program using Python:

```bash
python main.py
```

### Expected Output

The program will:
1. Create multiple vehicle instances (cars and motorbikes)
2. Add them to the management system
3. Display all vehicles with their details
4. Demonstrate polymorphism by calling `vehicle_type()` on each object
5. Show error handling examples

### Sample Output

```
============================================================
VEHICLE MANAGEMENT SYSTEM
============================================================

Adding vehicles to the system...

✓ Added: 2022 Toyota Camry - Car with 4 doors
✓ Added: 2023 Tesla Model S - Car with 4 doors
✓ Added: 2021 Ford Mustang - Car with 2 doors
✓ Added: 2020 Harley-Davidson Street 750 - Motorbike without sidecar
✓ Added: 2022 Ural Gear Up - Motorbike with sidecar
✓ Added: 2023 Yamaha YZF-R1 - Motorbike without sidecar

============================================================
VEHICLE MANAGEMENT SYSTEM - ALL VEHICLES
============================================================

1. 2022 Toyota Camry - Car with 4 doors
   Type: Car with 4 doors

2. 2023 Tesla Model S - Car with 4 doors
   Type: Car with 4 doors

...
```

## 🎯 Code Examples

### Creating Vehicles

```python
# Create a car
car = Car("Toyota", "Camry", 2022, 4)

# Create a motorbike
motorbike = Motorbike("Harley-Davidson", "Street 750", 2020, False)
```

### Using the Management System

```python
# Initialize the system
vms = VehicleManagementSystem()

# Add vehicles
vms.add_vehicle(car)
vms.add_vehicle(motorbike)

# Display all vehicles
vms.display_all_vehicles()

# Demonstrate polymorphism
vms.demonstrate_polymorphism()
```

### Error Handling

The system includes comprehensive error handling:

```python
# Invalid year (too old)
try:
    car = Car("Invalid", "Car", 1800, 4)
except ValueError as e:
    print(f"Error: {e}")  # Year must be between 1886 and 2100

# Invalid number of doors
try:
    car = Car("Invalid", "Car", 2020, 10)
except ValueError as e:
    print(f"Error: {e}")  # Number of doors must be between 2 and 5


# Invalid type
try:
    vms.add_vehicle("Not a vehicle")
except TypeError as e:
    print(f"Error: {e}")  # Only Vehicle objects can be added
```

## 🛡️ Input Validation

The system validates:
- ✅ Make and model are non-empty strings
- ✅ Year is between 1886 (first car invented) and 2100
- ✅ Number of doors is between 2 and 5
- ✅ has_sidecar is a boolean value
- ✅ Only Vehicle instances can be added to the system

## 🎓 Learning Objectives

This project demonstrates:

1. **Abstraction**: Using ABC (Abstract Base Class) to define a contract
2. **Inheritance**: Creating specialized classes from a base class
3. **Encapsulation**: Using private attributes and property decorators
4. **Polymorphism**: Same method call producing different results based on object type
5. **Error Handling**: Comprehensive validation and exception handling
6. **Type Hints**: Modern Python type annotations
7. **Documentation**: Clear docstrings and comments

## 🔍 Key OOP Concepts Demonstrated

### Abstraction
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def vehicle_type(self) -> str:
        pass
```

### Encapsulation
```python
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self._make = make  # Private attribute

    @property
    def make(self) -> str:
        return self._make  # Controlled access
```

### Polymorphism
```python
for vehicle in vehicles:
    print(vehicle.vehicle_type())  # Different behavior per type
```

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Created as a demonstration of Object-Oriented Programming principles in Python.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Happy Coding! 🚗🏍️**