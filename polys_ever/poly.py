"""this is the file that will make a way for saving the polynomials and
doing arithmetic with them.
the degree of them should be specified by the programmer."""



class Poly:

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




