"""
This module computes and prints the maximum skill difference between any pair of control groups,
for all skill. Highlights the greatest (worst competence comparability) of these values as metric
for the given control group distribution. A preliminary goal in search for a meaningful partition
was the minimization of this value (Search for MiniMax). The current value is worse is not the best
possible solution, since the population evolved over time (enrolled participants dropping out and
being replaced).
"""

from restify_mining.participant import Participant
from restify_mining import participant_filter_tools as pft
from restify_mining.skills import full_skill_tags, skill_tags, get_formated_skill_tag
from csv_tools import file_load_utils

# Load all participant objects (specifies skills, codename, control group) from csv file
population: list[Participant] = file_load_utils.load_all_participants()

# Prepare variables to remember worst average difference and corresponding index
worst_min_max_diff: float = 0.0
worst_min_max_diff_index: int = 0

# Iterate over skills and for each compute the average score difference for any pair of control
# groups. Print the highest (worst) value found.
control_groups: list[str] = pft.get_group_names(population)
for skill_index, skill in enumerate(skill_tags):

    # Compute average skill value for each control group
    average_skill_values = []
    for control_group in control_groups:
        control_group_population = pft.filter_population_by_group(population, control_group)
        average_skill_values.append(
            pft.get_average_skill_value_by_index(control_group_population, skill_index))

    # Print line with lowers, highest and max diff values for given skill:
    avg_min: float = min(average_skill_values)
    avg_max: float = max(average_skill_values)
    avg_min_max_diff = avg_max - avg_min

    # Update high-score if the results for this skill are worse than anything encountered so far
    if avg_min_max_diff > worst_min_max_diff:
        worst_min_max_diff = avg_min_max_diff
        worst_min_max_diff_index = skill_index

    # Print the stats for the current skill
    print(get_formated_skill_tag(skill_index) + ": \tAVG_MIN=" + str(round(avg_min, 1))
          + ",\tAVG_MAX=, " + str(round(avg_max, 1)) +
          ",\tMAX_AVG_DIFF=" + str(round(avg_max - avg_min, 1)))

# Print the name of the skill that serves as metric for this partition.
print("--------------")
print(
    "The worst difference in average skill values between two control groups in the given "
    "partition appears for:")
print("\t\"" + full_skill_tags[worst_min_max_diff_index] + "\", with a difference of " + str(
    round(worst_min_max_diff, 1)))
