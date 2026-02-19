"""
Vehicle Management System

This module implements a vehicle management system using Object-Oriented Programming
principles including abstraction, inheritance, encapsulation, and polymorphism.
"""

from abc import ABC, abstractmethod
from typing import List


class Vehicle(ABC):
    """
    Abstract base class representing a generic vehicle.

    Attributes:
        make (str): The manufacturer of the vehicle
        model (str): The model name of the vehicle
        year (int): The year the vehicle was manufactured
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Initialize a Vehicle object.

        Args:
            make (str): The manufacturer of the vehicle
            model (str): The model name of the vehicle
            year (int): The year the vehicle was manufactured

        Raises:
            ValueError: If year is not a positive integer or if make/model are empty
            TypeError: If arguments are not of the correct type
        """
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < 1886 or year > 2100:  # First car was invented in 1886
            raise ValueError("Year must be between 1886 and 2100")

        self._make = make.strip()
        self._model = model.strip()
        self._year = year

    @property
    def make(self) -> str:
        """Get the vehicle's make."""
        return self._make

    @property
    def model(self) -> str:
        """Get the vehicle's model."""
        return self._model

    @property
    def year(self) -> int:
        """Get the vehicle's year."""
        return self._year

    @abstractmethod
    def vehicle_type(self) -> str:
        """
        Abstract method to return the type of vehicle.

        Returns:
            str: A description of the vehicle type
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the vehicle."""
        return f"{self._year} {self._make} {self._model}"


class Car(Vehicle):
    """
    Car class representing a car vehicle.

    Attributes:
        make (str): The manufacturer of the car
        model (str): The model name of the car
        year (int): The year the car was manufactured
        num_doors (int): The number of doors on the car
    """

    def __init__(self, make: str, model: str, year: int, num_doors: int):
        """
        Initialize a Car object.

        Args:
            make (str): The manufacturer of the car
            model (str): The model name of the car
            year (int): The year the car was manufactured
            num_doors (int): The number of doors on the car

        Raises:
            ValueError: If num_doors is not between 2 and 5
            TypeError: If num_doors is not an integer
        """
        super().__init__(make, model, year)

        if not isinstance(num_doors, int):
            raise TypeError("Number of doors must be an integer")
        if num_doors < 2 or num_doors > 5:
            raise ValueError("Number of doors must be between 2 and 5")

        self._num_doors = num_doors

    @property
    def num_doors(self) -> int:
        """Get the number of doors."""
        return self._num_doors

    def vehicle_type(self) -> str:
        """
        Return the type of vehicle.

        Returns:
            str: A description indicating this is a car with door count
        """
        return f"Car with {self._num_doors} doors"

    def __str__(self) -> str:
        """Return a detailed string representation of the car."""
        return f"{super().__str__()} - {self.vehicle_type()}"


class Motorbike(Vehicle):
    """
    Motorbike class representing a motorcycle vehicle.

    Attributes:
        make (str): The manufacturer of the motorbike
        model (str): The model name of the motorbike
        year (int): The year the motorbike was manufactured
        has_sidecar (bool): Whether the motorbike has a sidecar
    """

    def __init__(self, make: str, model: str, year: int, has_sidecar: bool):
        """
        Initialize a Motorbike object.

        Args:
            make (str): The manufacturer of the motorbike
            model (str): The model name of the motorbike
            year (int): The year the motorbike was manufactured
            has_sidecar (bool): Whether the motorbike has a sidecar

        Raises:
            TypeError: If has_sidecar is not a boolean
        """
        super().__init__(make, model, year)

        if not isinstance(has_sidecar, bool):
            raise TypeError("has_sidecar must be a boolean")

        self._has_sidecar = has_sidecar

    @property
    def has_sidecar(self) -> bool:
        """Get whether the motorbike has a sidecar."""
        return self._has_sidecar

    def vehicle_type(self) -> str:
        """
        Return the type of vehicle.

        Returns:
            str: A description indicating this is a motorbike with/without sidecar
        """
        sidecar_status = "with sidecar" if self._has_sidecar else "without sidecar"
        return f"Motorbike {sidecar_status}"

    def __str__(self) -> str:
        """Return a detailed string representation of the motorbike."""
        return f"{super().__str__()} - {self.vehicle_type()}"


