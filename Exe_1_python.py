# Topic : BASIC PYTHON
# Exercise Number : 3
# PROBLEM STATEMENT:
#    Write a Python program to display the current date and time.

# Python Version : 3.7

import datetime
CURRENT_TIME = datetime.datetime.now()
x=CURRENT_TIME.strftime("%d-%m-%Y %H:%M:%S")
print("Current date and time : ", x)
