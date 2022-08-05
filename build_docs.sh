#!/bin/bash
#rebuild documentation
cd docs
make clean > ../logs/docs_clean.log
make html > ../logs/docs_make_html.log