# a script to take in CSV data and to determine what is new data based on an older file
import pandas as pd
import csv

with open('winning_lottery_numbers.csv', newline='') as winning_numbers:
    reader = csv.DictReader(winning_numbers)
    for row in reader:
        print(row['Draw Date'])




