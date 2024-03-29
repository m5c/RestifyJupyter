"""
Author: Maximilian Schiedermeier
"""

from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.skill_extractors.compute_cgroup_skill_diffs import compute_cgroup_skill_diffs


def cell_04() -> None:
    """
    Jupyter cell 04. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # Here, we still include outliers, as this is an experiment is a pretest.
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(False)

    # Compute and print skill diffs stats to assess comparability of individual control groups.
    compute_cgroup_skill_diffs(assessed_population)
