#!/usr/bin/env python3
class Dog:
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

    def __init__(self, name="Fido", breed="Pug"):  # <-- ADDED DEFAULT NAME VALUE
        # Validate name
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = None  
        else:
            self.name = name

        # Validate breed
        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = None  
        else:
            self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Example usage
if __name__ == "__main__":
    fido = Dog(breed="Pug")  # Now this works!
    print(f"Dog created: {fido.name}, {fido.breed}")
