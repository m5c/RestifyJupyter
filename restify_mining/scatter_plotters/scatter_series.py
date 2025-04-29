"""
Defines a series of scatter plots, based on fixed axis extractors and a given series of
strings that act as extractor parameters and define the sequence of generated plots. All plots
use a common dimensions.
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.correlation import Correlation
from restify_mining.scatter_plotters.correlation_plotter import plot_correlation
from restify_mining.scatter_plotters.dimension import Dimension
from restify_mining.scatter_plotters.extractors.label_maker import LabelMaker


class ScatterSeries:
    """
    Defines a series of scatter plots, based on fixed axis extractors and a given series of
    strings that act as extractor parameters and define the sequence of generated plots. All plots
    use a common dimensions.
    """

    # pylint: disable=too-many-arguments

    def __init__(self, x_extractor_type: type, y_extractor_type: type, label_maker: LabelMaker,
                 outliers: bool, prefix: str) -> 'ScatterSeries':
        """
        Constructor, defines the characteristics to apply for the full series.
        @param: x_extractor as variable to apply for x-axis.
        @param: y_extractor as observation to print on y-value.
        """
        self.__y_extractor_type: type = x_extractor_type
        self.__x_extractor_type: type = y_extractor_type
        self.__prefix: str = prefix
        self.__label_maker: LabelMaker = label_maker
        self.__outliers: bool = outliers

    def plot_uncoupled_series(self, series_extractor_1: list[str],
                              series_extractor_2: list[str]) -> None:
        """
        Call to actually produce the series of plots and persist them on disk.
        The first argument is the list of parameters to alter for the first extractor. The second
        list provides the series values for the second iterator. Those series are uncoupled,
        that is to say all combinations must be considered.
        The amount of produced plots equals the product of both list sizes.
        :param: series_extractor_1 as the series parameter to apply for first extractor.
        :param: series_extractor_2 as the series parameter to apply for second extractor.
        :return: None
        """
        # Create actual cross product of both received lists
        # create symmetric pairs for each entry in input list
        tuples: list[(int, int)] = []
        for parameter_1 in series_extractor_1:
            for parameter_2 in series_extractor_2:
                tuples.append((parameter_1, parameter_2))

        # then call the actual plotter, using the resulting tuple list (same values used for both
        # extractors)
        self.__plot_tuple_series(tuples)

    def plot_coupled_series(self, series: list[str]) -> None:
        """
        Call to actually produce the series of plots and persist them on disk.
        This variant is an overloaded version of the previous, it couples the provided values (
        single list) for both extractors.
        :param: series as the series of plots to apply, e.g. different methodologies / applications.
        :return: None
        """
        # create symmetric pairs for each entry in input list
        tuples: list[(int, int)] = []
        for parameter in series:
            tuples.append((parameter, parameter))

        # then call the actual plotter, using the resulting tuple list (same values used for both
        # extractors)
        self.__plot_tuple_series(tuples)


    def __plot_tuple_series(self, tuples: list[(str, str)]) -> None:
        """
        This method plots the actual tuple series where each tuple in lsit results from a
        combination
        of extractors.
        This method should not be called directly. If you want to produce series, use one of the two
        previous methods.
        """

        # Load all participant objects (specifies skills, codename, control-group) from csv file
        # This scatter shows individual participant data, so we include outliers, but mark them.
        assessed_population: list[
            AssessedParticipant] = file_load_utils.load_all_assessed_participants(False)

        # Create several correlation bundles for desired metrics and plot them.
        dimension: Dimension = Dimension(0, 0)
        correlation_series: list[Correlation] = []
        for series_tuple in tuples:
            item_correlation: Correlation = Correlation(assessed_population,
                                                        self.__x_extractor_type(series_tuple[0]),
                                                        self.__y_extractor_type(series_tuple[1]),
                                                        self.__label_maker,
                                                        self.__outliers)
            dimension.fuse(item_correlation.dimension)
            correlation_series.append(item_correlation)


        # Plot all items, using the resulting optimal dimension
        for correlation in correlation_series:
            plot_correlation(correlation, self.__prefix, dimension)

