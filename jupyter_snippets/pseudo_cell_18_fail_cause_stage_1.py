"""
This module consumes the "stageonefailcause.csv" file and visualizes its content as a pie chart.
"""

import matplotlib.pyplot as plt
import numpy as np

from csv_tools.file_load_utils import load_stage_one_error_occurrences


def cell_18() -> None:
    """
    Jupyter cell 18. See markdown description.
    :return: None
    """

    # load fail cause stage 1 data from csv
    error_frequencies: dict[str, int] = load_stage_one_error_occurrences()

    # create shares, i.e. count occurrences of entries.
    pie_data: np.array = np.array(list(error_frequencies.values()))
    pie_labels = error_frequencies.keys()

    # Set some nice colours
    colours: list[str] = []
    for label in pie_labels:
        if label == "OK":
            colours.append("#82F282")
        elif label.startswith("repairable"):
            colours.append("#FCFC99")
        else:
            colours.append("#FB6962")

    # Remove label prefixes for better readability
    pie_labels: list[str] = [deprefix(label) for label in pie_labels]

    # actually plot the thing
    explode: list[float] = [0.015] * len(pie_labels)
    plt.pie(pie_data, autopct=absolute_value, labels=pie_labels, colors=colours, explode=explode)

    # plot an inner white circe to get nice donut
    # see: https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib
    # -935b7667d77f
    centre_circle = plt.Circle((0, 0), 0.75, fc='white')
    fig = plt.gcf()
    fig.set_size_inches(9, 5)
    fig.gca().add_artist(centre_circle)
    plt.savefig("generated-plots/18-fail-cause.png")
    plt.show()


def absolute_value(percentage):
    """
    helper funciton because python does not offer a built-in way to show actual numbers.
    :param percentage: as the auto compouted pie percentage
    :return:
    """
    return int(percentage/100*28)

def deprefix(label: str) -> None:
    """
    Helper function to remove error cause prefix if there is one.
    :return: Deprefixed error cause as string
    """
    if '_' in label:
        return label.split('_')[1]
    return label

