"""
Label extractor abstract superclass. Implementations return ordered list of participant labels,
based on received collection and the labeling strategy they implement.
Author: Maximilian Schiedermeier
"""

from abc import ABC, abstractmethod

from csv_tools.file_load_utils import load_label_overrides
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant import Participant


class LabelMaker(ABC):

    def __init__(self):
        """
        Base constructor. Parses override file and stores it in filter list.
        """
        self.__label_overrides: list[str] = load_label_overrides()

    @abstractmethod
    def make_labels(self, participants: list[AssessedParticipant], reduce_to_overrides: bool) -> \
            list[str]:
        """
        Abstract label maker method. All label makers must implement this method with their own
        strategy.
        :param participants: as the set of participants to create labels for.
        :param reduce_to_overrides: set to true to apply a filter that stripes all non-outliers to
        the empty string.
        :return: list of participant labels.
        """

    @property
    def label_overrides(self):
        """
        Getter for the list of label overrides.
        :return: full list of all participants marked for override (reduction to matching
        participants)
        """
        return self.__label_overrides

    def is_in_override(self, participant: Participant) -> bool:
        """
        Helper method to determine if a participant is in override list
        :param participant: as the participant to check
        :return: boolean telling if participant object has match in override list.
        """
        return self.__label_overrides.__contains__(
            participant.group_name.lower() + "-" + participant.animal_name.lower())
