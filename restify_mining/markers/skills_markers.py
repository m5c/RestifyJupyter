"""Helper module to define the default order of skills as strings and the corresponding
hexadecimal colour codes. The tags defined here mainly serve as markers on axis of produced
plots."""

full_skill_tags = ['Java', 'Spring', 'Maven', 'TouchCORE', 'UNIX', 'REST', 'Singleton',
                   'Reflection']
skill_tags = ['Java', 'Spring', 'MVN', 'T.CORE', 'UNIX', 'REST', 'Singl.', 'Refl.']
palette = ["#8d8d8d", "#5ce7cb", "#5ca6e7", "#7a5ce7", "#d75ce7", "#e75c90", "#e7865c", "#747474"]


def get_formated_skill_tag(skill_index: int) -> str:
    """
    Returns a format string consisting of the skill tag and a buffer of zero to many tabs.
    Ensures the skill is printed with
    consistent string width, compared to all other skills.
    :param skill_index: as the skill for which a format buffer is required
    :return: the buffer string, ensuring this skill is formatted with the required amount of tabs.
    """
    unbuffered_string = skill_tags[skill_index]
    if len(unbuffered_string) > 6:
        return unbuffered_string
    return unbuffered_string + "\t"
