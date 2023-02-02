"""
Correlation plotter prints sample points in a 2D plane, to allow a visual detection of
concentrated clusters. Internally uses the pyplot scatter module. Useful e.g. for time to
error-rate ratio. Skill to error rate ratio, etc.
"""
import matplotlib.pyplot as plt

from restify_mining.plotters.correlation import Correlation

def plot_correlation(correlation: Correlation) -> None:
    """Meta plotter method to just print my data with labels, but without any contrived parameters
    that nobody actually every needs.
    """

    # Compute plot axis dimensions including a buffer margin.
    x_max_with_buffer: float = correlation.x_axis_max * 1.05
    y_max_with_buffer: float = correlation.y_axis_max * 1.05
    plt.axis([0, x_max_with_buffer, 0, y_max_with_buffer])

    # Add the axis labels
    plt.xlabel(correlation.x_axis_label)
    plt.ylabel(correlation.y_axis_label)

    # For all groups in the bundle, add the sample points in the correct colour
    plt.scatter(correlation.red_bundle.x_axis_values, correlation.red_bundle.y_axis_values)
    plt.scatter(correlation.green_bundle.x_axis_values, correlation.green_bundle.y_axis_values)
    plt.scatter(correlation.blue_bundle.x_axis_values, correlation.blue_bundle.y_axis_values)
    plt.scatter(correlation.yellow_bundle.x_axis_values, correlation.yellow_bundle.y_axis_values)
    plt.show()
