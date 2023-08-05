"""
Helper module that combines two provided extractors and applies them on a given population.
Produces all parameters needed for printing by correlation scatter plotter.
Author Maximilian Schiedermeier
"""

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.scatter_plotters.dimension import Dimension
from restify_mining.scatter_plotters.extractors.extractor import Extractor
from restify_mining.scatter_plotters.extractors.label_maker import LabelMaker
from restify_mining.scatter_plotters.group_samples import GroupSamples


class Correlation:
    """Helper class for convenient extraction of data for colourized plots."""

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-locals

    def __init__(self, full_population: list[AssessedParticipant], x_extractor: Extractor,
                 y_extractor: Extractor, label_maker: LabelMaker, filter_outliers: bool):
        """
        Constructor for a plotable correlation.
        :param full_population: as the population to analyze (should be full, assessed population).
        :param x_extractor: as the extractor to apply for x-ordinate of samples
        :param y_extractor: as the extractor to apply for y-ordinate of samples
        :param label_maker: as the labeling strategy to apply.
        :param filter_outliers: boolean flag to indicate if only outliers should be labeled.
        """
        # Store axis labels and Scatter dot label maker
        self.__x_axis_label: str = x_extractor.axis_label()
        self.__y_axis_label: str = y_extractor.axis_label()

        # Extract sub-populations (groups)
        red_assessed_population: list[AssessedParticipant] = filter_population_by_group(
            full_population, "red")
        green_assessed_population: list[AssessedParticipant] = filter_population_by_group(
            full_population, "green")
        blue_assessed_population: list[AssessedParticipant] = filter_population_by_group(
            full_population, "blue")
        yellow_assessed_population: list[AssessedParticipant] = filter_population_by_group(
            full_population, "yellow")

        # Generate x-sample points for all participants, using x_extractor
        red_samples_x: list[float] = x_extractor.extract(red_assessed_population)
        green_samples_x: list[float] = x_extractor.extract(green_assessed_population)
        blue_samples_x: list[float] = x_extractor.extract(blue_assessed_population)
        yellow_samples_x: list[float] = x_extractor.extract(yellow_assessed_population)

        # Generate y-sample points for all participants, using y_extractor
        red_samples_y: list[float] = y_extractor.extract(red_assessed_population)
        green_samples_y: list[float] = y_extractor.extract(green_assessed_population)
        blue_samples_y: list[float] = y_extractor.extract(blue_assessed_population)
        yellow_samples_y: list[float] = y_extractor.extract(yellow_assessed_population)

        # Generate sample point labels for all participants
        self.__red_labels: list[str] = label_maker.make_labels(red_assessed_population,
                                                               filter_outliers)
        self.__green_labels: list[str] = label_maker.make_labels(green_assessed_population,
                                                                 filter_outliers)
        self.__blue_labels: list[str] = label_maker.make_labels(blue_assessed_population,
                                                                filter_outliers)
        self.__yellow_labels: list[str] = label_maker.make_labels(yellow_assessed_population,
                                                                  filter_outliers)

        # Store extracted x / y sample points in printable bundles.
        self.__red_bundle: GroupSamples = GroupSamples("red", red_samples_x, red_samples_y,
                                                       True)
        self.__green_bundle: GroupSamples = GroupSamples("green", green_samples_x, green_samples_y,
                                                         True)
        self.__blue_bundle: GroupSamples = GroupSamples("blue", blue_samples_x, blue_samples_y,
                                                        True)
        self.__yellow_bundle: GroupSamples = GroupSamples("yellow", yellow_samples_x,
                                                          yellow_samples_y, True)

        # Figure out the maximum values in sample points
        self.__x_axis_max: float = max(red_samples_x + green_samples_x +
                                       blue_samples_x + yellow_samples_x)
        self.__y_axis_max: float = max(red_samples_y + green_samples_y +
                                       blue_samples_y + yellow_samples_y)

        self.__filename: str = "x" + x_extractor.filename_segment() + "-y" + \
                               y_extractor.filename_segment()

    @property
    def dimension(self) -> Dimension:
        """
        Computes a dimension object that equivalents the size required for all sample points in
        the correlation object.
        :return: The required space as dimension object.
        """
        return Dimension(self.__x_axis_max, self.__y_axis_max)

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

    @property
    def red_labels(self) -> list[str]:
        """
        Getter for the labels of red sample points.
        :return: labels for all red sample points.
        """
        return self.__red_labels

    @property
    def green_labels(self) -> list[str]:
        """
        Getter for the labels of green sample points.
        :return: labels for all green sample points.
        """
        return self.__green_labels

    @property
    def blue_labels(self) -> list[str]:
        """
        Getter for the labels of blue sample points.
        :return: labels for all blue sample points.
        """
        return self.__blue_labels

    @property
    def yellow_labels(self) -> list[str]:
        """
        Getter for the labels of yellow sample points.
        :return: labels for all yellow sample points.
        """
        return self.__yellow_labels

    @property
    def filename(self) -> str:
        """
        Getter for the file name resulting of the applied extractors.
        :return: filename describing the applied extractors.
        """
        return self.__filename
