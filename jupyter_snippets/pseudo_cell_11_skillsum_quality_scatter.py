"""
Author: Maximilian Schiedermeier
"""
from restify_mining.plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.summed_skill_extractor import SummedSkillExtractor
from restify_mining.plotters.scatter_series import ScatterSeries


def cell_11() -> None:
    """
    Jupyter cell 11. See markdown description.
    :return: None
    """
    # Plot final correlations for the summed skill vectors
    scatter_series_summed_skills: ScatterSeries = ScatterSeries(SummedSkillExtractor,
                                                                MethodologyPassrateExtractor,
                                                                FullLabelMaker(),
                                                                False, "11-")
    scatter_series_summed_skills.plot_coupled_series({"ide", "tc"})
