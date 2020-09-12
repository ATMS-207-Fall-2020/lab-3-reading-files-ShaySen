# reading files

This is Lab 3 for ATMS 207.

Your problems for this week (to be submitted to `github`):

*Problem 1*

Using the example code from the lecture

```python
filename='aravg.ann.land_ocean.90S.90N.v5.0.0.202007.asc'
wxdata={'year':[],'temperature':[]}    #define dictionary
with open(filename, "r") as f:    #read all the lines in the file
    alist = f.read().splitlines()
for line in alist:  #iterate through lines
    wxdata['year'].append(int(line.split()[0]))
    wxdata['temperature'].append(float(line.split()[1]))
```

Add code that will print a table of the top 10 warmest years in the first column and their temperature anomalies to the screen.

*Problem 2*

Using the data contained within the file `Aug2020_Champaign_Temperature_Dewpoint.csv`, write a python program to display the data for a given day on the screen.  The day can be specified within the program, for example

```python
date = '2020-08-01'
```

[![Run on Repl.it](https://repl.it/badge/github/swnesbitt/lab3-reading-files)](https://repl.it/github/swnesbitt/lab3-reading-files)
