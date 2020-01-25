# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class Vehicle


class Vehicle():
    pass


# GroundVehicle "is a" Vehicle relationship

class GroundVehicle(Vehicle):
    pass

# FlightVehicle "is a" Vehicle relationship


class FlightVehicle(Vehicle):
    pass


# Starship "is a" FlightVehicle relationship

class Starship(FlightVehicle):
    pass


# Airplane "is a" FlightVehicle relationship

class Airplane(FlightVehicle):
    pass


# Car "is a" GroundVehicle relationship

class Car(GroundVehicle):
    pass


# Motorcycle "is a" GroundVehicle relationship

class Motorcycle(GroundVehicle):
    pass
