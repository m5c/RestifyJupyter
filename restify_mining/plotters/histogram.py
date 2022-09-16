"""
Helper class for plotting histograms in 2D. This ons store cumulative (histogram) information. It
has hence only a notion for discrete int-like depths per cells.
You can add samples by providing the position. The histogram then stores the value. You can also
create histograms form provided discrete input arrays or boolean arrays.
"""


class Histogram:

    def __init__(self, x_range: int, y_range: int):
        __x_values: list[int] = []
        __y_values: list[int] = []
        __x_range: int = x_range
        __y_range: int = y_range

    @property
    def x_values(self):
        return self.__x_values

    @property
    def y_values(self):
        return self.__y_values

    @property
    def x_range(self):
        return self.x_range

    @property
    def y_range(self):
        return self.y_range
