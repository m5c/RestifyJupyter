from jupyter_snippets.pseudo_cell_09_time_and_passrate_boxplot import partition_population
from restify_mining.data_objects.assessed_participant import AssessedParticipant


def cell_10() -> None:
    """
    Jupyter cell 10. See markdown description.
    :return: None
    """
    partitioned_population: list[list[AssessedParticipant]] = partition_population()

    # Run wilcoxon rank sum between orange BS / turquoise bookstore: time distribution (& passrate?)
    # TODO: implement...
    # orange_xox_samples: list[int] = partitioned_population[4]

    # Run wilcoxon rank sum between orange xox / turquoise xox: time distribution (& passrate ?)
