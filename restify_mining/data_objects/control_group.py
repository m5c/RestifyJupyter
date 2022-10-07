"""
Data object representing a control group, that is to say colour (string) and associated
methodology and application order.
"""
from restify_mining.data_objects.task_application import TaskApplication
from restify_mining.data_objects.task_methodology import TaskMethodology


class ControlGroup:
    """
    Groups control group specific fields.
    """

    # Disable nonsense pylint warnings. This is a bean, the whole purpose is to group data.
    # pylint: disable=too-many-arguments
    # pylint: disable=too-few-public-methods
    def __init__(self, name: str, first_app: TaskApplication, second_app: TaskApplication,
                 first_methodology: TaskMethodology, second_methodology: TaskMethodology):
        """
        Constructor for data object representing all information for a given control group.
        :param name: name of the control group, all lower case.
        :param first_app: enum defining first app refactored by participants of this control group.
        :param second_app: enum defining second app refactored by participants of this control
        group.
        :param first_methodology: enum defining first methodology applied by participants of this
        control group.
        :param second_methodology: enum defining second methodology applied by participants of
        this control group.
        """
        self.__name = name
        self.__first_app = first_app
        self.__second_app = second_app
        self.__first_methodology = first_methodology
        self.__second_methodology = second_methodology

    @property
    def name(self) -> str:
        """
        Just a getter.
        :param self: self reference
        :return: the control group's string name
        """
        return self.__name

    @property
    def first_app(self) -> TaskApplication:
        """
        Just a getter.
        :param self: self reference
        :return: the control group's first application
        """
        return self.__first_app

    @property
    def second_app(self) -> TaskApplication:
        """
        Just a getter.
        :param self: self reference
        :return: the control group's second application
        """
        return self.__second_app

    @property
    def first_methodology(self) -> TaskMethodology:
        """
        Just a getter.
        :param self: self reference
        :return: the control group's second methodology
        """
        return self.__first_methodology

    @property
    def second_methodology(self) -> TaskMethodology:
        """
        Just a getter.
        :param self: self reference
        :return: the control group's second methodology
        """
        return self.__second_methodology
