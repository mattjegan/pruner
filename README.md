# Pruner

[![PyPI version](https://badge.fury.io/py/pruner.svg)](https://badge.fury.io/py/pruner)
[![Build Status](https://travis-ci.org/mattjegan/pruner.svg?branch=master)](https://travis-ci.org/mattjegan/pruner)
[![Code Triagers Badge](https://www.codetriage.com/mattjegan/pruner/badges/users.svg)](https://www.codetriage.com/mattjegan/pruner)

Pruner is your best friend when it comes to pruning your Python requirements file.
Pruner will run over your requirements and test each one against your test command.
If your projects test command fails then we know the package needs to remain in the requirements
otherwise we prune it.

## Installation
```
pip install pruner
```

## Usage

```
usage: pruner.py [-h] [--nocolor] [--with_exit_code]
                 requirements_file output_file
                 [test_command [test_command ...]]

A CLI tool to help prune your overgrown requirements file

positional arguments:
  requirements_file  requirements file you want to prune
  output_file        file to store the required requirements
  test_command       command to run to test the project still works

optional arguments:
  -h, --help         show this help message and exit
  --nocolor          turns off colored output
  --with_exit_code   forces exit code to 1 if requirements needed pruning
```


## Example
```
> pruner requirements.txt pruned_requirements.txt python myproj.py

PRUNER: virtualenv prunertests
PRUNER: source prunertests/bin/activate
PRUNER: pip install -r requirements.txt
PRUNER: Running initial test...
PRUNER: Initial test was a success, beginning requirement tests...
PRUNER: Testing django
PRUNER: django was needed
PRUNER: Testing garbagepackage1
PRUNER: garbagepackage1 was not needed
PRUNER: Testing rancat
PRUNER: rancat was needed
PRUNER: Testing garbagepackage2
PRUNER: garbagepackage2 was not needed
PRUNER: Testing garbagepackage3
PRUNER: garbagepackage3 was not needed
PRUNER: deactivate
PRUNER: rm -rf prunertests
PRUNER: Writing results to pruned_requirements.txt
PRUNER: DONE

> cat requirements.txt
garbagepackage1
rancat
django
garbagepackage1
garbagepackage2

> cat pruned_requirements.txt
django
rancat

> cat myproj.py
import argparse
import sys
import django
import rancat
```

## Contributing

### Submitting an issue or feature request

If you find an issue or have a feature request please open an issue at [Github Pruner Repo](https://github.com/mattjegan/pruner).
