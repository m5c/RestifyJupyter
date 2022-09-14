"""
2D plotter module that creates visualizations of test success rates for population / population
subsets and for one or two selected applications.
Inspired by: https://stackoverflow.com/a/7230921
"""

import matplotlib as mpl
from matplotlib import pyplot
import numpy as np

from restify_mining import participant_filter_tools
from restify_mining.assessed_participant import AssessedParticipant
from restify_mining.markers import unit_tests_markers


def plot_random(assessed_population: list[AssessedParticipant]):
    # Extract covered control groups
    control_groups: list[str] = participant_filter_tools.extract_group_names(assessed_population)
    print(control_groups)

    # Create 2D array, consisting of all participants (already ordered by control group) and test
    # results for all individual unit tests (both apps, sequential. First all BookStore unit
    # tests, then all Xox unit tests.
    grid_values: list[list[float]]
    unit_tests_markers.all_unit_tests()
    # for assessed_participant in assessed_population:
    #
    #     # Inner loop, iterate over all test cases (bookstore + xox)
    #     plot_values.append(assessed_participant.all_test_values)

    # make values from -5 to 5, for this example
    zvals: list[list[float]] = np.random.rand(100, 100) * 10 - 5

    # make a color map of fixed colors
    cmap = mpl.colors.ListedColormap(['blue', 'black', 'red'])
    bounds = [-6, -2, 2, 6]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    # tell imshow about color map so that only set colors are used
    img = pyplot.imshow(zvals, interpolation='nearest',
                        cmap=cmap, norm=norm)

    # make a color bar
    pyplot.colorbar(img, cmap=cmap,
                    norm=norm, boundaries=bounds, ticks=[-5, 0, 5])

    pyplot.show()
