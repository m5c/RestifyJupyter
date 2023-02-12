"""
Author: Maximilian Schiedermeier
"""
from restify_mining.plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.skill_extractor import SkillExtractor
from restify_mining.plotters.scatter_series import ScatterSeries
from restify_mining.markers.skills_markers import full_skill_tags


def cell_09() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    scatter_series: ScatterSeries = ScatterSeries(
        SkillExtractor, MethodologyPassrateExtractor, FullLabelMaker(),
        True, "09-")
    scatter_series.plot_uncoupled_series(
        {"ide", "tc"}, full_skill_tags)
