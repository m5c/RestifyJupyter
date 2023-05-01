"""
This module consumes the "feedback.csv" file and visualizes its content as a bar chart.
"""
from csv_tools.file_load_utils import load_participant_feedback


def cell_18() -> None:
    """
    Jupyter cell 18. See markdown description.
    :return: None
    """
    # Step 1: Import feedback data
    feedback: list[str] = load_participant_feedback()
    easier_methodology: str = feedback[1]
    confidence_tests: str = feedback[12]
    preferred_own_projects: str = feedback[15]
    # print(easier_methodology)
    # print(confidence_tests)
    # print(preferred_own_projects)

    # Create a dict, pass to plotter...