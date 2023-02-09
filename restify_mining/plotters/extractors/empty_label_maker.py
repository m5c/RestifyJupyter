"""
Implementation of LabelMaker that produces empty labels.
@Author Maximilian Schiedermeier
"""

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.label_maker import LabelMaker


class EmptyLabelMaker(LabelMaker):
    """
    Implementation of LabelMaker that produces empty labels.
    """

    def make_labels(self, participants: list[AssessedParticipant], reduce_to_outliers: bool) -> \
            list[str]:
        """
        Dummy method to create empty labels (no labels at all).
        :param participants: as the list of requested participants.
        :param reduce_to_outliers: set to true to apply a filter that stripes all non-outliers to
        the empty string.
        :return: empty labels.
        """
        empty_labels: list[str] = [''] * len(participants)
        return empty_labels
