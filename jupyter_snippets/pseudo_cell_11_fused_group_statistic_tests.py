import numpy
import scipy
from scipy.stats._morestats import ShapiroResult
from scipy.stats._stats_py import RanksumsResult

from jupyter_snippets.pseudo_cell_10_time_and_passrate_boxplot import partition_population
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor


def cell_11() -> None:
    """
    Jupyter cell 11. See markdown description.
    This cell runs a wilcoxon rank sum comparison for the performances of fused groups (same app
    / methodology but different order). It also quantifies effect size of the respective
    distributions. In total this produces 4 comparisons: 2 for bookstore (time & passrate) and
    2 for xox (time & passrate).
    :return: None
    """
    # Obtain (without scammers) all assessed participants, partitioned by group
    partitioned_population: list[list[AssessedParticipant]] = partition_population()
    orange_samples: list[AssessedParticipant] = partitioned_population[4]
    turquoise_samples: list[AssessedParticipant] = partitioned_population[5]

    # Extract samples for both fused groups, per methodology/app combo, for both time and pass rate
    # Everything orange
    orange_bookstore_assisted_time_samples: list[float] = MethodologyTimeExtractor("tc").extract(
        orange_samples)
    orange_bookstore_assisted_passrate_samples: list[float] = MethodologyPassrateExtractor(
        "tc").extract(
        orange_samples)
    orange_xox_manual_time_samples: list[float] = MethodologyTimeExtractor("ide").extract(
        orange_samples)
    orange_xox_manual_passrate_samples: list[float] = MethodologyPassrateExtractor("ide").extract(
        orange_samples)

    # Everything turquoise
    turquoise_bookstore_manual_time_samples: list[float] = MethodologyTimeExtractor("ide").extract(
        turquoise_samples)
    turquoise_bookstore_manual_passrate_samples: list[float] = MethodologyPassrateExtractor(
        "ide").extract(
        turquoise_samples)
    turquoise_xox_assisted_time_samples: list[float] = MethodologyTimeExtractor("tc").extract(
        turquoise_samples)
    turquoise_xox_assisted_passrate_samples: list[float] = MethodologyPassrateExtractor(
        "tc").extract(
        turquoise_samples)

    # Now that we have all samples to work with, we perform the wilcoxon rank sum comparion of
    # the distributions, for:
    # 1) BookStore
    #   -bookstore manual VS bookstore assisted: time
    #   -bookstore manual VS bookstore assisted: passrate
    # 2) Xox
    #   -xox manual VS xox assisted: time
    #   -xox manual VS xox assisted: passrate
    wilcoxon_fused_group_analysis("BookStore (Time)", orange_bookstore_assisted_time_samples,
                                  turquoise_bookstore_manual_time_samples)
    wilcoxon_fused_group_analysis("BookStore (PassRate)",
                                  orange_bookstore_assisted_passrate_samples,
                                  turquoise_bookstore_manual_passrate_samples)
    wilcoxon_fused_group_analysis("Xox (Time)", orange_xox_manual_time_samples,
                                  turquoise_xox_assisted_time_samples)
    wilcoxon_fused_group_analysis("Xox (PassRate)", orange_xox_manual_passrate_samples,
                                  turquoise_xox_assisted_passrate_samples)

    # Wilcoxon only tells if the distributions are different, but does not compute effect size.
    # We compute means (average) as non-normalized effect size, and CohensD as normalized effect
    # size. The latter requires an additional Shapiro-Wilk test, because CohensD cannot be used
    # for non-normal distributions.

    # Compute average / mean (non normalized) effect size and print markdown table
    print(
        "\n\n| Metric | Orange Median | Turquoise Median | Median Offset | Orange Average | "
        "Turquoise "
        "Average | Average Offset |")
    print("|---|---|---|---|---|---|---|")
    print(computeAverageAndMedianSampleSetDiffs("BookStore (Time)",
                                                orange_bookstore_assisted_time_samples,
                                                turquoise_bookstore_manual_time_samples))
    print(computeAverageAndMedianSampleSetDiffs("BookStore (PassRate)",
                                                orange_bookstore_assisted_passrate_samples,
                                                turquoise_bookstore_manual_passrate_samples))
    print(computeAverageAndMedianSampleSetDiffs("Xox (Time)", orange_xox_manual_time_samples,
                                                turquoise_xox_assisted_time_samples))
    print(
        computeAverageAndMedianSampleSetDiffs("Xox (PassRate)", orange_xox_manual_passrate_samples,
                                              turquoise_xox_assisted_passrate_samples))
    print("\n")

    # Next we compute a normalized effect size table using CohensD.
    # We begin by testing all sample sets for normal distribution.
    # Note: For PassRate the Shaprio Wilk almost certainly rejects the null hypothesis of an
    # underlying normal distributions. Given the fixed amount of tests, app possible outcomes lie
    # on discrete intervals. Whereas time is a continous like spectrum.
    # In return, CohensD should not be used for passrate, only for time.
    test_normal_distr("Orange BookStore Assisted Time", orange_bookstore_assisted_time_samples)
    test_normal_distr("Turquoise BookStore Manual Time", turquoise_bookstore_manual_time_samples)
    test_normal_distr("Orange BookStore Assisted PassRate",
                      orange_bookstore_assisted_passrate_samples)
    test_normal_distr("Turquoise BookStore Manual PassRate",
                      turquoise_bookstore_manual_passrate_samples)
    test_normal_distr("Orange Xox Manual Time", orange_xox_manual_time_samples)
    test_normal_distr("Turquoise Xox Assisted Time", turquoise_xox_assisted_time_samples)
    test_normal_distr("Orange Xox Manual PassRate", orange_xox_manual_passrate_samples)
    test_normal_distr("Turquoise Xox Assisted PassRate", turquoise_xox_assisted_passrate_samples)

    # Compute CohensD for time distributions of fused groups:
    print("\nCohen's D for BookStore (Time):")
    print(compute_cohensd(orange_bookstore_assisted_time_samples,
                          turquoise_bookstore_manual_time_samples))

    print("\nCohen's D for Xox (Time):")
    print(compute_cohensd(orange_xox_manual_time_samples,
                          turquoise_xox_assisted_time_samples))
    print("\n")

    # Compute CohensD for passrate distributions of fused groups:
    print("\nCohen's D for BookStore (PassRate):")
    print(compute_cohensd(orange_bookstore_assisted_passrate_samples,
                          turquoise_bookstore_manual_passrate_samples))

    print("\nCohen's D for Xox (PassRate):")
    print(compute_cohensd(orange_xox_manual_passrate_samples,
                          turquoise_xox_assisted_passrate_samples))
    print("\n")