class VehicleManagementSystem:
    """
    A system to manage a collection of vehicles.

    Attributes:
        vehicles (List[Vehicle]): A list of vehicle objects
    """

    def __init__(self):
        """Initialize the vehicle management system with an empty list."""
        self._vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """
        Add a vehicle to the management system.

        Args:
            vehicle (Vehicle): The vehicle object to add

        Raises:
            TypeError: If the provided object is not a Vehicle instance
        """
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only Vehicle objects can be added")
        self._vehicles.append(vehicle)
        print(f"✓ Added: {vehicle}")

    def display_all_vehicles(self) -> None:
        """Display all vehicles in the system."""
        if not self._vehicles:
            print("No vehicles in the system.")
            return

        print("\n" + "=" * 60)
        print("VEHICLE MANAGEMENT SYSTEM - ALL VEHICLES")
        print("=" * 60)

        for idx, vehicle in enumerate(self._vehicles, 1):
            print(f"\n{idx}. {vehicle}")
            print(f"   Type: {vehicle.vehicle_type()}")

        print("\n" + "=" * 60)

    def demonstrate_polymorphism(self) -> None:
        """Demonstrate polymorphism by calling vehicle_type() on each object."""
        if not self._vehicles:
            print("No vehicles to demonstrate polymorphism.")
            return

        print("\n" + "=" * 60)
        print("DEMONSTRATING POLYMORPHISM")
        print("=" * 60)
        print("\nCalling vehicle_type() on each object:\n")

        for vehicle in self._vehicles:
            # Polymorphism: same method call, different behavior based on object type
            print(f"• {vehicle.make} {vehicle.model}: {vehicle.vehicle_type()}")

        print("\n" + "=" * 60)

    @property
    def vehicle_count(self) -> int:
        """Get the total number of vehicles in the system."""
        return len(self._vehicles)


def main():
    """Main function to demonstrate the Vehicle Management System."""
    print("=" * 60)
    print("VEHICLE MANAGEMENT SYSTEM")
    print("=" * 60)

    # Create a vehicle management system
    vms = VehicleManagementSystem()

    try:
        # Create and add various vehicles
        print("\nAdding vehicles to the system...\n")

        car1 = Car("Toyota", "Camry", 2022, 4)
        vms.add_vehicle(car1)

        car2 = Car("Tesla", "Model S", 2023, 4)
        vms.add_vehicle(car2)

        car3 = Car("Ford", "Mustang", 2021, 2)
        vms.add_vehicle(car3)

        motorbike1 = Motorbike("Harley-Davidson", "Street 750", 2020, False)
        vms.add_vehicle(motorbike1)

        motorbike2 = Motorbike("Ural", "Gear Up", 2022, True)
        vms.add_vehicle(motorbike2)

        motorbike3 = Motorbike("Yamaha", "YZF-R1", 2023, False)
        vms.add_vehicle(motorbike3)

        # Display all vehicles
        vms.display_all_vehicles()

        # Demonstrate polymorphism
        vms.demonstrate_polymorphism()

        print(f"\nTotal vehicles in system: {vms.vehicle_count}")

        # Demonstrate error handling
        print("\n" + "=" * 60)
        print("DEMONSTRATING ERROR HANDLING")
        print("=" * 60)

        print("\nAttempting to create a car with invalid year...")
        try:
            invalid_car = Car("Invalid", "Car", 1800, 4)
        except ValueError as e:
            print(f"✗ Error caught: {e}")

        print("\nAttempting to create a car with invalid number of doors...")
        try:
            invalid_car = Car("Invalid", "Car", 2020, 10)
            print(invalid_car.make)
        except ValueError as e:
            print(f"✗ Error caught: {e}")

        print("\nAttempting to add a non-vehicle object...")
        try:
            vms.add_vehicle("Not a vehicle")  # type: ignore
        except TypeError as e:
            print(f"✗ Error caught: {e}")

        print("\n" + "=" * 60)
        print("PROGRAM COMPLETED SUCCESSFULLY")
        print("=" * 60)

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
