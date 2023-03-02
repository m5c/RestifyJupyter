"""
This module allows comparison of methodology fitness for a task by comparing the results of two
half of the total population.
Example: Compare Xox IDE and Xox TouchCORE. Compare the two groups who solved Xox using IntelliJ
to the two groups who solved Xox using TouchCORE.
The metric for fittness is the time to quality ratio. That is to say fast solving with few
mistakes is considered better than slow solving with many mistakes.
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group


def cell_12() -> None:
    """
    Jupyter cell 12. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Before we construct the tradeoff, we need to normalize the task solving times
    normalized_population: list[NormalizedParticipant] = []

    # In a first step we compute the effective methodology fittness. We do not use a dedicated
    # extractor for this, because extractors are meant for combination. We are not interested
    # in a scatter here, but comparison of resulting normal distributions.
    # First divide the population into two subsets, where each subset combined the participants
    # of two control groups with the same task-methodology combination.
    green_blue_population: list[AssessedParticipant] = filter_population_by_group(
        assessed_population, "green") + filter_population_by_group(assessed_population, "blue")
    red_yellow_population: list[AssessedParticipant] = filter_population_by_group(
        assessed_population, "red") + filter_population_by_group(assessed_population, "yellow")

    # Next we apply a tradeoff extractor on every subgroup, to determine
