"""
Author: Maximilian Schiedermeier
"""

from csv_tools import file_load_utils
from restify_mining.data_objects.participant import Participant
from restify_mining.skill_extractors.extract_control_group_boxplot import \
    extract_control_groups_boxplot


def cell_02() -> None:
    """
    Jupyter cell 02. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    population: list[Participant] = file_load_utils.load_all_participants()

    # Compute, print and save boxplot skill distribution for individual control groups to disk.
    extract_control_groups_boxplot(population)
