import scipy
from scipy.stats._stats_py import RanksumsResult

from jupyter_snippets.pseudo_cell_09_time_and_passrate_boxplot import partition_population, \
    extract_methodology_metric
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor


def cell_10() -> None:
    """
    Jupyter cell 10. See markdown description.
    :return: None
    """
    partitioned_population: list[list[AssessedParticipant]] = partition_population()
    orange_samples: list[AssessedParticipant] = partitioned_population[4]
    turquoise_samples: list[AssessedParticipant] = partitioned_population[5]

    # Extract samples for both fused groups, per methodology/app combo, for both time and pass rate
    # Everything orange
    orange_bookstore_assisted_time_samples = MethodologyTimeExtractor("tc").extract(orange_samples)
    orange_bookstore_assisted_passrate_samples = MethodologyPassrateExtractor("tc").extract(
        orange_samples)
    orange_xox_manual_time_samples = MethodologyTimeExtractor("ide").extract(orange_samples)
    orange_xox_manual_passrate_samples = MethodologyPassrateExtractor("ide").extract(orange_samples)

    # Everything turquoise
    turquoise_bookstore_manual_time_samples = MethodologyTimeExtractor("ide").extract(
        turquoise_samples)
    turquoise_bookstore_manual_passrate_samples = MethodologyPassrateExtractor("ide").extract(
        turquoise_samples)
    turquoise_xox_assisted_time_samples = MethodologyTimeExtractor("tc").extract(turquoise_samples)
    turquoise_xox_assisted_passrate_samples = MethodologyPassrateExtractor("tc").extract(
        turquoise_samples)

    # Run Wilcoxon rank sum between orange BS / turquoise bookstore: time distribution (& passrate?)
    print("\nWilcoxon for BookStore (Time)")
    wilcoxon_bs_time: RanksumsResult = scipy.stats.ranksums(orange_bookstore_assisted_time_samples,
                                                    turquoise_bookstore_manual_time_samples)
    print(wilcoxon_bs_time)

    print("\nWilcoxon for BookStore (Pass Rate)")
    wilcoxon_bs_pass_rate: RanksumsResult = scipy.stats.ranksums(orange_bookstore_assisted_passrate_samples,
                                                    turquoise_bookstore_manual_passrate_samples)
    print(wilcoxon_bs_pass_rate)

    # Run Wilcoxon rank sum between orange xox / turquoise xox: time distribution (& passrate?)
    print("\nWilcoxon for Xox (Time)")
    wilcoxon_xox_time: RanksumsResult = scipy.stats.ranksums(orange_xox_manual_time_samples,
                                                    turquoise_xox_assisted_time_samples)
    print(wilcoxon_xox_time)

    print("\nWilcoxon for Xox (Pass Rate)")
    wilcoxon_xox_pass_rate: RanksumsResult = scipy.stats.ranksums(orange_xox_manual_passrate_samples,
                                                    turquoise_xox_assisted_passrate_samples)
    print(wilcoxon_xox_pass_rate)