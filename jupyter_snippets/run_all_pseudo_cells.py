"""
Run this file to imitate everything the Jupyter Notebook does, but in a single execution.
This script just sequentially calls everything sprinkled over the individual jupyter pseudo cells.
If you just want to replicate our data and plots, run this file, then check the contents of the
generated-* directories.
Author: Maximilian Schiedermeier
"""
import matplotlib

from jupyter_snippets.pseudo_cell_01_display_population_skill_stats import cell_01
from jupyter_snippets.pseudo_cell_02_display_cgroups_skill_boxplot import cell_02
from jupyter_snippets.pseudo_cell_03_merge_csvs import cell_03
from jupyter_snippets.pseudo_cell_04_compute_cgroup_skill_diffs import cell_04
from jupyter_snippets.pseudo_cell_05_multi_linear_model import cell_05
from jupyter_snippets.pseudo_cell_06_all_results_all_participants import cell_06
from jupyter_snippets.pseudo_cell_07_all_results_all_groups_radar import cell_07
from jupyter_snippets.pseudo_cell_08_all_tests_all_groups import cell_08
from jupyter_snippets.pseudo_cell_09_time_passrate_normal_test import cell_09
from jupyter_snippets.pseudo_cell_10_time_and_passrate_boxplot import cell_10
from jupyter_snippets.pseudo_cell_11_fused_group_statistic_tests import cell_11
from jupyter_snippets.pseudo_cell_12_pretime_time_scatter import cell_12
from jupyter_snippets.pseudo_cell_13_time_passrate_scatter import cell_13
from jupyter_snippets.pseudo_cell_14_pretime_passrate_scatter import cell_14
from jupyter_snippets.pseudo_cell_15_skill_passrate_scatter import cell_15
from jupyter_snippets.pseudo_cell_16_skillsum_passrate_scatter import cell_16
from jupyter_snippets.pseudo_cell_18_fail_cause_stage_1 import cell_18
from jupyter_snippets.pseudo_cell_21_pearson_pretime_skillsum import cell_21
from jupyter_snippets.pseudo_cell_22_participant_feedback import cell_22

from restify_mining.utils.cache_clearer import clear_cache

print("Clearing cached output files...")
clear_cache("generated-csv-files")
clear_cache("generated-plots")
clear_cache("generated-text-files")
print("Clear cache complete.")

# print("Imitating Jupyter Pseudo Cell 01...")
# cell_01()
# print("Cell 01 complete.\n")
#
# print("Imitating Jupyter Pseudo Cell 02...")
# cell_02()
# print("Cell 02 complete.\n")

print("Imitating Jupyter Pseudo Cell 03...")
cell_03()
print("Cell 03 complete.\n")

print("Imitating Jupyter Pseudo Cell 04...")
cell_04()
print("Cell 04 complete.\n")

print("Imitating Jupyter Pseudo Cell 05...")
cell_05()
print("Cell 05 complete.\n")

print("Imitating Jupyter Pseudo Cell 06...")
cell_06()
print("Cell 06 complete.\n")
#
print("Imitating Jupyter Pseudo Cell 07...")
cell_07()
print("Cell 07 complete.\n")

print("Imitating Jupyter Pseudo Cell 08...")
cell_08()
print("Cell 08 complete.\n")

print("Imitating Jupyter Pseudo Cell 09...")
cell_09()
print("Cell 09 complete.\n")

print("Imitating Jupyter Pseudo Cell 10...")
cell_10()
print("Cell 10 complete.\n")

print("Imitating Jupyter Pseudo Cell 11...")
cell_11()
print("Cell 11 complete.\n")

print("Imitating Jupyter Pseudo Cell 12...")
cell_12()
print("Cell 12 complete.\n")

print("Imitating Jupyter Pseudo Cell 13...")
cell_13()
print("Cell 13 complete.\n")

print("Imitating Jupyter Pseudo Cell 14...")
cell_14()
print("Cell 14 complete.\n")

## 15 / 16 deactivated becaus pyplot suddenly communicates over localhost and sets a nonsense threshold. :/
print("Imitating Jupyter Pseudo Cell 15...")
cell_15()
print("Cell 15 complete.\n")

print("Imitating Jupyter Pseudo Cell 16...")
cell_16()
print("Cell 16 complete.\n")

# Cell 17 is deprecated and has been excluded from the paper. See module description of cell.
#
print("Imitating Jupyter Pseudo Cell 18...")
cell_18()
print("Cell 18 complete.\n")
# Cell 19 is deprecated and has been excluded from the paper. See module description of cell.
# Cell 20 is deprecated and has been excluded from the paper. See module description of cell.
#
print("Imitating Jupyter Pseudo Cell 21...")
cell_21()
print("Cell 21 complete.\n")

print("Imitating Jupyter Pseudo Cell 22...")
cell_22()
print("Cell 22 complete.\n")

print("Success!")
print("All Jupyter Cells imitated.")
print("Your data is in\n - generated-csv-files/*\n - generated-plots/*")
