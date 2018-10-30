# Table of Contents
1. [Problem](README.md#Problem)
2. [Approach](README.md#Approach)
3. [Run instructions](README.md#Run instructions)

# Problem

This script is used to analyze and identify the occupations and states with the most number of approved H1B visas using [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).  It will identify the **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

The code has been tested on data from 2014 to 2018. The code is also modular and reusable for future use as long as the necessary data to calculate the metrics are available, which is 'CASE_STATUS', 'SOC_NAME', and 'WORKSITE_STATE'

# Approach

1. Read data header, if the file is the old H1B_FY_2014.csv, modify its column names to becompatible with the newer ones, whose column names seem consistent
2. Find the indicies of required fields: 'CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'
3. Read file line by line, use rows having 'CERTIFIED' in 'CASE_STATUS' column and then aggregate counts for each group of 'SOC_NAME', 'WORKSITE_STATE'seperately.From this step, 'SOC_NAME', 'WORKSITE_STATE' data will be handled seperately.
4. Calculate total number of counts for all group, calculate count percentage for each group, and then add the percentage to dict element to make a list of {group, [count, percentage string]}.
5. Sort by count (reverse) and then by group name incase two groups have the same name.
6. Write to output csv with header and then data

# Run instructions
Download H1B data from [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis) and then put it in the input directory, run the run.sh script, wait untill 'Saved to file' message shown, find output file under output folder.
