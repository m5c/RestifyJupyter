"""
Implementation of LabelMaker that produces full labels with colour and animal names.
@Author Maximilian Schiedermeier
"""

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.label_maker import LabelMaker


class FullLabelMaker(LabelMaker):
    """
    Implementation of LabelMaker that produces full labels with colour and animal names.
    """

    def make_labels(self, participants: list[AssessedParticipant], reduce_to_outliers: bool) -> \
            list[str]:
        """
        Returns the full participant name as [colour]_[animal]
        :param participants: as the list of participants for which labels are wanted.
        :param reduce_to_outliers: set to true to apply a filter that stripes all non-outliers to
        the empty string.
        :return: list of strings, each entry carrying the full participant label.
        """

        result: list[str] = []
        for assessed_participant in participants:
            result.append(assessed_participant.animal_name)
        return result
