# RESTify Data Analysis

Data, Data-Mining and Visualization for the RESTify experiment.

![pycharm](https://img.shields.io/badge/PyCharm-22.2.1-blue)
![pylint](https://img.shields.io/badge/PyLint-2.15.2-blue)
![jupyter](https://img.shields.io/badge/Jupyter%20Notebook-6.4.12-blue)
![docker](https://img.shields.io/badge/Docker%20Docker-20.10.17-blue)

## About

This repository hosts sources and raw input data that allows replication of empiric findings around the RESTify
experiment.
The data can be reproduced and inspected with a Jupyter Notebook instance, or for more experienced users and
collaborators with a preconfigured PyCharm project.

To replicate our data analysis, you have four options:

* [Inspect the rendered preview on GitHub, using only your browser](Restify.ipynb)  
  => You will see all figures of this paper, pre-rendered. However, you will not be able to modify the notebook
  execution content, and some document-internal section links will not work.
* [Deploy a local Jupyter Notebook as preconfigured Docker container.](#dockerized-notebook)  
  => *The fastest and simples way to inspect our work and findings.*
* [Manually set up a local Jupyter Notebook.](#manual-notebook)  
  => *Similar to the previous option. The manual setup requires proficiency with python installations.*
* [Manually run individual parts of the data analysis with the PyCharm IDE](#pycharm-ide):  
  => *Full access to all implementation details. The preferred option for software developers and data scientists who
  want to deeply investigate our work, or take things further.*

## Produced Analyses

The notebook runs 19 execution cells, which each correspond to one python file. You can replicate individual results or
use the ```run_all_pseudo_cells.py``` script, to replicate the entire statistical analysis in a single run.

| Cell | Filename                                                                                                                                                                                  | Description                                                                                                                                                                                                              |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01   | [```pseudo_cell_01_display_population_skill_stats.py```](jupyter_snippets/pseudo_cell_01_display_population_skill_stats.py)                                                               | Creates a series of barcharts for skill distribution of all participants and all skills.                                                                                                                                 |
| 02   | [```pseudo_cell_02_display_cgroups_skill_boxplot.py```](jupyter_snippets/pseudo_cell_02_display_cgroups_skill_boxplot.py)                                                                 | Creates a boxplot for skill distributions of all skills across the experiment group partition.                                                                                                                           |
| 03   | [```pseudo_cell_03_merge_csvs.py```](jupyter_snippets/pseudo_cell_03_merge_csvs.py)                                                                                                       | Helper tool to create a fused CSV file with combined data.                                                                                                                                                               |
| 04   | [```pseudo_cell_04_compute_cgroup_skill_diffs.py```](jupyter_snippets/pseudo_cell_04_compute_cgroup_skill_diffs.py)                                                                       | Computes effectiveness of MiniMax heuristic for balanced groups by testing all pairs of groups for distance in average skill level and prints the results.                                                               |
| 05   | [```pseudo_cell_05_all_results_all_participants.py```](jupyter_snippets/pseudo_cell_06_all_results_all_participants.py)                                                                   | Displays two 2D grids with all participant test results.                                                                                                                                                                 |
| 06   | [```pseudo_cell_06_all_results_all_groups_radar.py```](jupyter_snippets/pseudo_cell_07_all_results_all_groups_radar.py)                                                                   | Displays the group average test scores for all individual tests as Radar Chart.                                                                                                                                          |
| 07   | [```pseudo_cell_07_all_tests_all_groups.py```](jupyter_snippets/pseudo_cell_08_all_tests_all_groups.py)                                                                                   | 2D grids similar to cell 05, but bundles the test results by group and therefore displays group performance as a HeatMap.                                                                                                |
| 08   | [```pseudo_cell_08_time_passrate_normal_test.py```](jupyter_snippets/pseudo_cell_09_time_passrate_normal_test.py)                                                                         | Runs a Shapiro Wilk test on on effectiveness distributions of refactoring (weighted sum of normalized time and correctness).                                                                                             |
| 09   | [```pseudo_cell_09_time_boxplot.py```](jupyter_snippets/pseudo_cell_10_time_and_passrate_boxplot.py)                                                                                                   | Displays conversion time distributions for both refactoring tasks per groups as single boxplot.                                                                                                                          |
| 10   | [```pseudo_cell_10_pretime_time_scatter.py```](jupyter_snippets/pseudo_cell_12_pretime_time_scatter.py)                                                                                   | Produces a scatter plot series putting into relation participant time spent on task familiarization to time spent on the actual task solving.                                                                            |
| 11   | [```pseudo_cell_11_time_passrate_scatter.py```](jupyter_snippets/pseudo_cell_13_time_passrate_scatter.py)                                                                                 | Produces a scatter series putting into relation time spent on task solving to correctness of the outcome.                                                                                                                |
| 12   | [```pseudo_cell_12_pretime_passrate_scatter.py```](jupyter_snippets/pseudo_cell_14_pretime_passrate_scatter.py)                                                                           | Produces a scatter series putting into relation time spent on task familiarization to correctness of the outcome.                                                                                                        |
| 13   | [```pseudo_cell_13_skill_passrate_scatter.py```](jupyter_snippets/pseudo_cell_15_skill_passrate_scatter.py)                                                                               | Produces a scatter plot series putting into skill level of all participants and all skills to the correctness of the outcome.                                                                                            |
| 14   | [```pseudo_cell_14_skillsum_passrate_scatter.py```](jupyter_snippets/pseudo_cell_16_skillsum_passrate_scatter.py)                                                                         | Similar to previous skill, but only uses the participants skill sum instead of all there individual skills.                                                                                                              |
| 15   | [```pseudo_cell_15_qualitytradeoff_by_app.py```](jupyter_snippets/pseudo_cell_17_qualitytradeoff_by_app.py)                                                                               | Produces Normal Distributions (see test in cell 08) for weighted conversion effectiveness all participants with same application and methodology.                                                                        |
| 16   | [```pseudo_cell_16_fail_cause_stage_1.py```](jupyter_snippets/pseudo_cell_18_fail_cause_stage_1.py)                                                                                       | Creates a pie chart of the most common errors observed in submissions, at stage one. That is to say lists where files were missing, where pom edits were needed, where submissions did not compile.                      |
| 17   | [```pseudo_cell_17_skill_quality_by_methodology_scatter_pearson.py```](jupyter_snippets/pseudo_cell_19_skill_quality_by_methodology_scatter_pearson.py)                                   | Produces a scatter plot series putting into relation preliminary participant skill (one scatter per skill) and quality of the outcome. Also runs a two sided pearson test for linear correlation and prints the outcome. |
| 18   | [```pseudo_cell_18_pretime_quality_by_methodology_scatter_pearson.py```](jupyter_snippets/pseudo_cell_20_pretime_quality_by_methodology_scatter_pearson.py)                               | Produces a scatter plot series putting into relation time spent on task familiarization and quality of the outcome. Also runs a two sided pearson test for linear correlation and prints the outcome.                    |
| 19   | [```pseudo_cell_19_participant_feedback.py```](jupyter_snippets/pseudo_cell_21_participant_feedback.py)                                                                                   | Produces a barchart on the participant feedback as extracted from the submitted forms.                                                                                                                                   |

## Dockerized Notebook

This repository hosts a Docker configuration that creates a container Jupyter Notebook instance with all runtime
dependencies.    
The notebook allows you to locally replicate our methodology and all findings, together with in-depth explanations.

Instructions for Docker:

1. [Install Docker](https://docs.docker.com/get-docker/)
2. Clone this repository:  
   ```git clone https://github.com/m5c/RestifyJupyter.git```
3. Build and Run the Jupyter Notebook Container:  
   ```cd RestifyJupyter; ./docker-autostart.sh```
4. Access the Notebook: [http://127.0.0.1:8888/notebooks/Restify.ipynb](http://127.0.0.1:8888/notebooks/Restify.ipynb)

## Manual Notebook

This section explains how to run the Jupyter Notebook instance natively. For this to work, all runtime dependencies must
be first installed manually.

1. Install ```Python 3.9``` or newer. Make sure the installed python interpreter is selected in the PyCharm run
   configurations.
2. Install all required python libraries, e.g. using the ```pip3``` package manager:  
   ```pip3 install pandas numpy matplotlib plotly scipy jupyter```  
   You can also use the provided [```requirements.txt```](requirements.txt) for this.
3. Start up the Notebook:
    * Go to the project base directory: ```cd RestifyJupyter```
    * Start the Notebook: ```jupyter notebook```
    * Access the
      Notebook: [http://localhost:8888/notebooks/Restify.ipynb](http://localhost:8888/notebooks/Restify.ipynb)

## PyCharm IDE

Complementary to the replication of our results with a Jupyter Notebook, you can also directly execute the python code
used for data mining.
This option provides an in depth access to implementation details and is intended for data scientist who want to either:

* Validate the correctness of our extracted data at coding level.
* Enrich our the data analysis we implemented by additional insights.

All runtime dependencies, including python itself, can be directly installed from PyCharm, however it is important that
the IDE is configured to use the correct interpreter.

1. Install PyCharm. The [free *Community Edition*](https://www.jetbrains.com/pycharm/download/) is sufficient.
2. Install the ```python3``` interpreter. You find a corresponding option in the ```PyCharm -> Settings``` menu:  
   ![interpreter](markdown/interpreter.png)
3. Install all required libraries. Open the ```PyCharm -> Settings -> Project -> Interpreter``` menu:
   ![libraries](markdown/libraries.png)
    * Click the ```+``` sign, then install all the following: ```pandas numpy matplot plotly scipy```
4. Install PyLint. Open the plugins menu: ```PyCharm -> Settings -> Plugins```:  
   ![pylint](markdown/pylint.png)
    * Configure PyLint to use the root ```.pylintrc``` config file, so
      it [correctly resolves imports](https://github.com/dense-analysis/ale/issues/208#issuecomment-265590465).
5. Select the desired run configuration, to replicate any of our results:
    * For every code cell of the Notebook, there is a corresponding preconfigured run configuration.
    * We recommend that you run the ```run_all_pseudo_cell.py``` script, which recreates all statistical figures and
      listings from the paper.

### Inputs and Outputs

* Inputs:  
  The Notebook works on the CSV data, stored in [```source-csv-files``](source-csv-files). It is the same data as
  provided in [our replication bundle](https://anonymous4doubleblinded.github.io/ExperimentReplicationPackage).
* Outputs:
    * Figures are generated to ```generated-plots```
    * Intermediate CSV files are generated to ```generated-csv-files```

## Implementation Details

This section is only relevant for data analysts who want to tweak the notebook output / visualization.

### Label Makers

For scatter plots and scatter series you can easily change how samples are annotated. Just pass a different `LabelMaker`
at the moment of scatter instantiation.  
`LabelMakers` are defined in [`restify_mining/scatter_plotters/extractors`](restify_mining/scatter_plotters/extractors).

If you with to annotated only selected dots, edit the `labeloverride.csv` and use a custom `LabelMaker`.
* To remove all labels, use the `EmptyLabelMaker`.
* To annotate full codenames (colour + animal) use the `FullLabelMaker`.
* To annotate group internal codenames (only animal), use `AnimalLabelMaker`.

## Author / References

* Principal Investigator: [Maximilian Schiedermeier](https://www.cs.mcgill.ca/~mschie3/)
* Academic Supervisors: [Bettina Kemme](https://www.cs.mcgill.ca/~kemme/)
  , [Jorg Kienzle](https://www.cs.mcgill.ca/~joerg/Home/Jorgs_Home.html)
* Implementation: [Maximilian Schiedermeier](https://github.com/m5c)
    * Study Instructions, by control group:
        * [Red](https://www.cs.mcgill.ca/~mschie3/red/restify-study/)
        * [Green](https://www.cs.mcgill.ca/~mschie3/green/restify-study/)
        * [Blue](https://www.cs.mcgill.ca/~mschie3/blue/restify-study/)
        * [Yellow](https://www.cs.mcgill.ca/~mschie3/yellow/restify-study/)
    * Legacy Application Source Code:
        * [BookStore](https://github.com/m5c/BookStoreInternals/tree/RESTifyStudy)
        * [Zoo](https://github.com/m5c/Zoo/tree/RESTifyStudy)
        * [Xox](https://github.com/m5c/XoxInternals/tree/RESTifyStudy)
    * Participant Submission Analyzer: [RestifyAnalyzer](https://github.com/m5c/RestifyAnalyzer)
* Research Ethics Board Advisor: Lynda McNeil
