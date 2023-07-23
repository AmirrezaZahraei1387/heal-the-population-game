"""this is the file that will make a way for saving the polynomials and
doing arithmetic with them.
the degree of them should be specified by the programmer."""


def otherParaCheck(method):
    """this is a decorator created to check the other parameter in the
    additions or subtractions of the following class"""
    def newMethod(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("can not add type ",
                            type(other), " to type ", self.__class__)

        newMethod.__doc__ = method.__doc__  # putting the method doc to the newMethod, so it won't be lost

        return method(self, other)
    return newMethod


class Poly:

    defaultUsedVar: str = 'x'
    degree: int
    values: list    # the values contain the coeff of different variables
    # for example:
    # the variable x**0 has coeff in index 0
    # the variable x**1 has coeff in index 1
    # the variable x**2 has coeff in index 2
    # ...

    def __init__(self, degree, values_poly):

        if degree != len(values_poly) - 1:  # meaning that number of numbers provided does not match the degree number
            raise ValueError("the degree with value ", degree,
                             " does not match the number of provided values ",
                             values_poly)

        self.degree = degree
        self.values = values_poly

    def minDegV(self, other):

        if self.degree > other.degree:
            return other
        return self

    def maxDegV(self, other):

        if self.degree < other.degree:
            return other
        return self

    def sub(self, other):

        newValue = []
        maxDegree = self.maxDegV(other).degree

        for index in range(0, maxDegree + 1):
            try:
                newValue.append(self.values[index] - other.values[index])
            except IndexError:
                if maxDegree == self.degree:
                    newValue.append(self.values[index])
                else:
                    newValue.append(other.values[index])

        return newValue

    def add(self, other):

        newValue = []

        minValue = self.minDegV(other)
        maxValue = self.maxDegV(other)
        # here the sequence in not matter as it is addition
        for index in range(0, minValue.degree + 1):
            newValue.append(minValue.values[index] + maxValue.values[index])

        for index in range(minValue.degree+1, maxValue.degree + 1):
            newValue.append(maxValue.values[index])

        return newValue

    @otherParaCheck
    def __add__(self, other):

        additionResult = self.add(other)
        newPoly = self.__class__(degree=len(additionResult)-1, values_poly=additionResult)
        return newPoly

    @otherParaCheck
    def __sub__(self, other):
        subtractionResult = self.sub(other)
        newPoly = self.__class__(degree=len(subtractionResult)-1, values_poly=subtractionResult)
        return newPoly

    def __str__(self):
        """it will print the poly.txt.txt.txt.txt using the powers
        of a variable"""

        counter = -1
        polyStr = ""

        for coeff in self.values:
            counter += 1
            polyStr += str(coeff)+self.defaultUsedVar+"**"+str(counter)+'+'

        return polyStr











