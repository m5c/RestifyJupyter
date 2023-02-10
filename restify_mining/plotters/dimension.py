"""
Helper class to store space required by a plot in a single object. Can be combined with other
objects of same size to compute the effective space needed to store any of the plots. This is
computed by extracting the maximum value per axis, so e.g. for a plot of size [50, 100] and a
plot of size [120, 40], the result would be a dimension s of size [120, 100].
@Author Maximilian Schiedermeier.
"""


class Dimension:

    def __init__(self, x: int, y: int):
        """
        Constructor for a dimensions object. Consumes the size of plot and stores its values in a
        single object.
        :param x: as the x size of plot 1.
        :param y: as the y size of plot 1.
        """
        self.__x = x
        self.__y = y

    def fuse(self, other: 'Dimension') -> 'Dimension':
        """
        Combines the dimension object with a
        :param other: as a second dimension object to adapt to (takes max size required for both
        axes).
        :return: the resulting object (self).
        """
        self.__x = max(self.__x, other.x)
        self.__y = max(self.__y, other.y)
        return self

    @property
    def x(self) -> int:
        """
        Getter for the dimension's size in x.
        :return: stored dimension in x.
        """
        return self.__x

    @property
    def y(self) -> int:
        """
        Getter for the dimension's size in y.
        :return: stored dimension in y.
        """
        return self.__y
