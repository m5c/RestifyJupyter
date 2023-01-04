# RESTify Data Analysis

Data, Data-Mining and Visualization for the RESTify experiment.

![pycharm](https://img.shields.io/badge/PyCharm-22.2.1-blue)
![pylint](https://img.shields.io/badge/PyLint-2.15.2-blue)
![jupyter](https://img.shields.io/badge/Jupyter%20Notebook-6.4.12-blue)
![docker](https://img.shields.io/badge/Docker%20Docker-20.10.17-blue)

## About

This repository hosts sources and raw input data that allows replication of empiric findings around the RESTify experiment.
The data can be reproduced and inspected with a Jupyter Notebook instance, or for more experienced users and collaborators with a preconfigured PyCharm project.

To replicate our data analysis, you have three options:

 * [Deploy a local Jupyter Notebook as preconfigured Docker container.](#dockerized-notebook)  
=> *The fastest and simples way to inspect our work and findings.*
 * [Manually set up a local Jupyter Notebook.](#manual-notebook)  
=> *Similar to the previous option. The manual setup requires proficiency with python installations.*
 * [Manually run individual parts of the data analysis with the PyCharm IDE](#pycharm-ide):  
=> *Full access to all implementation details. The preferred option for software developers and data scientists who want to deep investigate our work, or take things further.*

 > For an overlook of the repository structure, see the [Contents](#contents) section.

## Dockerized Notebook

This repository hosts a Docker configuration that creates a container Jupyter Notebook instance with all runtime dependencies.    
The notebook allows you to locally replicate our methodology and all findings, together with in-depth explanations.

Instructions for Docker:

1. [Install Docker](https://docs.docker.com/get-docker/)
2. Clone this repository:  
```git clone https://github.com/m5c/RestifyJupyter.git```
3. Build and Run the Jupyter Notebook Container:  
```cd RestifyJupyter; ./docker-autostart.sh```
4. Access the Notebook: [http://127.0.0.1:8888/notebooks/Restify.ipynb](http://127.0.0.1:8888/notebooks/Restify.ipynb)

## Manual Notebook

This section explains how to run the Jupyter Notebook instance natively. For this to work, all runtime dependencies must be first installed manually.  

 1. Install ```Python 3.7``` or newer.
 2. Install all required python libraries, e.g. using the ```pip3``` package manager:  
```pip3 install pandas numpy matplotlib plotly scipy jupyter```
 3. Start up the Notebook:
    * Go to the project base directory: ```cd RestifyJupyter```
    * Start the Notebook: ```jupyter notebook```
    * Access the Notebook: [http://localhost:8888/notebooks/Restify.ipynb](http://localhost:8888/notebooks/Restify.ipynb)

## PyCharm IDE

Complementary to the replication of our results with a Jupyter Notebook, you can also directly execute the python code used for data mining.
This option provides an in depth access to implementation details and is intended for data scientist who want to either:

 * Validate the correctness of our extracted data at coding level.
 * Enrich our the data analysis we implemented by additional insights.

All runtime dependencies, including python itself, can be directly installed from PyCharm, however it is important that the IDE is configured to use the correct interpreter.

 1. Install PyCharm. The [free *Community Edition*](https://www.jetbrains.com/pycharm/download/) is sufficient.
 2. Install the ```python3``` interpreter. You find a corresponding option in the ```PyCharm -> Settings``` menu:  
![interpreter](markdown/interpreter.png)
 3. Install all required libraries. Open the ```PyCharm -> Settings -> Project -> Interpreter``` menu:
![libraries](markdown/libraries.png)
    * Click the ```+``` sign, then install all the following: ```pandas numpy matplot plotly scipy```
 4. Install PyLint. Open the plugins menu: ```PyCharm -> Settings -> Plugins```:  
![pylint](markdown/pylint.png)
    * Configure PyLint to use the root ```.pylintrc``` config file, so it [correctly resolves imports](https://github.com/dense-analysis/ale/issues/208#issuecomment-265590465).
 5. Select the desired run configuration, to replicate any of our results:
    * For every code cell of the Notebook, there is a corresponding preconfigured run configuration.

### Run Configurations

The Data Mining used for the purpose of this project is too complex for Jupyter Notebook cells. The Notebook is still useful to explain the individual and detailed analysis performed and replicate the extracted data on your system. Yet the python cells are merely proxy calls to the actual data analysis performed in this python repository. In the following we also refer to the code cells that showcase in the Jupyter Notebook as *Data Mining Cells*, short DMC.
When opened with PyCharm, this project is preconfigured to offer all DMCs as convenient run configurations

Every DMC matches exactly the content and launch configuration of one file in ```jupyter_snippets```:

| DMC | File | PyCharm Launch Config | Output in ```generated-plots```|
|-----|---|---|---|
| 00  | ... | ... | ... |
| 01  | [```display_population_gaussian.py```](restify_mining/skill_extractors/extract_population_gaussian.py) | DisplayPopulationGaussian | ```generated-plots/gaussians.png``` |
| 02  | [```display_control_group_skill_boxplot.py```](restify_mining/skill_extractors/extract_control_group_boxplot.py) | DisplayControlGroupSkillBoxPlot | ```generated-plots/fused-stats.png``` |
| 03  | [```compute_group_skill_diffs.py```](restify_mining/skill_extractors/compute_cgroup_skill_diffs.py) | ComputeGroupSkillDiffs | ```--printed--``` |
| 04  | [```merge_csv.py```](restify_mining/skill_extractors/merge_csv.py) | MergeCsv | ```generated-csv-files/restify.csv``` |
| 05  | [```display_test_results_all_participants_by_method.py```](jupyter_snippets/pseudo_cell_05_all_results_all_participants.py) | DisplayParticipantTestResultsByMethod | ```05-test-individual.png``` |
| 06  | [```display_test_results_all_groups_by_method.py```](jupyter_snippets/pseudo_cell_06_all_tests_all_groups.py) | DisplayGroupTestResultsByMethod | ```06-test-heatmap.png``` |


## Repository Layout

... description of this section ...

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


## Author / References

* Principal Investigator: [Maximilian Schiedermeier](https://www.cs.mcgill.ca/~mschie3/)
* Academic Supervisors: [Bettina Kemme](https://www.cs.mcgill.ca/~kemme/), [Jörg Kienzle](https://www.cs.mcgill.ca/~joerg/Home/Jorgs_Home.html)
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
