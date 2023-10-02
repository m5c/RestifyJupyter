"""
Author: Maximilian Schiedermeier
"""
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries


def cell_13() -> None:
    """
    Jupyter cell 12. See markdown description.
    :return: None
    """
    reduce_labels_to_outliers: bool = True
    scatter_series: ScatterSeries = ScatterSeries(MethodologyTimeExtractor,
                                                  MethodologyPassrateExtractor, FullLabelMaker(),
                                                  reduce_labels_to_outliers, "12-")
    scatter_series.plot_coupled_series({"ide", "tc"})
