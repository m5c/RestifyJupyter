"""
Extractor for series of values for a given skill, identified by skill tag.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.markers.skills_markers import full_skill_tags
from restify_mining.scatter_plotters.extractors.extractor import Extractor


class SkillExtractor(Extractor):
    """
    Skill specific implementation of the Extractor abstract type.
    """

    def __init__(self, skill_tag: str) -> Extractor:
        """
        Constructor of the skill extractor.
        :param: skill_tag: as string to indicate which skill values we are interested in.
        """
        if skill_tag in full_skill_tags:
            self.__skill_tag = skill_tag
        else:
            raise Exception("Invalid skill: " + skill_tag)

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:

        # look up index of target skill
        skill_index: int = full_skill_tags.index(self.__skill_tag)

        # create target list
        skill_value_across_participants: list[float] = []
        for participant in participants:
            skill_value_across_participants.append(float(participant.get_skill_value(skill_index)))
        return skill_value_across_participants

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return "Self-declared proficiency for " + self.__skill_tag.capitalize() + " [1-5]"

    def filename_segment(self) -> str:
        return self.__skill_tag.capitalize() + "Skill"
