"""
Correlation plotter prints sample points in a 2D plane, to allow a visual detection of
concentrated clusters. Internally uses the pyplot scatter module. Useful e.g. for time to
error-rate ratio. Skill to error rate ratio, etc.
Author: Maximilian Schiedermeier
"""
import matplotlib.pyplot as plt

from restify_mining.scatter_plotters.correlation import Correlation
from restify_mining.scatter_plotters.dimension import Dimension
from restify_mining.scatter_plotters.group_samples import GroupSamples


def plot_correlation_with_auto_dimensions(correlation: Correlation, file_name_marker: str) -> None:
    """
    Reduces version of subsequent method. Uses the correlation size itself to retrieve required
    plot space.
    :param correlation: as the correlation data to visualize.
    :param file_name_marker: as string to use for persisted plot on disk.
    """
    plot_correlation(correlation, file_name_marker, correlation.dimension)


def plot_correlation(correlation: Correlation, file_name_marker: str, dimension: Dimension) -> None:
    """
    Meta plotter method to just print my data with labels, but without any contrived parameters
    that nobody actually every needs.

    :param correlation: as the correlation data to visualize.
    :param file_name_marker: as string to use for persisted plot on disk.
    :param dimension: as the space to use for both axes.
    """

    # Prepare subplots (needed for labeling, see: https: // stackoverflow.com/a/14434334 )
    label_overlay = plt.subplots()[1]

    # Set axis dimensions (add a little buffer)
    plt.axis([0, dimension.y_size * 1.05, 0, dimension.x_size * 1.05])

    # Add the axis labels
    plt.xlabel(correlation.y_axis_label)
    plt.ylabel(correlation.x_axis_label)

    red_bundle: GroupSamples = correlation.red_bundle
    plt.scatter(red_bundle.y_axis_values, red_bundle.x_axis_values, color=red_bundle.group_tint)
    for i, red_label in enumerate(correlation.red_labels):
        label_overlay.annotate(red_label,
                               (red_bundle.y_axis_values[i], red_bundle.x_axis_values[i]))

    green_bundle: GroupSamples = correlation.green_bundle
    plt.scatter(green_bundle.y_axis_values, green_bundle.x_axis_values,
                color=green_bundle.group_tint)
    for i, green_label in enumerate(correlation.green_labels):
        label_overlay.annotate(green_label,
                               (green_bundle.y_axis_values[i], green_bundle.x_axis_values[i]))

    blue_bundle: GroupSamples = correlation.blue_bundle
    plt.scatter(blue_bundle.y_axis_values, blue_bundle.x_axis_values, color=blue_bundle.group_tint)
    for i, blue_label in enumerate(correlation.blue_labels):
        label_overlay.annotate(blue_label,
                               (blue_bundle.y_axis_values[i], blue_bundle.x_axis_values[i]))

    yellow_bundle: GroupSamples = correlation.yellow_bundle
    plt.scatter(yellow_bundle.y_axis_values, yellow_bundle.x_axis_values,
                color=yellow_bundle.group_tint)
    for i, yellow_label in enumerate(correlation.yellow_labels):
        label_overlay.annotate(yellow_label,
                               (yellow_bundle.y_axis_values[i], yellow_bundle.x_axis_values[i]))

    plt.tight_layout
    plt.savefig("generated-plots/" + file_name_marker + correlation.filename, dpi=300)
    plt.show()
