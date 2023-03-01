"""
Extractor for all summed skills of participant.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.markers.skills_markers import full_skill_tags
from restify_mining.plotters.extractors.extractor import Extractor


class SummedSkillExtractor(Extractor):
    """
    Skill specific implementation of the Extractor abstract type.
    """

    def __init__(self, whatever: str):
        """
        Overloaded constructor is required, even if we discard the parameter.
        :param whatever: something to discard. Usually extractors change comportment based on the
        initial parameter. This one is the exception.
        """
        None

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        # create skill sum
        summed_skills_across_participants: list[float] = []
        for participant in participants:
            summed_skills_across_participants.append(sum(participant.skills))
        return summed_skills_across_participants

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return "Self-declared proficiency sum"

    def filename_segment(self) -> str:
        return "SkillSum"
