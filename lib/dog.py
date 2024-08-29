#!/usr/bin/env python3

class Dog:
    pass
    def __init__(self, name, breed="Mutt"):
        self.name = name       # Assign name to self.name
        self.breed = breed     # Assign breed to self.breed, defaults to "Mutt"

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
