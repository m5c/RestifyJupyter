"""
This module consumes the "feedback.csv" file and visualizes its content as a bar chart.
"""
from csv_tools.file_load_utils import load_participant_feedback
from restify_mining.bar_plotters.frequency_bars import print_pref_distribution


def cell_22() -> None:
    """
    Jupyter cell 22. See markdown description.
    :return: None
    """
    # Step 1: Import feedback data (load all lines of CSV file into list of strings)
    feedback_all_lines: list[str] = load_participant_feedback()
    easier_methodology_line_items: list[str] = extract_line_items(feedback_all_lines[1])
    confidence_tests_line_items: list[str] = extract_line_items(feedback_all_lines[12])
    preferred_own_projects_line_items: list[str] = extract_line_items(feedback_all_lines[15])
    easier_methodology_stats: list[int] = extract_int_values(easier_methodology_line_items)
    confidence_tests_stats: list[int] = extract_int_values(confidence_tests_line_items)
    preferred_own_projects_stats: list[int] = extract_int_values(preferred_own_projects_line_items)

    print(easier_methodology_stats)
    print(confidence_tests_stats)
    print(preferred_own_projects_stats)

    # Step 2: Prepare data to plot
    # Barchart spacing with python is an utter nightmare, se we just create blank entries in a dict
    pseudo_dict: dict[int, int] = dict()
    pseudo_dict[0] = easier_methodology_stats[0]
    pseudo_dict[1] = easier_methodology_stats[1]
    pseudo_dict[2] = easier_methodology_stats[2]
    pseudo_dict[3] = 0
    pseudo_dict[4] = confidence_tests_stats[0]
    pseudo_dict[5] = confidence_tests_stats[1]
    pseudo_dict[6] = confidence_tests_stats[2]
    pseudo_dict[7] = 0
    pseudo_dict[8] = preferred_own_projects_stats[0]
    pseudo_dict[9] = preferred_own_projects_stats[1]
    pseudo_dict[10] = preferred_own_projects_stats[2]
    # Create x-tics descriptors

    # Create colours for options TC, Neutral, Manual (break)
    colour_map: dict[str, str] = {'DSL': '#66a9cd', 'Neutral': '#8f8f8f', 'Manual': '#f0ab4c',
                                  'Separator': '#ffffff'}
    x_tick_override: list[str] = ["", "Easier conversion", "", "", "", "More confident unit tests",
                                  "", "", "", "Preferred for future", ""]
    print_pref_distribution(pseudo_dict, x_tick_override, colour_map)


def extract_line_items(single_line: list[str]) -> list[str]:
    """
    Gets third value (CSV) of CSV line and further separates that value by whitespaces.
    """
    return single_line.split(',')[2].strip().split(' ')


def extract_int_values(string_list: list[str]) -> list[int]:
    """
    Gets the actual value from key:value item list.
    :return: the value as int
    """
    return [int(item.split(':')[1]) for item in string_list]
