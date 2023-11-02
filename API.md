# API Documentation
This API documentation provides descriptions, input parameters, output results, and what each function will return for my project's utility functions and IO functions.
  
## `fileIO.py`
**dataset_read(file_name='input.csv', sep=',')**
* **Description**: Reads data from an input CSV file and returns two lists of numeric values representing two variables.
* **Input**:
  - **file_name**: (str) The name of the input file.
  - **sep**: (str) The separator used in the CSV file (default is ,).
* **Output**:
  - **variable_X** (list of float): List of values for the first variable.
  - **variable_Y** (list of float): List of values for the second variable.

**analyses_report(statistics={}, dec=3, file_name='input.csv')**
* **Description**: Outputs the analysis results to a report file and displays them.
* **Input**:
  - **statistics** (dict): A dictionary containing analysis results.
  - **dec** (int): The number of digits after the decimal point for float numbers (default is 3).
  - **file_name** (str): The name of the input file (default is 'input.csv').
* **Output**: None (Generates a report file with analysis results).
 
## `utils.py`
A set of utility functions for statistical analysis, including:
### 1. single variable statistics
**calc_mean(alist)**
* **Description**: Calculates the mean of a list of numeric values.
* **Input**:
  - **alist** (list): List of numeric values. 
* **Output**: Returns the mean (average) value.

**calc_std(alist)**
* **Description**: Calculates the standard deviation of a list of numeric values.
* **Input**:
  - **alist** (list): List of numeric values. 
* **Output**: Returns the standard deviation value.

**calc_variance(alist)**
* **Description**: Calculates the variance of a list of numeric values.
* **Input**:
  - **alist** (list): List of numeric values. 
* **Output**: Returns the variance value.

**calc_mode(alist)**
* **Description**: Calculates the mode (most frequent value) of a list of numeric values.
* **Input**:
  - **alist** (list): List of numeric values. 
* **Output**: Returns the mode value.

**calc_entropy(alist)**
* **Description**: Calculates the entropy of a list of numeric values.
* **Input**:
  - **alist** (list): List of numeric values. 
* **Output**: Returns the entropy value.

### 2. two-variable statistics
**calc_covariance(alist, blist)**
* **Description**: Calculates the covariance between two lists of numeric values.
* **Input**:
  - **alist** (list): List of values for the first variable.
  - **blist** (list): List of values for the second variable.
* **Output**: Returns the covariance value.

**calc_correlation(alist, blist)**
* **Description**: Calculates the correlation between two lists of numeric values.
* **Input**:
  - **alist** (list): List of values for the first variable.
  - **blist** (list): List of values for the second variable.
* **Output**: Returns the covariance value.

**calc_kld(alist, blist)**
* **Description**: Calculates the Kullback-Leibler Divergence (KL-divergence) between two lists of numeric values.
* **Input**:
  - **alist** (list): List of values for the first variable.
  - **blist** (list): List of values for the second variable.
* **Output**: Returns the KL-divergence value.

**t_test(alist, blist, t_critical=1.968)**
* **Description**: Performs a t-test for two lists of numeric values and returns the t-statistic, degrees of freedom, and the test result.
* **Input**:
  - **alist** (list): List of values for the first variable.
  - **blist** (list): List of values for the second variable.
  - **t_critical** (list): The critical t-value for significance (default is 1.968)
* **Output**: Returns the t-statistic, degrees of freedom, and the test result.

**regression_analyses(alist, blist)**
* **Description**: Performs a simple linear regression analysis and computes the R-squared value for two lists of numeric values.
* **Input**:
  - **alist** (list): List of values for the first variable.
  - **blist** (list): List of values for the second variable.
* **Output**: Returns the R-squared value for regression analyses.
