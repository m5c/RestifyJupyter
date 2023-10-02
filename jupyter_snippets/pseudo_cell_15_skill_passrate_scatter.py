"""
Author: Maximilian Schiedermeier
"""
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.skill_extractor import SkillExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries
from restify_mining.markers.skills_markers import full_skill_tags


def cell_15() -> None:
    """
    Jupyter cell 15. See markdown description.
    :return: None
    """
    # Plot correlations for all individual skills
    reduce_labels_to_outliers: bool = False
    scatter_series_all_skills: ScatterSeries = ScatterSeries(
        SkillExtractor, MethodologyPassrateExtractor, FullLabelMaker(),
        reduce_labels_to_outliers, "15-")
    scatter_series_all_skills.plot_uncoupled_series(
        {"ide", "tc"}, full_skill_tags)
