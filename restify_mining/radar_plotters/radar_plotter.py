import matplotlib.pyplot as plt
import numpy as np

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.unit_test_miners.abstract_miner import AbstractMiner


class RadarPlotter:
    """
    This class provides convenient access to radar plots.
    Its internals are based on the snippets provided in this blog:
    https://towardsdatascience.com/how-to-make-stunning-radar-charts-with-python-implemented-in
    -matplotlib-and-plotly-91e21801d8ca
    """

    def plot_sample(self) -> None:
        """
        Produces a sample plot
        :return: None
        """
        categories = ['Food Quality', 'Food Variety', 'Service Quality', 'Ambiance',
                      'Affordability']
        categories = [*categories, categories[0]]

        restaurant_1 = [4, 4, 5, 4, 3]
        restaurant_2 = [5, 5, 4, 5, 2]
        restaurant_3 = [3, 4, 5, 3, 5]
        restaurant_1 = [*restaurant_1, restaurant_1[0]]
        restaurant_2 = [*restaurant_2, restaurant_2[0]]
        restaurant_3 = [*restaurant_3, restaurant_3[0]]

        label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))

        plt.figure(figsize=(8, 8))
        plt.subplot(polar=True)
        plt.plot(label_loc, restaurant_1, label='Restaurant 1')
        plt.plot(label_loc, restaurant_2, label='Restaurant 2')
        plt.plot(label_loc, restaurant_3, label='Restaurant 3')
        plt.title('Restaurant comparison', size=20, y=1.05)
        lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
        plt.legend()
        plt.show()

    def radar_plot(self, miner: AbstractMiner,
                   participants: list[AssessedParticipant]) -> None:
        """
        Produces a radar plot for the four control group average test results.
        :param miner: as the miner to extract group average scores per
        test.
        :param participants: as the full population to represent in radar.
        :return: None
        """
        # TODO: Get the actual test labels.
        categories = ['Food Quality', 'Food Variety', 'Service Quality', 'Ambiance',
                      'Affordability']
        categories = [*categories, categories[0]]

        # TODO: get the actual test results
        # Something like:
        group_average_test_results: list[list[float]] = miner.mine(participants)
        restaurant_1 = [4, 4, 5, 4, 3]
        restaurant_2 = [5, 5, 4, 5, 2]
        restaurant_3 = [3, 4, 5, 3, 5]
        # This seems to duplicate the last entry and place it at front of list. (Needed to make the contour lines have a matching start and endpoint.
        restaurant_1 = [*restaurant_1, restaurant_1[0]]
        restaurant_2 = [*restaurant_2, restaurant_2[0]]
        restaurant_3 = [*restaurant_3, restaurant_3[0]]

        label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))

        plt.figure(figsize=(8, 8))
        plt.subplot(polar=True)
        plt.plot(label_loc, restaurant_1, label='Restaurant 1')
        plt.plot(label_loc, restaurant_2, label='Restaurant 2')
        plt.plot(label_loc, restaurant_3, label='Restaurant 3')
        plt.title('Restaurant comparison', size=20, y=1.05)
        lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
        plt.legend()
        plt.show()
