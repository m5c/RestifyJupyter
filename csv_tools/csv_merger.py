import pandas as pd

def build_merged_csv():
    """
    Reads in all individual csv files and merges them based on the participant. control group and
    code name entry. Stores the resulting fused csv in the "generated-csv-files" directory.
    """
    # Merge the individual key files. Use participant code name as key.
    tests_csv = pd.read_csv("source-csv-files/tests.csv")
    task_csv = pd.read_csv("source-csv-files/tasks.csv")
    skill_csv = pd.read_csv("source-csv-files/skills.csv")
    intermediate1 = tests_csv.merge(task_csv, on="codename")
    result = intermediate1.merge(skill_csv, on="codename")
    result.to_csv("generated-csv-files/restify.csv", index=None)
