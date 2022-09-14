"""Helper module to define the default order of tests for individual test applications. The tags
defined here mainly serve as markers on axis of produced
plots.
"""

xox_unit_tests = ["XoxGet",
                  "XoxPost",
                  "XoxIdGet",
                  "XoxIdDelete",
                  "XoxIdBoardGet",
                  "XoxIdPlayersGet",
                  "XoxIdPlayersIdActionsGet",
                  "XoxIdPlayersIdActionsPost"]
bs_unit_tests = ["BookStoreIsbnsGet",
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
