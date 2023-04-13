"""
Helper module to turn test success rates per group into radar plots. Based on an online tutorial:
https://tinyurl.com/2s4dnnek
Author: Maximilian Schiedermeier
"""
import matplotlib.pyplot as plt
import numpy as np

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.markers import unit_tests_markers
from restify_mining.unit_test_miners.abstract_miner import AbstractTestMiner


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
        plt.thetagrids(np.degrees(label_loc), labels=categories)
        plt.legend()
        plt.show()

    def radar_plot(self, miner: AbstractTestMiner,
                   app: str, participants: list[AssessedParticipant]) -> None:
        """
        Produces a radar plot for the four control group average test results
        :param miner: as the miner to extract group average scores per
        test
        :param app: as the application to analyze ("bs"/"xox")
        :param participants: as the full population to represent in radar
        :return: None
        """

        # reject if input app is not valid. Set test labels according to provided scope
        if app == "bs":
            test_markers: list[str] = unit_tests_markers.bs_unit_tests
        elif app == "xox":
            test_markers: list[str] = unit_tests_markers.xox_unit_tests
        else:
            raise Exception("Provided app for radar plot is not valid: " + app)
        # duplicate last test marker and place at front, so the labels form closed circuit on
        # radar circle.
        test_markers = [*test_markers, test_markers[0]]

        # Next we get the average tests score per control group and test
        # For every group ("circle" to appear in the radar plot), we want an extra list.
        group_average_test_results: list[list[float]] = miner.mine(participants)
        red_average_samples: list[float] = group_average_test_results[0]
        green_average_samples: list[float] = group_average_test_results[1]
        blue_average_samples: list[float] = group_average_test_results[2]
        yellow_average_samples: list[float] = group_average_test_results[3]

        # Next we do the same duplication trick with the sample points as with the labels
        # duplicate last element ant place in front) to ensure closed circuits.
        red_average_samples = [*red_average_samples, red_average_samples[0]]
        green_average_samples = [*green_average_samples, green_average_samples[0]]
        blue_average_samples = [*blue_average_samples, blue_average_samples[0]]
        yellow_average_samples = [*yellow_average_samples, yellow_average_samples[0]]

        # Finally actually construct the radar plot
        # Configure the plot to have as many sectors as there are test cases for the app:
        label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(test_markers))

        # Set plot to a radar (polar coordinate plot and feed the sample points)
        plt.figure(figsize=(8, 8))
        plt.subplot(polar=True)
        plt.plot(label_loc, red_average_samples, label='Red', color="red")
        plt.plot(label_loc, green_average_samples, label='Green', color="green")
        plt.plot(label_loc, blue_average_samples, label='Blue', color="blue")
        plt.plot(label_loc, yellow_average_samples, label='Yellow', color="yellow")

        plt.title('Xox Average Test Scores per Group', size=20, y=1.05)
        plt.thetagrids(np.degrees(label_loc), labels=test_markers)
        plt.legend()
        plt.savefig("generated-plots/" + "06-" + app + "-all-tests-radar.png")
        plt.show()
