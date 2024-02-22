"""
Note: This class is deprecated and has been excluded from the paper. There is no need to
normalize participant metrics for any of the statistical tests reported in the paper.
This class extends assessed participants by all fields that require normalization, that is to say
knowledge about the entire population. An example is task solve time for a given methodology or
application. Upper and lower bound are defined by the min and max value of the population. This
class allows for convenient extension of assessed participants by the affected fields.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant


class NormalizedParticipant(AssessedParticipant):
    """Normalized Participant class. See Module Description."""

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes

    def __init__(self, participant: AssessedParticipant, norm_time_bs: float,
                 norm_time_xox: float, norm_time_ide: float,
                 norm_time_tc: float):
        """
        :type self: object
        """
        # invoke super with base attributes
        # NOTE: we exclude crash times for this analysis. It is deprecated for the metric was
        # considered contrived (confounding of dependent variables)
        super().__init__(participant.group_name + "-" + participant.animal_name,
                         participant.control_group, participant.skills,
                         participant.test_results_bs, participant.test_results_xox,
                         participant.time_bs,
                         participant.time_xox, participant.pre_time_tc, participant.pre_time_ide)
        self.__norm_time_bs = norm_time_bs
        self.__norm_time_xox_by_app = norm_time_xox
        self.__norm_time_ide_by_meth = norm_time_ide
        self.__norm_time_tc_by_meth = norm_time_tc

    @property
    def norm_time_bs(self) -> float:
        """
        Python pseudo getter for private normalized bookstore solving time field, with respect to
        all bookstore solving times no matter the methodology.
        :return: normalized bookstore time
        """
        return self.__norm_time_bs

    @property
    def norm_time_xox(self) -> float:
        """
        Python pseudo getter for private normalized xox solving time field, with respect to
        all xox solving times no matter the methodology.
        :return: normalized bookstore time
        """
        return self.__norm_time_xox_by_app

    @property
    def norm_time_ide(self) -> float:
        """
        Python pseudo getter for private normalized ide solving time field, with respect to
        all ide solving times no matter the application.
        :return: normalized ide time
        """
        return self.__norm_time_ide_by_meth

    @property
    def norm_time_tc(self) -> float:
        """
        Python pseudo getter for private normalized touchcore solving time field, with respect to
        all touchcore solving times no matter the application.
        :return: normalized touchcore time
        """
        return self.__norm_time_tc_by_meth
