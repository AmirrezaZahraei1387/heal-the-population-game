"""this is the code file that is created for managing the
data and configurations of the game."""

import json
import pathlib
import os
import poly as polys_ever


CONFIG_JSON_PATH = str(pathlib.Path("data/config.json").absolute())
MAIN_DIR_PATH = str(pathlib.Path("data/main").absolute())


class DataM:

    def __init__(self):
        with open(file=CONFIG_JSON_PATH, mode='r', encoding="utf-8") as conf:
            config = json.load(conf)
        conf.close()

        self.__degree = config["degree"]

        self.__maxVirusDegree = config["virus"]["maxVirusDegree"]
        self.__minVirusDegree = config["virus"]["minVirusDegree"]

        self.__maxVirusRange = config["virus"]["maxRange"]
        self.__minVirusRange = config["virus"]["minRange"]

        self.__maxSickNumber = config["sickNumber"]["maxSickNumber"]
        self.__minSickNumber = config["sickNumber"]["minSickNumber"]

        self.__availableCreatures = os.listdir(MAIN_DIR_PATH)

        self.__imageFormat = config["imageFormat"]

        self.__polyName = config["polyName"]

    # make these variables read only
    @property
    def degree(self):
        return self.__degree

    @property
    def maxVirusDegree(self):
        return self.__maxVirusDegree

    @property
    def minVirusDegree(self):
        return self.__minVirusDegree

    @property
    def availableCreatures(self):
        return self.__availableCreatures

    @property
    def imageFormat(self):
        return self.__imageFormat

    @property
    def polyName(self):
        return self.__polyName

    @property
    def maxSickNumber(self):
        return self.__maxSickNumber

    @property
    def minSickNumber(self):
        return self.__minSickNumber

    @property
    def maxVirusRange(self):
        return self.__maxVirusRange

    @property
    def minVirusRange(self):
        return self.__minVirusRange

    def getImagePath(self, creatureName):

        path = pathlib.Path(MAIN_DIR_PATH+'/'+creatureName+'/'
                            +creatureName+'.'+self.imageFormat).absolute()
        return path

    def getPolyPath(self, creatureName):

        path = pathlib.Path(MAIN_DIR_PATH+'/'+creatureName+'/'
                            + self.polyName).absolute()
        return path

    def getPolyObj(self, creatureName):
        """it will read the all the data of the file poly.txt,
        and will return the object of it back"""
        path = self.getPolyPath(creatureName)

        data = open(file=path, mode='r', encoding="utf-8")

        lines = data.readlines()
        length = len(lines)
        for index in range(0, len(lines)):
            lines[index] = int(lines[index])

        data.close()

        return polys_ever.Poly(length - 1, lines)

    def saveData(self):

        data = {
            "degree": self.degree,
            "imageFormat": self.imageFormat,
            "polyName": self.polyName,

            "virus": {
                "maxVirusDegree": self.maxVirusDegree,
                "minVirusDegree": self.minVirusDegree,
                "maxRange": self.maxVirusRange,
                "minRange": self.minVirusRange
            },
            "sickNumber": {
                "maxSickNumber": self.maxSickNumber,
                "minSickNumber": self.minSickNumber
            }
            }
        with open(file=CONFIG_JSON_PATH, mode='w', encoding="utf-8") as conf:
            json.dump(data, conf, indent=3)
        conf.close()













