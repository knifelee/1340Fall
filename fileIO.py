# Author: Yuxin Gao
#!/usr/bin/env python
# coding: utf-8

import time
from datetime import datetime, date

# the functions to read data from an input file and output the data analyses results to a file.

# store the two variables from the input file into separate lists .
# the value of parameter sep can be something like '\t', ',', ' ', ';' 
def dataset_read(file_name='input.csv', sep=','):
    variable_X, variable_Y = [], [] # initialize the variable lists
    with open(file_name) as f:
        for line in f:
            numbers = line.rstrip('\n').strip().split(sep) # split the line into two numbers
            variable_X.append(float(numbers[0]))
            variable_Y.append(float(numbers[1]))
    
    print("Dataset Successfully Read!\n")
    return variable_X, variable_Y

# output the analyse result of input datasets into report.txt
# display the analyse meanwhile
# parameter 'dec' means how many digits after the decimal point
# parameter 'file_name' indicate the input dataset file name
def analyses_report(statistics={}, dec=3, file_name='input.csv'):
    with open("report.txt", 'w') as f:
        print("The analyses results of {}: \n".format(file_name))
        f.write("The analyses results of {}: \n\n".format(file_name))
        
        # iterate all the analyses results, output and display it
        for k, v in statistics.items():
            # formalize float numbers
            if type(v) == float:
                v = round(v, dec)
            f.write("{}: {}\n".format(k, v))
            print("{}: {}".format(k, v))
        
        # time stamp
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        print("\nReport Time: {} {}".format(today, current_time))
        f.write("\nReport Time: {} {}\n".format(today, current_time))
        