"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.participant import Participant
from restify_mining.skill_extractors.extract_population_gaussian import extract_population_gaussian
from restify_mining.skill_extractors.participant_stat_tools import \
    compute_shapiro_will_skills_standarddev_pvalue


def cell_01() -> None:
    """
    Jupyter cell 01. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    population: list[Participant] = file_load_utils.load_all_participants()

    # Provide evidence that skill data is approximately normal distributed.
    compute_shapiro_will_skills_standarddev_pvalue(population)
