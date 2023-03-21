"""
Author: Maximilian Schiedermeier
"""

from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries


def cell_10() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    scatter_series: ScatterSeries = ScatterSeries(
        MethodologyPretimeExtractor, MethodologyPassrateExtractor, FullLabelMaker(),
        True, "10-")
    scatter_series.plot_coupled_series({"ide", "tc"})
