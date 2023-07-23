"""here we implemented the main and important part of the
game that will do all the backend calculations.
here we first will generate the virus to make a sick
we give it back."""
import dataman
import errors
import random

class GameM:

    sickNumber: int

    def __init__(self):

        self.data = dataman.DataM()
        self.allPoly = []

        for creature in self.data.availableCreatures:
            self.allPoly.append(self.data.getPolyObj(creature))

    def gameSetUp(self, sickNumber):
        """sickNumber is the number of sicks for the game"""
        self.sickNumber = sickNumber

    def generateVirus(self):
        pass






