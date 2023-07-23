"""here we implemented the main and important part of the
game that will do all the backend calculations.
here we first will generate the virus to make a sick
we give it back."""
import dataman
import errors


class GameM:

    def __init__(self):

        self.data = dataman.DataM()
        self.allPoly = []

        for creature in self.data.availableCreatures:
            self.allPoly.append(self.data.getPolyObj(creature))





