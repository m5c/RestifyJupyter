# RESTify Jupyter

Data and visualization of the RESTify experiment results.

## About

This repository hosts the sources and input data for the RESTify experiment analysis, in form of a Jupyter Notebook instance.

 > Set PYTHON workdir in pycharm to the repo basedir (won't find CSV files otherwise)

## Contents

### Data

 * Task order defintiion CSV
 * Unit test statistics CSV
 * Skill vectors CSV
 * Post completion ratings CSV
 * Manually extracted data CSV

### Sources

 * CSV merger
 * Jupyter files

## Usage

 * Make sure the unmnerged input CSV files are fully up to date
 * Run the CSV merger / Run the Jupyter notebook (not sure if auto merge should be invoked. I think so , since it makes sense to first display the individual data? Figure out.
    * Running the merger: ```./fusecsv.py``` (currently only fuses stats and task order)
    * Running the notebook: ```jupyter notebook```

## Author / References

 * PI: Maximilian Schiedermeier
 * Supervisors: Bettina Kemme, Jörg Kienzle
 * Raw Data: ...csv bundle...
 * Implementation: Maximilian Schiedermeier
    * Study Instructions: Red / Green / Blue / Yellow
    * Legacy Source Code: ...
    * Unit Test Evaluation Script: ...
 * Research Ethics Board Advisor: Lynda McNeil
