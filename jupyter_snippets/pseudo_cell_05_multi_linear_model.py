"""
This module consumes the "restify.csv" file generated by pseudo cell 21 and creates a
multi-linear model for all factors of the experiment crossover layout.
The cell implementation strongly follows this tutorial:
https://www.sfu.ca/~mjbrydon/tutorials/BAinPy/10_multiple_regression.html
"""
import pandas as pd
from pandas import DataFrame
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant


def cell_05() -> None:
    """
    The multi-linear model uses two sample points per participant. To obtain these input data,
    we first load the restify csv and split the info of every participant into two sampling points.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # This is a group based comparison, we exclude the scammer.
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)

    # reduce samples down to one application (this way we eliminate the repeated measures,
    # and there is no need to have a participant dimension in the model)
    for app in ['xox', 'bs']:

        print("APP: "+app)

        # Split mangled participant sampling points into one sample point per row (actually contains
        # time AND pass-rate per row, but every experiment run is a row instead of restify.csv every
        # participant representing a row.)
        multi_linear_samples: DataFrame = extract_multi_linear_samples(assessed_population, app)

        # Run linear regression analysis for both: time and pass_rate impact.
        for response_name in ['time', 'pass_rate']:
            run_ols_linear_regression(response_name, multi_linear_samples)

        # Create visual codependency matrix for explanatory variables
        sns.pairplot(multi_linear_samples)
        plt.savefig("generated-plots/10-explanatory-correlation.png", dpi=300)
        plt.show()
        print("done")


def run_ols_linear_regression(response_name: str, multi_linear_samples: DataFrame):
    # explanation: https://www.geeksforgeeks.org/interpreting-the-results-of-linear-regression
    # -using-ols-summary/
    print("==============================================================================")
    print("==============================================================================")
    print("==============================================================================")
    print("Linear Regression for \"" + response_name + "\"")

    # Prepare variables and complete matrix
    response_variable = multi_linear_samples[response_name]
    explanatory_variables = multi_linear_samples[['period', 'technique']]
    explanatory_variables = sm.add_constant(explanatory_variables)

    # Run the linear regression
    ks = sm.OLS(response_variable, explanatory_variables)
    ks_res = ks.fit()
    print(ks_res.summary())


def categorical_to_numerical(participant: AssessedParticipant, first: bool) -> dict:
    """
    Helper function to convert participant information into an array of numeric values.
    This targets factors that determine
    :param participant: as the participant raw (including categorical values) to process.
    :param first: flag to indicate if first or second sample for this participant must be extracted.
    :return: dictionary with dependent variables (time, pass-rate) and dummy-converted
    categorical values (methodology, period, app)
    """
    if first:
        period: int = 0
        pass_rate: float = participant.test_percentage_first
        time: float = participant.time_first
        app_bookstore: int = 1 if participant.app_first == "bs" else 0
        meth_dsl: int = 1 if participant.meth_first == "tc" else 0
    else:
        period: int = 1
        pass_rate: float = participant.test_percentage_first if first else \
            participant.test_percentage_second
        time: float = participant.time_first if first else participant.time_second
        app_bookstore: int = 1 if participant.app_second == "bs" else 0
        meth_dsl: int = 1 if participant.meth_second == "tc" else 0

    return {'time': time, 'pass_rate': pass_rate, 'period': period, 'app_bookstore': app_bookstore,
            'technique': meth_dsl}


def filter_to_xox(item):
    """
    Helper function to tell for each sample if the app matches a provided string.
    :param app:
    :return:
    """
    if item['app_bookstore'] == 1:
        return False  # filter pair out of the dictionary
    else:
        return True  # keep pair in the filtered dictionary

def filter_to_bs(item):
    """
    Helper function to tell for each sample if the app matches a provided string.
    :param app:
    :return:
    """
    if item['app_bookstore'] == 0:
        return False  # filter pair out of the dictionary
    else:
        return True  # keep pair in the filtered dictionary


def extract_multi_linear_samples(assessed_population: list[AssessedParticipant], app: str) -> DataFrame:
    """
    Existing restify CSV has sampling points for repeated measures interleaved per table
    entry. This helper function splits the mangled data into one sampling point per table entry,
    and converts categorical variables to numeric (dummy) variables.
    :param assessed_population: as all participant data as extracted from the restify csv file.
    :return: Pandas dataframe with one experiment measure (sample) per row.
    """
    # list of dictionaries.
    multi_linear_samples: list = []

    # # For every participant, extract both experiment samples (one per period)
    for participant in assessed_population:
        multi_linear_samples.append(categorical_to_numerical(participant, True))
        multi_linear_samples.append(categorical_to_numerical(participant, False))

    # filter down to only those with matching application
    if app == 'xox':
        filtered_linear_samples: list = list(filter(filter_to_xox, multi_linear_samples))
    else:
        filtered_linear_samples: list = list(filter(filter_to_bs, multi_linear_samples))

    # remove app info
    for item in filtered_linear_samples:
        item.pop('app_bookstore')

    # convert to pandas dataframe and return
    multi_linear_samples_dataframe: DataFrame = pd.DataFrame.from_records(filtered_linear_samples)
    return multi_linear_samples_dataframe