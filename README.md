# Table of Contents
1. [Problem](README.md#Problem)
2. [Approach](README.md#Approach)
3. [Run Instructions](README.md#Run-Instructions)

# Problem

This python script is used to analyze and identify the occupations and states with the most approved H1B visas using [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).  It will identify the **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

The code has been tested on data from 2014 to 2018. The code is also modular and reusable for future use as long as the necessary data for calculating the metrics are available with column/field names of 'CASE_STATUS', 'SOC_NAME', and 'WORKSITE_STATE'.

# Approach

1. Use the python standard library "csv" to load the semicolon-delimited data file and iterate by rows. Command line arguments were taken by sys.argv of the "sys" module. 
2. Read data header and find the indicies of required fields named 'CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'. Note: After reading data header, the program checks the column names, and if the file is the old H1B_FY_2014.csv, the column names were modified to be compatible with the newer ones of later years, whose column names are consistent.
3. Read csv file line by line, use rows having 'CERTIFIED' in the 'CASE_STATUS' column and aggregate counts for each occupation ('SOC_NAME') and each state ('WORKSITE_STATE') seperately. A function was written to generate and return count dictionaries given any number of groups (e.g., occupation, state, and potential other variables) to analyze.
4. Calculate total counts for occupations and states, and accordingly calculate percentages for each occupation and state, and then add the percentages to dictionary elements to make a new dictionary as {group : [count, percentage string]}.
5. Sort by count (reversely) and then by group name if different occupation/state have same counts.
6. Write to csv using the sorted data.

# Run Instructions
Download H1B data from [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis) and convert the Excel files into semicolon-delimited csv. Place it in the "input" directory, run the "run.sh" script, the result of 2 files named "top_10..." will be written into the output folder with message 'Saved to file' shown.
