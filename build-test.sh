#!/bin/bash
#This script runs all the build and tes scripts for the project and stores the output in log files

#clear logs
rm logs/*

#run pylint on all python files
pylint src/* > logs/pylint_src.log
pylint test/* > logs/pylint_test.log

#rebuild documentation
cd docs
make clean > ../logs/docs_clean.log
make html > ../logs/docs_make_html.log
