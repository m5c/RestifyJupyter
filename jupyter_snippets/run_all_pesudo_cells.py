"""
Run this file to imitate everything the Jupyter Notebook does, but in a single execution.
This script just sequentially calls everything sprinkled over the individual jupyter pseudo cells.
If you just want to replicate our data and plots, run this file, then check the contents of the
generated-* directories.
Author: Maximilian Schiedermeier
"""

from jupyter_snippets.pseudo_cell_01_display_population_skills_gaussian import cell_01
from jupyter_snippets.pseudo_cell_02_display_cgroups_skill_boxplot import cell_02
from jupyter_snippets.pseudo_cell_03_merge_csvs import cell_03
from jupyter_snippets.pseudo_cell_04_compute_cgroup_skill_diffs import cell_04
from jupyter_snippets.pseudo_cell_05_all_results_all_participants import cell_05
from jupyter_snippets.pseudo_cell_06_all_tests_all_groups import cell_06
from jupyter_snippets.pseudo_cell_07_quality_vectors import cell_07
from restify_mining.utils.cache_clearer import clear_cache

print("Clearing cached output files...")
clear_cache("generated-csv-files")
clear_cache("generated-plots")
print("Clear cache complete.")

print("Imitating Jupyter Pseudo Cell 01...")
cell_01()
print("Cell 01 complete.\n")

print("Imitating Jupyter Pseudo Cell 02...")
cell_02()
print("Cell 02 complete.\n")

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


print("Imitating Jupyter Pseudo Cell 07...")
cell_07()
print("Cell 07 complete.\n")

print("Success!")
print("All Jupyter Cells imitated.")
print("Your data is in\n - generated-csv-files/*\n - generated-plots/*")
