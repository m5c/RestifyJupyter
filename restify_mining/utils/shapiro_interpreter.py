"""
Helper module to print interpretation of values from a shapiro-wilk test for normal distribution.
Useful to provide a direct explanation of the results.
Author: Maximilian Schiedermeier
"""
from scipy.stats._morestats import ShapiroResult


def print_normal_dist_interpretation(context: str, shapiro: ShapiroResult) -> None:
    """
    Helper function to print p value and interpretation for a given context
    :param context: as descriptive string to use when printing message
    :param shapiro: ShapiroResult object containing certainty and p-value for null hypothesis
    :return: None.
    """
    if shapiro.pvalue >= 0.05:
        interpretation: str = "\nCannot reject Null-Hypothesis. Found no evidence to assume " \
                              "the samples could not come from a normal distribution."
    else:
        interpretation: str = "\nNull-Hypothesis rejected. Data suggests the samples do not " \
                              "come from a normal distribution."
    print("------\np-value for " + context + ": " + str(shapiro.pvalue) + interpretation)
