"""
Helper module to bundle x/y sample points for a specific group. Does not store the colour to use
for plotting, the group name is sufficient in combination with the group_tint_makers module.
Author: Maximilian Schiedermeier
"""
from restify_mining.markers.group_tint_markers import group_to_tint


class GroupSamples:
    """Bundle class to group sample points and group name."""

    def __init__(self, group_name: str, x_axis_values: list[float], y_axis_values: list[float], with_tint: bool):
        self.__group_name: str = group_name
        self.__group_tint: str = group_to_tint(group_name) if with_tint else "#000000"
        self.__x_axis_values: list[float] = x_axis_values
        self.__y_axis_values: list[float] = y_axis_values

    @property
    def group_name(self) -> str:
        """Getter to look up group name associated to this sample point bundle."""
        return self.__group_name

    @property
    def group_tint(self) -> str:
        """"Getter to look up group tint associated to this sample point bundle."""
        return self.__group_tint

    @property
    def x_axis_values(self) -> list[float]:
        """Getter for all x_axis values of all sample points."""
        return self.__x_axis_values

    @property
    def y_axis_values(self) -> list[float]:
        """Getter for all y_axis values of all sample points."""
        return self.__y_axis_values
