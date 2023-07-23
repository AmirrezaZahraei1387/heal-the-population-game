"""here we implemented the main and important part of the
game that will do all the backend calculations.
here we first will generate the virus to make a sick
we give it back."""
import dataman
import polys_ever


data = dataman.DataM()


class GameM:

    def __init__(self):
        try:
            data = dataman.DataM()
        except Exception:
            raise
