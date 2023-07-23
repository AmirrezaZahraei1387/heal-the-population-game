"""here we implemented the main and important part of the
game that will do all the backend calculations.
here we first will generate the virus to make a sick
we give it back."""
import dataman
import errors


class GameM:

    def __init__(self):
        try:
            self.data = dataman.DataM()
        except Exception:
            raise errors.CanNotOpenDataError("can not open data")


    def openPoly(self, creatureName):
        """opening the poly.txt read it and give the
        object of it back"""








