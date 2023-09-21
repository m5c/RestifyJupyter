"""
Pseudo Cell similar to previous cell. Computes pearson test (two tailed) to check for correlation
of pretime and skillsum. In contrast to the previous cell this one operates on basic metrics
"pass rate" and "conversion time".
Author: Maximilian Schiedermeier
"""
from scipy.stats import stats
from scipy.stats._stats_py import PearsonRResult

from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor
from restify_mining.scatter_plotters.extractors.summed_skill_extractor import SummedSkillExtractor


def cell_21() -> None:
    """
    Jupyter cell 21. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # Aggregated analysis, so we exclude outliers (scammer)
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)

    # PASS 1:
    # Run four tests per methodology:
    # Effect of pre-time on time, effect of pre-time on pass-rate, effect of skill-sum on time,
    # effect of skill-sum on pass-rate
    for methodology in ["tc", "ide"]:
        # Run pearson test for liner correlation of values:
        # tradeoffs: list[float] = MethodologyTimeToPassRateTradeoffExtractor(methodology).extract(
        #     assessed_population)

        # Extract data needed for the person correlation tests
        # Explanatory variables:
        pre_times: list[int] = MethodologyPretimeExtractor(methodology).extract(assessed_population)
        skill_sum: list[int] = SummedSkillExtractor("PythonIsAwful").extract(assessed_population)
        # Dependent variables:
        pass_rates: list[float] = MethodologyPassrateExtractor(methodology).extract(
            assessed_population)
        times: list[int] = MethodologyTimeExtractor(methodology).extract(assessed_population)

        # Run the 4 pearson tests for the current methodology:
        # # Computed person correlation between values:
        # # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
        pre_time_to_time: PearsonRResult = stats.pearsonr(pre_times, times)
        pre_time_to_pass_rate: PearsonRResult = stats.pearsonr(pre_times, pass_rates)
        skill_sum_to_time: PearsonRResult = stats.pearsonr(skill_sum, times)
        skill_sum_to_pass_rate: PearsonRResult = stats.pearsonr(skill_sum, pass_rates)

        # Print results:
        print("Methodology: " + methodology)
        print("Pre-Time to Time: " + str(pre_time_to_time))
        print("Pre-Time to Pass-Rate: " + str(pre_time_to_pass_rate))
        print("Skill-Sum to Time: " + str(skill_sum_to_time))
        print("Skill-Sum to Pass-Rate: " + str(skill_sum_to_pass_rate))
        print(
            "Note: Linear correlation result (\"statistic\") is only significant if \"pvalue\" is "
            "smaller than 0.05")


