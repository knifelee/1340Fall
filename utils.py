# Author: Yuxin Gao
#!/usr/bin/env python
# coding: utf-8

import sys
from math import log2

# get the maximum and minimum values in your system
MAX_FLOAT = sys.float_info.max
MIN_FLOAT = sys.float_info.min

# the value to smooth the calculation of entropy and KL-divergence
SMOOTH_VALUE = 1e-9

# Input: a list of numeric values in alist
# output: the summation value of the list
def calc_sum(alist):
    s = 0
    for v in alist:
        s += v
        
    return s

# Input: a list of numeric values in alist
# output: the average value of the list
def calc_avg(alist):
    return calc_sum(alist) / len(alist)

# Input: a list of numeric values in alist
# output: the stardand deviation value of the list
def calc_std(alist):
    
    # the average of values is the mean of a list
    mean = calc_avg(alist)
    
    # compute the variance of a list
    var = 0
    for v in alist:
        var += (v - mean)**2
    var /= len(alist)
    
    # compute the std value
    sd = var**0.5
    
    return sd

# Input: a list of numeric values in alist
# Output: the variance of the list
# note that here we consider another notation of variance where the results should be divided by (n-1) where n is the length of the list.
def calc_variance(alist):
    sd = calc_std(alist)
    return sd**2 * len(alist) / (len(alist)-1)

# Input: a list of numeric values in alist
# output: the maximum value of the list
def calc_max(alist):
    max_value = MIN_FLOAT

    # iteratively visit all the values in alist
    for v in alist:
        if v > max_value:
            max_value = v

    return max_value

# Input: a list of numeric values in alist
# output: the minimum value of the list
def calc_min(alist):
    min_value = MAX_FLOAT

    # iteratively visit all the values in alist
    for v in alist:
        if v < min_value:
            min_value = v

    return min_value


# get the frequency of values in a list
def calc_histogram(alist):
    frequency_dict = {}

    # Count the frequency of each value
    for item in alist:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    return frequency_dict


# get one of the most frequent items in this list
def calc_mode(alist):

    # get the dictionary for the histogram of the list
    frequency_dict = calc_histogram(alist)

    # Find the number(s) with the highest frequency
    max_freq = calc_max(frequency_dict.values())
    mode = [number for number, freq in frequency_dict.items() if freq == max_freq]

    return mode[0]


# Input: a list of numeric values in alist
# Output: the entropy of this list's distribution
def calc_entropy(alist):
    variable = calc_histogram(alist)
    list_length = len(alist)

    entropy = 0
    for v in variable.values():
        probability = v / list_length
        entropy -= probability * log2(probability)

    return entropy


# compute covariance of two variables
# Input: two lists of numeric values in alist and blist
# Output: the covariance between the lists
def calc_covariance(alist, blist):

    # check if the input is valid
    if len(alist)!=len(blist):
        print("The given two lists have different lengths")
        return None
    
    # get the average values of the two lists
    avg_alist = calc_avg(alist)
    avg_blist = calc_avg(blist)

    # compute all the coefficiency of all the pairs of values in alist and blist
    cor_list = [(alist[i] - avg_alist) * (blist[i] - avg_blist) for i in range(len(alist))]
    return calc_sum(cor_list)/ (len(alist)-1)


# compute correlation of two variables
# Input: two lists of numeric values in alist and blist
# Output: the correlation between the lists
def calc_correlation(alist, blist):

    # check if the input is valid
    if len(alist)!=len(blist):
        print("The given two lists have different lengths")
        return None

    # Calculate the correlation coefficient
    coefficient = calc_covariance(alist, blist) / (calc_std(alist) * calc_std(blist)) / len(alist) * (len(alist)-1)
    return coefficient


# get the KL-divergence of two variables
def calc_kld(alist, blist):
    a_freq, b_freq = calc_histogram(alist), calc_histogram(blist)
    all_values = list(set(a_freq.keys()).union(set(b_freq.keys())))
    l1, l2 = len(alist), len(blist) # get the lengths of the two lists
    
    kl_divergence = 0
    for v in all_values:
        if v in a_freq and v in b_freq:
            kl_divergence += a_freq[v]/l1 * log2(a_freq[v] / b_freq[v] / l1 * l2)
        elif v in a_freq and v not in b_freq:
            kl_divergence += a_freq[v]/l1 * log2(a_freq[v] / SMOOTH_VALUE / l1 * l2)
        else:
            kl_divergence += SMOOTH_VALUE/l1 * log2(SMOOTH_VALUE / b_freq[v] / l1 * l2)
    
    return kl_divergence

