"""here we implemented the main and important part of the
game that will do all the backend calculations.
here we first will generate the virus to make a sick
we give it back."""
import dataman
import random

import poly as polys_ever


class GameM:

    sickNumber: int = 0

    def __init__(self):

        self.data = dataman.DataM()
        self.allPoly = []

        for creature in self.data.availableCreatures:
            self.allPoly.append(self.data.getPolyObj(creature))

    def gameSetUp(self, sickNumber):
        """sickNumber is the number of sicks for the game"""
        if self.data.minSickNumber <= sickNumber <= self.data.maxSickNumber:
            self.sickNumber = sickNumber
        else:
            raise ValueError("the sickNumber is not in accepted range")

    def generateVirus(self):

        values = []

        degree = random.randint(self.data.minVirusDegree, self.data.maxVirusDegree)

        for i in range(degree+1):
            values.append(random.randint(self.data.minVirusRange, self.data.maxVirusRange))

        return polys_ever.Poly(degree, values)

    def generateQuestion(self):

        if self.sickNumber == 0:
            raise ValueError("the questions are finished")
        index = random.randint(0, len(self.data.availableCreatures))    # it is a random
        # index for choosing a creature for making a question for the game

        creaturePolyObj = self.allPoly[index]
        creatureName = self.data.availableCreatures[index]
        virus = self.generateVirus()

        sickCreature = creaturePolyObj + virus
        self.sickNumber -= 1
        return sickCreature, virus, creaturePolyObj, creatureName, self.data.getImagePath(creatureName)











