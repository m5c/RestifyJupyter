import numpy
import numpy as np
from restify_mining.Participant import Participant


# compute the actual average of participant skills
def build_mean_skills(participants: list[Participant]):
    return [number / len(participants) for number in build_summed_skills(participants)]


# returns a vector of all a given skill over all participants
def extract_skill_values_by_index(index: int, participants: list[Participant]):
    skill_values = []
    for participant in participants:
        skill_values.append(participant.skills[index])
    return skill_values


# computes the standard deviation for a given set of skills
def compute_single_skill_deviation(skill_values):
    # mean = sum(skill_values)/len(skill_values)
    return numpy.std(skill_values)


def build_standard_deviation_skills(participants):
    standard_deviations = []
    amount_skills = len(participants[0].skills)
    for skill_index in range(amount_skills):
        skill_values = extract_skill_values_by_index(skill_index, participants)
        standard_deviations.append(compute_single_skill_deviation(skill_values))
    return standard_deviations


# compute the normalized vector of participant skills
def build_normalized_skills(participants):
    summed_skills = build_summed_skills(participants)
    return summed_skills / np.sqrt(np.sum(summed_skills ** 2))


# computes a summed vector of all participant skills
def build_summed_skills(participants):
    # sum of all participant skills
    summed_skills = [0, 0, 0, 0, 0, 0, 0, 0]
    for participant in participants:
        # print(summed_skills)
        # print(participant)
        # print(participant.get_skills())
        summed_skills = np.add(summed_skills, participant.get_skills())
        # to convert to list of ints: [int(x) for x in participant.get_skills()]
    return summed_skills
