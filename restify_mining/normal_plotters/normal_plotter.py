"""
Helper module to conveniently print normal distributed data (gaussian bell shape thingy like).
Author: Maximilian Schiedermeier
"""
import math

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def plot_normal(samples: list[float], colour: str, x_label: str, y_label: str, app: str, dashed: bool) -> None:
    """
    Plots the normal distribution curves, based on provided data samples.
    Note: provided data should be tested for approximately normal distributed first, e.g. using
    shapiro-wilk test.
    :param samples: as sample points used for computation of mean and deviation.
    :param colour: as string describing colour of curve
    :param x_label: as text to show on horizontal axis
    :param y_label: as text to show on vertical axis
    :param app: as label for title to indicate the app the graph depicts.
    :return: None
    """
    # Set figure dimensions
    plt.rcParams["figure.figsize"] = (8, 3)

    # Compute stdev and mean based on provided samples
    mean: float = sum(samples) / len(samples)
    stddev: float = np.std(samples)

    # actually plot the gaussian distributions
    sigma: float = math.sqrt(stddev)
    distribution = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
    plt.xlim(0, 1)
    plt.title("Conversion Effectiveness Distributions, " + app.capitalize())
    if dashed:
        plt.plot(distribution, stats.norm.pdf(distribution, mean, sigma), colour, linestyle='dashed', linewidth='1')
    else:
        plt.plot(distribution, stats.norm.pdf(distribution, mean, sigma), colour)

    # Add axis labels
    plt.xlabel(x_label)  # e.g. Skill Score
    plt.ylabel(y_label)  # e.g. Probability Density


def show(filename: str) -> None:
    """
    Call to plotter to actually depict the overlay of all previous calls.
    :param filename: as the name of the graphics to store on disk
    :return: None
    """
    plt.tight_layout()
    plt.savefig("generated-plots/" + filename + ".png", dpi=300)
    plt.show()

def clear() -> None:
    plt.clf()
