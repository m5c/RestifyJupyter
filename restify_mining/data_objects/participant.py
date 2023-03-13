"""Represents an individual participant. Also encodes the corresponding control group and
codename. None of the metrics actually measured throughout the study are associated to any instance
of this class, those values are taken care of by subclasses."""
from restify_mining.data_objects.control_group import ControlGroup


class Participant:
    """Participant class. Represents all information regarding a participant, that is not yet stored
    in the encompassing partition (group assignment / group characteristics)."""

    def __init__(self, codename: str, control_group: ControlGroup, skills: list[int]):
        # received codename covers control group and animal name, e.g. something like purple-tiger
        self.__animal_name: str = codename.split('-')[1]
        self.__control_group: ControlGroup = control_group
        self.__skills: list[int] = skills

    @property
    def skills(self) -> list[int]:
        """Getter for skills. Returns an array of int valued, where each position represents a
        self-declared skill."""
        return self.__skills

    def get_skill_value(self, skill_index: int) -> int:
        """
        Getter for a specific skill value, based on the provided skill index
        :param skill_index: index of the skill following the default order
        :return: the self-declared skill value for the participant.
        """
        return self.skills[skill_index]

    @property
    def total_score(self) -> int:
        """Computes the total score of all skills, summed up. Useful to create a participant
        ranking."""
        return sum(self.__skills)

    @property
    def skill_amount(self) -> int:
        """Helper method to look up how many skills were decrated for this pariticpant. TODO:
        make obsolete by declaring an enum class with with fixed strings / criteria."""
        return len(self.__skills)

    @property
    def animal_name(self) -> str:
        """Getter to look up the participant animal name."""
        return self.__animal_name

    @property
    def group_name(self) -> str:
        """Getter to look up the participant control group name."""
        return self.__control_group.name

    @property
    def control_group(self) -> ControlGroup:
        """Getter for the actual control group object."""
        return self.__control_group

    def __str__(self):
        """
        tostring method for nice pretty formatted printing of object details.
        :return:
        """
        participant_str = self.group_name + "-" + self.animal_name + ": \t["
        for skill in self.skills:
            participant_str += str(skill) + ","
        participant_str += "]"
        return participant_str