# use regression analyses to see the relationship of two variables
def regression_analyses(alist, blist):
    mean_x, mean_y = calc_avg(alist), calc_avg(blist)
    variance_x = calc_variance(alist)
    covariance = calc_covariance(alist, blist)
    
    # compute parameter for the linear regression model
    slope = covariance / variance_x
    intercept = mean_y - slope * mean_x
    
    # compute the predicted value using the regression model
    predicted_y = [slope * x + intercept for x in alist]
    
    # compute the R square value
    total_sum_of_squares = calc_sum((y - mean_y) ** 2 for y in blist)
    residual_sum_of_squares = calc_sum((y - predicted_y) ** 2 for y, predicted_y in zip(blist, predicted_y))
    r_squared = 1 - (residual_sum_of_squares / total_sum_of_squares)

    return r_squared


""" 
A t-test is a type of statistical analysis used to compare the averages of two groups and 
determine whether the differences between them are more likely to arise from random chance.
"""
# get the t_test results of the two lists
# the t_critical value is set for a two-tailed test with alpha=0.05 for the given dataset in Iris_petal.csv
# users can lookup the critical value for a two-tailed test
def t_test(alist, blist, t_critical = 1.968):

    # Calculate the means of both samples
    avg_1, avg_2 = calc_avg(alist) / len(alist), calc_avg(blist) / len(blist)
    # Calculate the variances of both samples
    variance_1, variance_2 = calc_variance(alist), calc_variance(blist)

    # Calculate the pooled standard error
    pooled_standard_error = ((variance_1 / len(alist)) + (variance_1 / len(blist)) ** 0.5)

    # Calculate the t-statistic
    t_statistic = (avg_1 - avg_2) / pooled_standard_error

    # Calculate the degrees of freedom
    degree_freedom = len(alist) + len(blist) - 2

    # get the absolute value of t_statistic
    if t_statistic<0:
        t_statistic = -t_statistic

    # Determine if the t-statistic is significant 
    if t_statistic > t_critical:
        result = "Reject the null hypothesis"
    else:
        result = "Fail to reject the null hypothesis"

    return t_statistic, degree_freedom, result


# analyze the dataset and return the results as a dict
def data_analyze(variable_X, variable_Y):
    statistics = {}

    # single variable statistics
    statistics["variable_X minimum value"] = calc_min(variable_X)
    statistics["variable_Y minimum value"] = calc_min(variable_Y)
    statistics["variable_X maximum value"] = calc_max(variable_X)
    statistics["variable_Y maximum value"] = calc_max(variable_Y)
    statistics["variable_X mode value"] = calc_mode(variable_X)
    statistics["variable_Y mode value"] = calc_mode(variable_Y)
    statistics["variable_X summation"] = calc_sum(variable_X)
    statistics["variable_Y summation"] = calc_sum(variable_Y)
    statistics["variable_X average"] = calc_avg(variable_X)
    statistics["variable_Y average"] = calc_avg(variable_Y)
    statistics["variable_X standard Deviation"] = calc_std(variable_X)
    statistics["variable_Y standard Deviation"] = calc_std(variable_Y)
    statistics["variable_X variance"] = calc_variance(variable_X)
    statistics["variable_Y variance"] = calc_variance(variable_Y)
    statistics["variable_X entropy"] = calc_entropy(variable_X)
    statistics["variable_Y entropy"] = calc_entropy(variable_Y)
    
    # two variable statistics
    statistics["covariance"] = calc_covariance(variable_X, variable_Y)
    statistics["correlation"] = calc_correlation(variable_X, variable_Y)
    statistics["KL-divergence"] = calc_kld(variable_X, variable_Y)
    statistics["R square value (regression analysis)"] = regression_analyses(variable_X, variable_Y)
    statistics["t_statistic"], statistics['degree of freedom'], statistics['t-test result'] = t_test(variable_X, variable_Y)
    
    return statistics
