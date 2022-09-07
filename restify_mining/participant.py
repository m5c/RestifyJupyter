"""Represents an individual participant. Also encodes the corresponding control group and
codename. None of the metrics actually measured throughout the study are associated to any instance
of this class, those values are taken care of by subclasses."""


class Participant:
    """Participant class. Represents all information regarding a participant, that is not yet stored
    in the encompassing partition (group assignment / group characteristics)."""

    def __init__(self, codename: str, skills: list[int]):
        # received codename covers control group and animal name, e.g. something like purple-tiger
        self.__animal_name: str = codename.split('-')[0]
        self.__group_name: str = codename.split('-')[1]
        self.__skills: list[int] = skills

    @property
    def skills(self) -> list[int]:
        """Getter for skills. Returns an array of int valued, where each position represents a
        self-declared skill."""
        return self.__skills

    @property
    def total_score(self):
        """Computes the total score of all skills, summed up. Useful to create a participant
        ranking."""
        return sum(self.__skills)

    @property
    def skill_amount(self):
        """Helper method to look up how many skills were decrated for this pariticpant. TODO:
        make obsolete by declaring an enum class with with fixed strings / criteria."""
        return len(self.__skills)

    @property
    def animal_name(self):
        """Getter to look up the participant animal name."""
        return self.__animal_name

    @property
    def group_name(self):
        """Getter to look up the participant control group name."""
        return self.__group_name

    def __str__(self):
        participant_str = self.__name + ": ["
        for skill in self.skills:
            participant_str += str(skill) + ","
        participant_str += "]"
        return participant_str
