"""
Helper module that combines two provided extractors and applies them on a given population. 
Produces all parameters needed for printing by correlation plotter.
Author Maximilian Schiedermeier
"""

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.plotters.extractors.extractor import Extractor
from restify_mining.plotters.group_sample_points import GroupSamples


class Correlation:
    """Helper class for convenient extraction of data for colourized plots."""

    def __init__(self, full_population: list[AssessedParticipant], x_extractor: Extractor,
                 y_extractor: Extractor, indicate_groups: bool):
        # Store axis labels
        self.__x_axis_label: str = x_extractor.axis_label()
        self.__y_axis_label: str = y_extractor.axis_label()

        # Extract sub-populations (groups)
        red_assessed_popultation: list[AssessedParticipant] = filter_population_by_group(
            full_population, "red")
        green_assessed_popultation: list[AssessedParticipant] = filter_population_by_group(
            full_population, "green")
        blue_assessed_popultation: list[AssessedParticipant] = filter_population_by_group(
            full_population, "blue")
        yellow_assessed_popultation: list[AssessedParticipant] = filter_population_by_group(
            full_population, "yellow")

        # Generate x-sample points for all participants, using x_extractor
        red_samples_x: list[float] = x_extractor.extract(red_assessed_popultation);
        green_samples_x: list[float] = x_extractor.extract(green_assessed_popultation);
        blue_samples_x: list[float] = x_extractor.extract(blue_assessed_popultation);
        yellow_samples_x: list[float] = x_extractor.extract(yellow_assessed_popultation);

        # Generate y-sample points for all participants, using y_extractor
        red_samples_y: list[float] = y_extractor.extract(red_assessed_popultation);
        green_samples_y: list[float] = y_extractor.extract(green_assessed_popultation);
        blue_samples_y: list[float] = y_extractor.extract(blue_assessed_popultation);
        yellow_samples_y: list[float] = y_extractor.extract(yellow_assessed_popultation);

        # Store extracted x / y sample points in printable bundles.
        self.__red_bundle: GroupSamples = GroupSamples("red", red_samples_x, red_samples_y,
                                                       indicate_groups)
        self.__green_bundle: GroupSamples = GroupSamples("green", green_samples_x, green_samples_y,
                                                         indicate_groups)
        self.__blue_bundle: GroupSamples = GroupSamples("blue", blue_samples_x, blue_samples_y,
                                                        indicate_groups)
        self.__yellow_bundle: GroupSamples = GroupSamples("yellow", yellow_samples_x,
                                                          yellow_samples_y, indicate_groups)

        # Figure out the maximum values in sample points
        self.__x_axis_max: float = max(max(red_samples_x), max(green_samples_x),
                                       max(blue_samples_x), max(yellow_samples_x))
        self.__y_axis_max: float = max(max(red_samples_y), max(green_samples_y),
                                       max(blue_samples_y), max(yellow_samples_y))

    @property
    def x_axis_label(self) -> str:
        """
        Getter for private x-axis label field
        :return: string to be used by plotter for x-axis.
        """
        return self.__x_axis_label

    @property
    def y_axis_label(self) -> str:
        """
        Getter for private y-axis label field
        :return: string to be used by plotter for y-axis.
        """
        return self.__y_axis_label

    @property
    def x_axis_max(self) -> float:
        """
        Getter for private x-axis max field
        :return: maximum float value in all x ordinates of sample points.
        """
        return self.__x_axis_max

    @property
    def y_axis_max(self) -> float:
        """
        Getter for private y-axis max field
        :return: maximum float value in all y ordinates of sample points.
        """
        return self.__y_axis_max

    @property
    def red_bundle(self) -> GroupSamples:
        """
        Getter for the bundle of red sample points.
        :return: group sample points of red control group for applied extractor.
        """
        return self.__red_bundle

    @property
    def green_bundle(self) -> GroupSamples:
        """
        Getter for the bundle of red sample points.
        :return: group sample points of green control group for applied extractor.
        """
        return self.__green_bundle

    @property
    def blue_bundle(self) -> GroupSamples:
        """
        Getter for the bundle of red sample points.
        :return: group sample points of blue control group for applied extractor.
        """
        return self.__blue_bundle

    @property
    def yellow_bundle(self) -> GroupSamples:
        """
        Getter for the bundle of red sample points.
        :return: group sample points of yellow control group for applied extractor.
        """
        return self.__yellow_bundle
