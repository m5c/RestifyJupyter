# RESTify Jupyter

Data, Data-Mining and visualization of correlations for the RESTify experiment.

TODO: Add Webpage for experiment description.

![pycharm](https://img.shields.io/badge/PyCharm-22.2.1-blue)
![pylint](https://img.shields.io/badge/PyLint-2.15.2-blue)
![jupyter](https://img.shields.io/badge/Jupyter%20Notebook-6.4.12-blue)

## About

This repository hosts the sources and input data for the RESTify experiment analysis, in form of a Jupyter Notebook
instance.

## Contents

TODO: Rather than copying complex cells to jupyter, create proxy cells that call actual code (too complex for jupyter)

The Data Mining Cells (DMCs) are to complex Jupyter. Therefore, they were developed in PyCharm and afterwards transferred to Jupyter cells.
Every DMC matches exactly the content and launch configuration of one file in ```jupyter_snippets```:

| DMC | File | PyCharm Launch Config | Output |
|--|---|---|---|
| 1 | [```display_population_gaussian.py```](jupyter_snippets/display_population_gaussian.py) | DisplayPopulationGaussian | ```generated-plots/gaussians.png``` |
| 2 | [```display_control_group_skill_boxplot.py```](jupyter_snippets/display_control_group_skill_boxplot.py) | DisplayControlGroupSkillBoxPlot | ```generated-plots/fused-stats.png``` |
| 3 | [```compute_group_skill_diffs.py```](jupyter_snippets/compute_group_skill_diffs.py) | ComputeGroupSkillDiffs | ```--printed--``` |
| 4 | [```merge_csv.py```](jupyter_snippets/merge_csv.py) | MergeCsv | ```generated-csv-files/restify.csv``` |
| 5 | [```display_test_results_all_participants_by_method.py```](jupyter_snippets/display_test_results_all_participants_by_method.py) | DisplayParticipantTestResultsByMethod | ```TODO: Store to file``` |
| 6 | [```display_test_results_all_groups_by_method.py```](jupyter_snippets/pseudo_cell_all_tests_all_groups.py) | DisplayGroupTestResultsByMethod | ```TODO: Store to file``` |



* The Jupyter files are sprinkled at top level, the main one being: ```restify.ipynb```
    * The snippets listed in the notebook are too complex to be developed in jupyter. They are thus copies of the files
      in ```jupyter_snippets```. Those can be conveniently launched with PyCharm.
    * Additional python files used for the actual mining are in ```restify_mining```.
* Raw input data collected in the experiment is in ```source-csv-files```.
* Plots are stored to ```generated-plots```.

### Raw CSV Data

The contents of ```source-csv-files``` are as follows:

* Task order definition: ```source-csv-files/tasks.csv```
* Unit test statistics CSV: ```source-csv-files/teststats.csv```
* Skill vectors per codename (colours define partition) CSV: ```source-csv-files/patitionskills.csv```
* Post completion ratings CSV: ```TBA```
* Manually extracted time data CSV: ```TBA```

## Usage

For data analysis, use Jupyter. For development of new snippets, use pycharm and place your new snipped in
the ```jupyter_snippets``` directory. Copy the content of your snipped into a new jupyter cell when done.

 * Starting the Notebook: ```jupyter notebook```
 * Visit: [http://localhost:8888/notebooks/Restify.ipynb](http://localhost:8888/notebooks/Restify.ipynb)

### Pycharm Setup

 * Install [PyLint]
 * Configure PyLint to use the root ```.pylintrc``` config file, so it correclty resolves imports.  
(See [this discussion](https://github.com/dense-analysis/ale/issues/208#issuecomment-265590465))
 * Use provided Run configurations to dry run Jupyter cells (working directory preconfigured, so there are no IO issued on CSV import / graph export)

## Author / References

* PI: Maximilian Schiedermeier
* Supervisors: Bettina Kemme, Jörg Kienzle
* Raw Data: ...csv bundle...
* Implementation: Maximilian Schiedermeier
    * Study Instructions, by control group: 
       * [Red](https://www.cs.mcgill.ca/~mschie3/red/restify-study/)
       * [Green](https://www.cs.mcgill.ca/~mschie3/green/restify-study/)
       * [Blue](https://www.cs.mcgill.ca/~mschie3/blue/restify-study/)
       * [Yellow](https://www.cs.mcgill.ca/~mschie3/yellow/restify-study/)
    * Legacy Application Source Code:
       * [BookStore](https://github.com/kartoffelquadrat/BookStoreInternals/tree/RESTifyStudy)
       * [Zoo](https://github.com/kartoffelquadrat/Zoo/tree/RESTifyStudy)
       * [Xox](https://github.com/kartoffelquadrat/XoxInternals/tree/RESTifyStudy)
    * Unit Test Evaluation Script: [RestifyAnalyzer](https://github.com/kartoffelquadrat/RestifyAnalyzer)
* Research Ethics Board Advisor: Lynda McNeil
