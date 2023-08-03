"""
Author: Maximilian Schiedermeier
"""
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries


def cell_11() -> None:
    """
    Jupyter cell 09. See markdown description.
    :return: None
    """
    scatter_series: ScatterSeries = ScatterSeries(MethodologyTimeExtractor,
                                                  MethodologyPassrateExtractor, FullLabelMaker(),
                                                  True, "11-")
    scatter_series.plot_coupled_series({"ide", "tc"})
