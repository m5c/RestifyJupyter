from csv_tools import file_load_utils
from restify_mining.assessed_participant import AssessedParticipant

# Load all participant objects (specifies skills, codename, controlgroup) from csv file
population: list[AssessedParticipant] = file_load_utils.load_all_assessed_participants()
for assessed_participant in population:
    print(assessed_participant)
print("OK.")