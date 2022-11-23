"""
Run this file to imitate everything the Jupyter Notebook does, but in a single execution.
This script just sequentially calls everything sprinkled over the individual jupyter pseudo cells.
If you just want to replicate our data and plots, run this file, then check the contents of the
generated-* directories.
Author: Maximilian Schiedermeier
"""
from jupyter_snippets.pseudo_cell_04_display_population_gaussian import cell_04
from jupyter_snippets.pseudo_cell_05_all_results_all_participants import cell_05
from jupyter_snippets.pseudo_cell_06_all_tests_all_groups import cell_06

print("Imitating Jupyter Pseudo Cell 04...")
cell_04()
print("Cell 04 complete.\n")

print("Imitating Jupyter Pseudo Cell 05...")
cell_05()
print("Cell 05 complete.\n")

print("Imitating Jupyter Pseudo Cell 06...")
cell_06()
print("Cell 06 complete.\n")

print("Success!")
print("All Jupyter Cells imitated.")
print("Your data is in\n - generated-csv-files/*\n - generated-plots/*")
