"""
Correlation plotter prints sample points in a 2D plane, to allow a visual detection of
concentrated clusters. Internally uses the pyplot scatter module. Useful e.g. for time to
error-rate ratio. Skill to error rate ratio, etc.
"""
import matplotlib.pyplot as plt


def plot_correlation(x_values: list[int], y_values: list[int], x_label: str, y_label: str) -> None:
    """Meta plotter method to just print my data with labels, but without any contrived parameters
    that nobody actually every needs.
    """
    x_max = max(x_values) * 1.05
    y_max = max(y_values) * 1.05

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.axis([0, x_max, 0, y_max])
    plt.scatter(x_values, y_values)
    plt.show()

