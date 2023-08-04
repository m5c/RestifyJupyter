"""
Helper module to resolve a given group and application name to associated data (methodology and
order)
TODO: couple implementation to read from existing csv
Author: Maximilian Schiedermeier
"""

def group_app_to_methodology(group: str, app: str) -> str:
    """
    Turns a given group and app to the associated methodology
    :param group: as the group name red/green/blue/yellow
    :param app: as the app to refactor xox/bs
    :return: string describing the methodology
    """
    if group in ['red', 'yellow']:
        if app == 'bs':
            return 'DSL'
        return 'Manual'
    if app == 'bs':
        return 'Manual'
    return 'DSL'


def group_app_to_task_number(group: str, app: str) -> str:
    """
    Turns a given group and app to the associated task number
    :param group: as the group name red/green/blue/yellow
    :param app: as the app to refactor xox/bs
    :return: string describing the methodology
    """
    if group in ['red', 'green']:
        if app == 'bs':
            return '1st'
        return '2nd'
    if app == 'bs':
        return '2nd'
    return '1st'
