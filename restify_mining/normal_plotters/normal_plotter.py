"""
Helper module to conveniently print normal distributed data (gaussian bell shape thingy like).
Author: Maximilian Schiedermeier
"""
import math

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def plot_normal(samples: list[float], colour: str, x_label: str, y_label: str,
                filename: str) -> None:
    """
    Plots the normal distribution curves, based on provided data samples.
    Note: provided data should be tested for approximately normal distributed first, e.g. using
    shapiro-wilk test.
    :param samples: as sample points used for computation of mean and deviation.
    :param colour: as string describing colour of curve
    :param x_label: as text to show on horizontal axis
    :param y_label: as text to show on vertical axis
    :param filename: as filename to use for persistence (without file extension)
    :return: None
    """
    # Set figure dimensions
    plt.rcParams["figure.figsize"] = (14, 4)

    # Compute stdev and mean based on provided samples
    mean: float = sum(samples) / len(samples)
    stddev: float = np.std(samples)

    # actually plot the gaussian distributions
    sigma: float = math.sqrt(stddev)
    distribution = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
    plt.plot(distribution, stats.norm.pdf(distribution, mean, sigma), colour)

    # Add axis labels
    plt.xlabel(x_label)  # e.g. Skill Score
    plt.ylabel(y_label)  # e.g. Probability Density

    # Store on disk
    plt.savefig("generated-plots/" + filename + ".png")
    plt.show()

