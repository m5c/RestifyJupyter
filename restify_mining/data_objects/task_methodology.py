"""
Defines enum for the two different task methodologies, refactoring with TouchCORE (tool assisted)
and manual refactoring with IntelliJ.
"""
from enum import Enum


class TaskMethodology(Enum):
    """
    Enum definition for both methodologies.
    """
    ASSISTED = 1
    MANUAL = 2
