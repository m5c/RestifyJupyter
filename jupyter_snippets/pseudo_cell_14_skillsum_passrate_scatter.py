"""
Author: Maximilian Schiedermeier
"""
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.summed_skill_extractor import SummedSkillExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries


def cell_14() -> None:
    """
    Jupyter cell 14. See markdown description.
    :return: None
    """
    # Plot final correlations for the summed skill vectors
    scatter_series_summed_skills: ScatterSeries = ScatterSeries(SummedSkillExtractor,
                                                                MethodologyPassrateExtractor,
                                                                FullLabelMaker(),
                                                                False, "14-")
    scatter_series_summed_skills.plot_coupled_series({"ide", "tc"})
