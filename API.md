* API Documentation
This API documentation provides descriptions, input parameters, output results, and what each function will return for my project's utility functions and IO functions.
  
## `fileIO.py`
**dataset_read(file_name='input.csv', sep=',')**
* Description: Reads data from an input file in CSV format and returns two lists of numeric values representing two variables.

Input:

file_name (str): The name of the input file.
sep (str): The separator used in the CSV file (default is ,).
Output:

variable_X (list of float): List of values for the first variable.
variable_Y (list of float): List of values for the second variable.
analyses_report(statistics={}, dec=3, file_name='input.csv')
Description: Outputs the analysis results to a report file and displays them.

Input:

statistics (dict): A dictionary containing analysis results.
dec (int): The number of digits after the decimal point for float numbers (default is 3).
file_name (str): The name of the input file (default is 'input.csv').
Output: None (Generates a report file with analysis results).
