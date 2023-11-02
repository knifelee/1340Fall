# INF1340 - Mid-term Project
This a repo for display mid-term assignment for INF1340

The project is a Python-based statistical analysis and reporting tool that provides a set of functions for analyzing datasets and generating detailed reports. The tool encompasses a variety of statistical calculations, including analyzing and calculating statistics for single numerical variable, such as calculating means, variances, as well as statistics for two varibles such as covariances, correlations, and conducting t-tests (totally 14 distinct tasks). The project also includes functionality to read data from an input file and generate a report containing analysis results. The project is designed to help users gain insights into their data and make informed decisions based on statistical evidence.

## Key Components:
* Descriptive Statistics: The tool includes functions to compute basic descriptive statistics for a list of numeric values. This includes calculations for the summation, average, standard deviation, variance, minimum, and maximum values.
* Histogram and Mode: Users can generate a histogram to visualize the distribution of values in a dataset. The mode, which represents the most frequent value, can also be computed.
* Entropy and KL-Divergence: The tool provides functions to calculate the entropy of a population sampled from a dataset and the Kullback-Leibler (KL) divergence between two datasets. These metrics are useful for information theory and data analysis.
* Correlation Analysis: The project offers functions to compute both covariance and correlation between two lists of numeric values. This is valuable for assessing the relationship between two variables.
* Regression Analysis: Users can perform linear regression analysis on two variables. The tool computes the regression parameters, including the slope and intercept, and generates a regression model. It also calculates the R-squared value, which indicates the goodness of fit of the model.
* Hypothesis Testing (t-Test): The tool includes a t-test function to compare the means of two groups and determine whether the differences are statistically significant. Users can customize the critical value for hypothesis testing.
* Data Analysis and Reporting: The data_analyze function analyzes a dataset containing two variables and returns a dictionary with various statistics for each variable and their relationships. This includes single variable statistics and two-variable statistics such as covariance, correlation, KL-divergence, and more.
* File I/O and Reporting: The project can read datasets from input files, and users can specify the separator (e.g., comma, tab) between values. After analysis, the tool generates a detailed report in a text file, which includes all the calculated statistics.

This statistical analysis and reporting tool is valuable for data scientists, analysts, researchers, and anyone who needs to perform statistical analysis on their datasets. It helps in understanding data distributions, relationships, and making data-driven decisions. Future enhancements could include additional statistical tests, support for different file formats, and a user-friendly graphical interface.

## Modules
### 'util.py'
This module contains utility functions for various statistical calculations and data analysis. The functions include:
* **'calc_sum(alist)'**: Calculate the summation of a list of numeric values.
* **'calc_avg(alist)'**: Calculate the average value of a list of numeric values.
* **'calc_std(alist)'**: Calculate the standard deviation of a list of numeric values.
* **'calc_variance(alist)'**: Calculate the variance of a list of numeric values.
* **'calc_max(alist)'**: Find the maximum value in a list.
* **'calc_min(alist)'**: Find the minimum value in a list.
* **'calc_histogram(alist)'**: Calculate the frequency of values in a list.
* **'calc_mode(alist)'**: Find the mode(s) of a list.
* **'calc_entropy(alist)'**: Calculate the entropy of a list.
* **'calc_covariance(alist, blist)'**: Compute the covariance between two lists.
* **'calc_correlation(alist, blist)'**: Compute the correlation between two lists.
* **'calc_kld(alist, blist)'**: Calculate the Kullback-Leibler divergence between two lists.
* **'regression_analyses(alist, blist)'**: Perform regression analysis and compute the R-squared value for two lists.
* **'t_test(alist, blist)'**: Perform a t-test between two lists and determine the statistical significance.

### 'fileIO.py'
This module provides functions for reading data from an input file and generating a report file. The functions include:
* **'dataset_read(file_name, sep)'**: Read data from an input file and separate it into two lists.
* **'analyses_report(statistics, dec, file_name)'**: Generate a report containing the results of data analysis and display them. The report is saved in a file named "report.txt."


## Usage
To use this project, follow these steps:
1. Import the required modules:
```python
from util import *
from IO import *
```
2. Read your dataset from an input file using dataset_read(file_name, sep). Replace file_name with the path to your input file and specify the separator (e.g., ,, \t) if needed.
```python
variable_X, variable_Y = dataset_read("input.csv", sep=',')
```
3. Perform data analysis and calculations by calling the **'data_analyze(variable_X, variable_Y)'** function. This function returns a dictionary of analysis results. All the data analyses in **util.py**  will be automatically conducted.
```python
statistics = data_analyze(variable_X, variable_Y)
```
4. Generate a report containing the analysis results and display them using analyses_report(statistics, dec, file_name).
```python
analyses_report(statistics, file_name="input.csv")
```

## Example

Here's an example of how to use this project:

```python
from util import *
from IO import *

# Read data from an input file
variable_X, variable_Y = dataset_read("input.csv", sep=',')

# Perform data analysis
statistics = data_analyze(variable_X, variable_Y)

# Generate and display a report
analyses_report(statistics, file_name="input.csv")
```
The report will be saved as "report.txt" in the current working directory.

Users (my dear TAs) are also encouraged to use the given example dataset **Iris_petal.csv** and the driver code in **'main.py'** to test the code.
The example dataset are selected from a well-known AI benchmark -- Iris at "https://www.kaggle.com/datasets/uciml/iris". We used the columns 'PetalLengthCm' and 'PetalWidththCm'.

## Requirements
This project does not require any external packages. It uses only Python's standard libraries.

## License
This project is available under the MIT License.

## Author
Yuxin Gao (1010757986)

## Contact
If you have any questions or suggestions, feel free to contact yx.gao@mail.utoronto.ca
