"""
This module consumes the "stageonefailcause.csv" file and visualizes its content as a pie chart.
"""

import matplotlib.pyplot as plt
import numpy as np

from csv_tools.file_load_utils import load_stage_one_error_occurrences


def cell_14() -> None:
    """
    Jupyter cell 14. See markdown description.
    :return: None
    """

    # load fail cause stage 1 data from csv
    error_frequencies: dict[str, int] = load_stage_one_error_occurrences()

    # create shares, i.e. count occurrences of entries.
    pie_data: np.array = np.array(list(error_frequencies.values()))
    pie_labels = error_frequencies.keys()

    # actually plot the thing

    plt.pie(pie_data, labels=pie_labels)
    plt.show()