def compute_cohensd(sample_set_1: list[float], sample_set_2: list[float]) -> float:
    """
    Implementation of Cohen's D effect size for sample sets of non-equal size. This is relevant,
    because the fused groups are of different size (we filtered the scammer).
    This implementation uses the pooled standard deviation to compute the weighted sum of individual
    sample set standard deviations.
    Implementation based on: https://stackoverflow.com/a/33002123/13805480
    """
    sample_size_1: int = len(sample_set_1)
    sample_size_2: int = len(sample_set_2)

    cohens_d_nominator: float = (numpy.mean(sample_set_1) - numpy.mean(sample_set_2))
    pooled_std_denominator: float = sample_size_1 + sample_size_2 - 2
    pooled_std: float = numpy.sqrt(
        ((sample_size_1 - 1) * numpy.std(sample_set_1, ddof=1) ** 2 + (
                sample_size_2 - 1) * numpy.std(sample_set_2, ddof=1) ** 2) / pooled_std_denominator)

    return cohens_d_nominator / pooled_std


# return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)


def wilcoxon_fused_group_analysis(title: str, sample_fused_group_1: list[float],
                                  samples_fused_group_2: list[float]) -> None:
    """
    Function to perform a Wilcoxon rank sum test for two sample lists (fused groups orange /
    turquoise), then print title and results. The test tells (in simplified terms) if the
    distributions of the two provided sample sets are distinct.
    :param title: string to print as label before printing test restults
    :param sample_fused_group_1: as the first sample set to compare
    :param samples_fused_group_2: as the second sample set to compare
    :return: None
    """
    print("\nWilcoxon for: " + title)
    wilcoxon_result: RanksumsResult = scipy.stats.ranksums(
        sample_fused_group_1,
        samples_fused_group_2)
    print(wilcoxon_result)


def computeAverageAndMedianSampleSetDiffs(metric: str,
                                          orange_samples: list[float],
                                          turquoise_samples: list[
                                              float]) -> str:
    """
    :param metric: descriptive comparison text of sample nature
    :param orange_samples:
    :param turquoise_samples:
    :return: MarkDown table line describing compared sample sets, respecitive average and means
    and their offsets.
    """
    orange_samples_median: float = numpy.median(orange_samples)
    turquoise_samples_median: float = numpy.median(turquoise_samples)
    median_offset: float = abs(orange_samples_median - turquoise_samples_median)

    orange_samples_average: float = numpy.average(orange_samples)
    turquoise_sample_average: float = numpy.average(turquoise_samples)
    average_offset: float = abs(orange_samples_average - turquoise_sample_average)

    return "| " + metric \
        + " | " + str(round(orange_samples_median, 1)) \
        + " | " + str(round(turquoise_samples_median, 1)) \
        + " | " + str(round(median_offset, 1)) \
        + " | " + str(round(orange_samples_average, 1)) \
        + " | " + str(round(turquoise_sample_average, 1)) \
        + " | " + str(round(average_offset, 1)) \
        + " |"


def test_normal_distr(title: str, samples: list[float]) -> None:
    """
    The Shapiro-Wilk test tests the null hypothesis that the data was drawn from a normal
    distribution.
    Prints result to console.
    :param samples: list of all raw amples.
    :return: None
    """
    shapiro_result: ShapiroResult = scipy.stats.shapiro(samples)
    print("---\n" + title)
    print(shapiro_result)
    print(shapiro_result.pvalue > 0.05)
    print(
        "False: Null Hypothesis rejected. The probability to obtain these samples from a normal "
        "distribution is below 0.05")
