#!/bin/bash
#clear logs
rm logs/*

#run pylint on all python files
python3 -m pylint src/* > logs/pylint_src.log
python3 -m pylint test/* > logs/pylint_test.log