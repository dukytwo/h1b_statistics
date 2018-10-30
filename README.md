# Table of Contents
1. [Problem](README.md#Problem)
2. [Approach](README.md#Approach)
3. [Run instructions](README.md#Run instructions)

# Problem


A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, I am asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

The code is also modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script will produce the results in the `output` folder without needing to change the code.

# Approach

1. Read data header, if the file is the old H1B_FY_2014.csv, modify its column names to becompatible with the newer ones, whose column names seem consistent
2. Find the indicies of required fields: 'CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'
3. Read file line by line, use rows having 'CERTIFIED' in 'CASE_STATUS' column and then aggregate counts for each group of 'SOC_NAME', 'WORKSITE_STATE'seperately.From this step, 'SOC_NAME', 'WORKSITE_STATE' data will be handled seperately.
4. Calculate total number of counts for all group, calculate count percentage for each group, and then add the percentage to dict element to make a list of {group, [count, percentage string]}.
5. Sort by count (reverse) and then by group name incase two groups have the same name.
6. Write to output csv with header and then data

# Run instructions
Download H1B data from [Office of Foreign Labor Certification Performance Data]data Put  in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.
