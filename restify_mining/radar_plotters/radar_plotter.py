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
from restify_mining.utils.group_to_methodology_and_order import group_app_to_methodology, \
    group_app_to_task_number


class RadarPlotter:
    """
    This class provides convenient access to radar plots.
    Its internals are based on the snippets provided in this blog:
    https://towardsdatascience.com/how-to-make-stunning-radar-charts-with-python-implemented-in
    -matplotlib-and-plotly-91e21801d8ca
    """

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
        app_title: str = ""
        if app == "bs":
            test_markers: list[str] = self.create_radar_test_label(app,
                len(unit_tests_markers.bs_unit_tests))
            app_title = "BookStore"
        elif app == "xox":
            test_markers: list[str] = self.create_radar_test_label(app,
                len(unit_tests_markers.xox_unit_tests))
            app_title = "Xox"
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

        # print the average samples and total per group pass rate:
        print("Radar numeric values for "+app+":")
        print("Red test average passrates: "+str(red_average_samples))
        print("Red overall average: "+str(sum(red_average_samples)/len(red_average_samples)))
        print("Green test average passrates: "+str(green_average_samples))
        print("Green overall average: "+str(sum(green_average_samples)/len(green_average_samples)))
        print("Blue test average passrates: "+str(blue_average_samples))
        print("Blue overall average: "+str(sum(blue_average_samples)/len(blue_average_samples)))
        print("Yellow test average passrates: "+str(yellow_average_samples))
        print("Yellow overall average: "+str(sum(yellow_average_samples)/len(yellow_average_samples)))




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
        red_label: str = group_app_to_methodology('red', app)+"/"+group_app_to_task_number('red', app)
        green_label: str = group_app_to_methodology('green', app)+"/"+group_app_to_task_number('green', app)
        blue_label: str = group_app_to_methodology('blue', app)+"/"+group_app_to_task_number('blue', app)
        yellow_label: str = group_app_to_methodology('yellow', app)+"/"+group_app_to_task_number('yellow', app)
        plt.plot(label_loc, red_average_samples, label=red_label, color="red")
        plt.plot(label_loc, green_average_samples, label=green_label, color="green")
        plt.plot(label_loc, blue_average_samples, label=blue_label, color="blue")
        plt.plot(label_loc, yellow_average_samples, label=yellow_label, color="yellow")

        plt.title(app_title + ' Average Test Scores per Group', size=20, y=1.05)
        plt.thetagrids(np.degrees(label_loc), labels=test_markers)
        plt.legend(loc='upper right')
        plt.savefig("generated-plots/" + "06-" + app + "-all-tests-radar.png", dpi=300)
        plt.show()

    @staticmethod
    def create_radar_test_label(app: str, amount: int) -> list[str]:
        """
        helper method to create opaque test labels that just enumerate instead of listing the actual
        endpoint names. Zero padded and indicating app.
        :param amount: amount of labels needed
        :return: string list with generic test labels
        """
        labels: list[str] = []
        for i in range(1, amount+1):
            padded_numer = str(i).zfill(2)
            labels.append(app.capitalize()+"Test" + padded_numer)
        return labels
