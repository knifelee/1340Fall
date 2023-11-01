#!/usr/bin/env python
# coding: utf-8

import os
from fileIO import * 
from utils import * 

# The user has the option to specify the file name they wish to analyze. 
# the program checks the file name until the input file name exists
# The input dataset is expected to consist of multiple lines, with each line containing two columns representing different variables.
while True:
    file_name = input("please input file path you would like to analyze: ")
    if os.path.exists(file_name):
        break
    else:
        print("Wrong file path!")
        print("Please check the path and file name.")
        print("")
     
# variable_X and variable_Y represent the first and second column in the input file
variable_X, variable_Y = dataset_read(file_name)
# data analyses results of variable_X and variable_Y
statistics = data_analyze(variable_X, variable_Y)
# display and log the results
analyses_report(statistics, file_name=file_name) 

