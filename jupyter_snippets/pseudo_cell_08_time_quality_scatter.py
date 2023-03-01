"""
Author: Maximilian Schiedermeier
"""
from restify_mining.plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.methodology_time_extractor import MethodologyTimeExtractor
from restify_mining.plotters.scatter_series import ScatterSeries


def cell_08() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    scatter_series: ScatterSeries = ScatterSeries(MethodologyTimeExtractor,
                                                  MethodologyPassrateExtractor, FullLabelMaker(),
                                                  True, "08-", True)
    scatter_series.plot_coupled_series({"ide", "tc"})
