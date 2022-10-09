"""
Bundle class for time measured for a given participant. The time bundle only stores brute seconds
values and has no notion for task or methodology order.
"""


class TimeBundle:
    """
    Bundle class for time measured for a given participant. The time bundle only stores brute
    seconds values and has no notion for task or methodology order.
    """

    def __init__(self, seconds_tc_instructions: int, seconds_ide_instructions: int,
                 seconds_xox: int, seconds_bookstore: int, ):
        """
        Constructor for time bundle class. Stores all measured times in private fields.
        :param seconds_tc_instructions: as the time in seconds measured to follow the zoo
        touchcore video tutorial.
        :param seconds_ide_instructions: as the time in seconds measured to follow the zoo
        intellij video tutorial.
        :param seconds_xox: as the time in seconds measured to refactor the xox application.
        :param seconds_bookstore:  as the time in seconds measured to refactor the bookstore
        application.
        """
        self.__seconds_tc_instructions = seconds_tc_instructions
        self.__seconds_ide_instructions = seconds_ide_instructions
        self.__seconds_xox = seconds_xox
        self.__seconds_bookstore = seconds_bookstore

    @property
    def seconds_tc_instructions(self) -> int:
        """
        Just a getter.
        :return: private field __seconds_tc_instructions
        """
        return self.__seconds_tc_instructions

    @property
    def seconds_ide_instructions(self) -> int:
        """
        Just a getter.
        :return: private field __seconds_ide_instructions
        """
        return self.__seconds_ide_instructions

    @property
    def seconds_xox(self) -> int:
        """
        Just a getter.
        :return: private field __seconds_xox
        """
        return self.__seconds_xox

    @property
    def seconds_bookstore(self) -> int:
        """
        Just a getter.
        :return: private field __seconds_bookstore
        """
        return self.__seconds_bookstore
