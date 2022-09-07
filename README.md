# RESTify Jupyter

Data and visualization of the RESTify experiment results.

## About

This repository hosts the sources and input data for the RESTify experiment analysis, in form of a Jupyter Notebook
instance.

## Contents

* The Jupyter files are sprinked at top level, the main one being: ```restify.ipynb```
    * The snippets listed in the notebook are too complex to be developed in jupyter. They are thus copies of the files
      in ```jupyter_snippets```. Those can be conveniently launched with PyCharm.
    * Additional python files used for the actual mining are in ```restify_mining```.
* Raw input data collected in the experiment is in ```source-csv-files```.
* Plots are stores to ```generated-plots```.

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
       * [BookStore](https://github.com/kartoffelquadrat/BookStoreInternals)
       * [Zoo](https://github.com/kartoffelquadrat/Zoo)
       * [Xox](https://github.com/kartoffelquadrat/XoxInternals)
    * Unit Test Evaluation Script: [RestifyAnalyzer](https://github.com/kartoffelquadrat/RestifyAnalyzer)
* Research Ethics Board Advisor: Lynda McNeil
