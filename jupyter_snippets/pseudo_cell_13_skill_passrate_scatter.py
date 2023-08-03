"""
Author: Maximilian Schiedermeier
"""
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.skill_extractor import SkillExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries
from restify_mining.markers.skills_markers import full_skill_tags


def cell_13() -> None:
    """
    Jupyter cell 13. See markdown description.
    :return: None
    """
    # Plot correlations for all individual skills
    scatter_series_all_skills: ScatterSeries = ScatterSeries(
        SkillExtractor, MethodologyPassrateExtractor, FullLabelMaker(),
        True, "13-")
    scatter_series_all_skills.plot_uncoupled_series(
        {"ide", "tc"}, full_skill_tags)
