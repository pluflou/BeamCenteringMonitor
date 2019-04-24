##BCM data analysis for SECAR
Packages needed:
numpy, matplotlib, pandas, datetime


![BCM Visual Example](examples/bcmcenter_2019-02-11_12:22:40.png)
#Retreiving the data

The method below gives us data that has been averaged of a specified time limit and the errors from the max and min during each time period have been calculated.

1. From the CSS file BCMarchives.plt, select the time range you want and then right-click and go to export.
2. Select the "linear interpolation" option and pick a time limit for the interpolation (5 seconds for example).
3. Select Tabular and check the errors option. Uncheck all else. Exponentials with precision 3 is fine.
4. Select path to where this code is (if running on same machine), name 'BCManalysis' and click Export.

#How to run

1. Unless the name of the data file is different, run the code immediately with 'python3 bcm_analysis.py'
2. Any changes in the CSS plot will likely cause an error while importing or cause to give you wrong information.


