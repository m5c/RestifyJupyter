"""Helper module to define the default order of tests for individual test applications. The tags
defined here mainly serve as markers on axis of produced
plots.
"""

xox_unit_tests: list[str] = ["XoxGet",
                             "XoxPost",
                             "XoxIdGet",
                             "XoxIdDelete",
                             "XoxIdBoardGet",
                             "XoxIdPlayersGet",
                             "XoxIdPlayersIdActionsGet",
                             "XoxIdPlayersIdActionsPost"]
bs_unit_tests: list[str] = ["BookStoreIsbnsGet",
                            "BookStoreIsbnsIsbnGet",
                            "BookStoreIsbnsIsbnPut",
                            "BookStoreStocklocationsGet",
                            "BookStoreStocklocationsStocklocationGet",
                            "BookStoreStocklocationsStocklocationIsbnsGet",
                            "BookStoreStocklocationsStocklocationIsbnsPost",
                            "BookStoreIsbnsIsbnCommentsGet",
                            "BookStoreIsbnsIsbnCommentsPost",
                            "BookStoreIsbnsIsbnCommentsDelete",
                            "BookStoreIsbnsIsbnCommentsCommentPost",
                            "BookStoreIsbnsIsbnCommentsCommentDelete"]


def all_unit_tests() -> list[str]:
    """
    Helper function to get fused markers for both application in single array. Order is always,
    first all bookstore markers, then all xox markers.
    """
    all_markers: list[str] = bs_unit_tests.copy()
    all_markers.append(xox_unit_tests)
    return all_markers
