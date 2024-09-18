# Experiment-3 : Python Data Analysis

# Objectives: 

To identify the codes and functions incorporated in the Pandas library

To be able to apply and use the different codes and functions in creating a Python program using a Pandas library


# PROBLEM 1 

# Task 
> Load the corresponding .csv file

> Display the first and last 5 rows of the dataframe

# Expected Behavior: 
> The script should correctly load the CSV file from the provided URL into a DataFrame named cars.

> The first five rows of the dataset should be displayed, showing the initial entries.

> The last five rows of the dataset should also be displayed, revealing the final entries in the dataset.

#start of code

import pandas as pd

#Loading the CSV file into a dataframe named cars

url = "http://bit.ly/Cars_file"
cars = pd.read_csv(url)

#Displaying the first five and last five rows of the dataframe

print("First 5 rows: ")
print(cars.head())

print("\nLast 6 rows: ")
print(cars.tail())

# PROBLEM 2

# Task : 

> Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...).

> Display the row that contains the 'Model' of 'Mazda RX4'.

> How many cylinders ('cyl') does the car model 'Camaro Z28' have?

> Determine how many cylinders ('cyl') and what gear type ('gear') do the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.

# Expected Behavior: 

> It should correctly display the first five rows of the cars DataFrame, but only the odd-numbered columns (e.g., columns 1, 3, 5, 7...).

> It should return the entire row where the 'Model' is 'Mazda RX4', showing all associated data for this model.

> It should accurately return the number of cylinders ('cyl') for the car model 'Camaro Z28'.

> It should also display the number of cylinders ('cyl') and gear type ('gear') for the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.

#start of code

###Part A

#Display the first five rows with Odd-Numbered columns of cars

#Use iloc function to find and print out specific rows/columns and utilize the slicing function

print(cars.iloc[:5, ::2])

###Part B

#Display the row which contains the Model of Mazda RX4

#Use loc function to specific and pick the row that contains 'Mazda RX4' in the 'Model' column

mazda = cars.loc[cars['Model'] == 'Mazda RX4']
mazda

###Part C

#How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

#Use loc function to find the value at that specific row index and column name
cars.loc[23,'cyl']

###Part D

#Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

#Use loc function to determine specific value 

cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
