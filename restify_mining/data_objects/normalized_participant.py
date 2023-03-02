"""
This class extends assessed participants by all fields that require normalization, that is to say
knowledge about the entire population. An example is task solve time for a given methodology or
application. Upper and lower bound are defined by the min and max value of the population. This
class allows for convenient extension of assessed participants by the affected fields.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.control_group import ControlGroup


class NormalizedParticipant(AssessedParticipant):
    """Normalized Participant class. See Module Description."""

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes

    def __init__(self, codename: str, control_group: ControlGroup, skills: list[int],
                 test_results_bs: list[bool], test_results_xox: list[bool], time_bs: int,
                 time_xox: int, pre_time_tc: int, pre_time_ide: int, norm_time_bs_by_app: float,
                 norm_time_xox_by_app: float, norm_time_ide_by_meth: float,
                 norm_time_tc_by_meth: float):
        """
        :type self: object
        """
        # invoke super with base attributes
        super().__init__(codename, control_group, skills,
                         test_results_bs, test_results_xox, time_bs,
                         time_xox, pre_time_tc, pre_time_ide)
        self.__norm_time_bs_by_app = norm_time_bs_by_app
        self.__norm_time_xox_by_app = norm_time_xox_by_app
        self.__norm_time_ide_by_meth = norm_time_ide_by_meth
        self.__norm_time_tc_by_meth = norm_time_tc_by_meth

    @property
    def norm_time_bs_by_app(self) -> float:
        """
        Python pseudo getter for private normalized bookstore solving time field, with respect to
        all bookstore solving times no matter the methodology.
        :return: normalized bookstore time
        """
        return self.____norm_time_bs_by_app

    @property
    def __norm_time_xox_by_app(self) -> float:
        """
        Python pseudo getter for private normalized xox solving time field, with respect to
        all xox solving times no matter the methodology.
        :return: normalized bookstore time
        """
        return self.__norm_time_xox_by_app

    @property
    def __norm_time_ide_by_meth(self) -> float:
        """
        Python pseudo getter for private normalized ide solving time field, with respect to
        all ide solving times no matter the application.
        :return: normalized ide time
        """
        return self.__norm_time_ide_by_meth

    @property
    def __norm_time_tc_by_meth(self) -> float:
        """
        Python pseudo getter for private normalized touchcore solving time field, with respect to
        all touchcore solving times no matter the application.
        :return: normalized touchcore time
        """
        return self.__norm_time_tc_by_meth
