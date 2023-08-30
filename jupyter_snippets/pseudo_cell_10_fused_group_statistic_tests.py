import scipy
from scipy.stats._stats_py import RanksumsResult

from jupyter_snippets.pseudo_cell_09_time_and_passrate_boxplot import partition_population
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor


def cell_10() -> None:
    """
    Jupyter cell 10. See markdown description.
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

    # Compute average / mean (non normalized) effect size:



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
