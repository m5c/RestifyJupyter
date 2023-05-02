"""Helper module to define the default tint for control-group visualization. This means this
module provides a map form group names to colour spaces."""

group_tints = {"red": "#FF0000",
               "green": "#00FF00",
               "blue": "#0000FF",
               "yellow": "#E5CB00",
               "orange": '#ffa500',
               "turquoise": '#00ffff'}


def group_to_tint(group_name: str):
    """
    Helper function for case-insensitive resolution of group names to tints.
    :param group_name: as the upper / lower or mixed case string name of a control group,
    e.g. "Green"
    :return: hexadecimal value encoded as string, representing the colour associated to the
    provided group name.
    """
    return group_tints.get(group_name.lower())
