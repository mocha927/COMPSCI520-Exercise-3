# COMPSCI520-Exercise-2

## Description

This repository contains the generated test code from Exercise-3 which I've included in the [code](./code/) directory.

*I used Github Copilot in VS-Code to generate specs and tests for this assignment*

Inside the code directory, there are the project directories for the llm-generated test-suites for the two selected functions. [./code/low_coverage_module](./code/low_coverage_module/) corresponds to the original test suite I used in exercise 2 and [./code/low_coverage_module_with_specs](./code/low_coverage_module_with_specs/) has the spec-guided test suite. HTML reports generated from pytest-cov are in [./code/low_coverage_module/htmlcov/](./code/low_coverage_module/htmlcov/) and [./code//low_coverage_module_with_specs/htmlcov/](./code//low_coverage_module_with_specs/htmlcov/) for each respective test suite.

## Installation

run ```pip install -r requirements.txt``` to install python packages

## How to Run

run ```pytest --cov low_coverage_code --cov-branch --cov-report html --cov-fail-under 0``` in [low_coverage_module](./code/low_coverage_module/) and [./code/low_coverage_module_with_specs](./code/low_coverage_module_with_specs/) respectively to generated HTML reports using pytest-cov