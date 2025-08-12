#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
        "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Fido", breed="Mutt"):
        # Temporarily set a flag so we know if name passed
        if self._set_name(name):
            self.breed = breed  # Only set breed if name valid

    def _set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
            return True
        else:
            print("Name must be string between 1 and 25 characters.")
            return False

    @property
    def name(self):
        return getattr(self, "_name", None)

    @name.setter
    def name(self, value):
        self._set_name(value)

    @property
    def breed(self):
        return getattr(self, "_breed", None)

    @breed.setter
    def breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
