"""this is the code file that is created for managing the
data and configurations of the game."""

import json
import os
import pathlib


CONFIG_JSON_PATH = "config.json"
MAIN_DIR_PATH = "main"


class DataM:

    def __init__(self):
        with open(file=CONFIG_JSON_PATH, mode='r', encoding="utf-8") as conf:
            config = json.load(conf)
        conf.close()

        self.__degree = config["degree"]
        self.__maxVirusDegree = config["virus"]["maxVirusDegree"]
        self.__minVirusDegree = config["virus"]["minVirusDegree"]
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

    def getImagePath(self, creatureName):

        path = pathlib.Path(MAIN_DIR_PATH+'/'+creatureName+'/'
                            +creatureName+'.'+self.imageFormat).absolute()
        return path

    def getPolyPath(self, creatureName):

        path = pathlib.Path(MAIN_DIR_PATH+'/'+creatureName+'/'
                            + self.polyName).absolute()
        return path

    def saveData(self):

        data = {
            "degree": self.degree,
            "imageFormat": self.imageFormat,
            "polyName": self.polyName,

            "virus": {
                "maxVirusDegree": self.maxVirusDegree,
                "minVirusDegree": self.minVirusDegree
            }
            }
        with open(file=CONFIG_JSON_PATH, mode='w', encoding="utf-8") as conf:
            json.dump(data, conf, indent=3)
        conf.close()













