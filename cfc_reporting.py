# Created by: Justin Baker
# First started in November 2023

# This script was developed to analyze jurisdiction data collected by the Code for the Carolinas organization
# with the intention of producing reporting statistics for the National Zoning Atlas team.

import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Get spreadsheet file path
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title='Please select a zoning jurisdiction information data file in .csv format.')

# Read spreadsheet into pandas
za_spreadsheet = pd.read_csv(file_path, encoding = "ISO-8859-1")

# ----------------- Number of jurisdictions --------------------

# Get total # of jurisdictions
totalNumJur = len(za_spreadsheet.index)
print('The total number of jurisdictions is ' + str(totalNumJur))

# Get number of jurisdictions with zoning
jurWithZoning = len(za_spreadsheet[za_spreadsheet['Does It Have Zoning?'] == 'Yes'])
print('The total number of jurisdictions with zoning is ' + str(jurWithZoning))

# Get number of jurisdictions without zoning
jurWithoutZoning = len(za_spreadsheet[za_spreadsheet['Does It Have Zoning?'] == 'No'])
print('The total number of jurisdictions without zoning is ' + str(jurWithoutZoning))

# Get number of jurisdictions with unknown zoning
jurWithUnkwnZoning = len(za_spreadsheet[za_spreadsheet['Does It Have Zoning?'].isnull()])
print(
    'The total number of jurisdictions with Unknown zoning is ' + str(jurWithUnkwnZoning))

# ----------------- Percentage of jurisdictions --------------------

# Get % of jurisdictions with zoning
percentWithZoning = (jurWithZoning / totalNumJur) * 100
print('The percentage of jurisdictions with zoning is ' + str(
        round(percentWithZoning, 2)) + '%')

# Get % of jurisdictions without zoning
percentWithoutZoning = (jurWithoutZoning / totalNumJur) * 100
print('The percentage of jurisdictions without zoning is ' + str(
        round(percentWithoutZoning, 2)) + '%')

# Get % of jurisdictions with unknown zoning
percentWithUnkwnZoning = (jurWithUnkwnZoning / totalNumJur) * 100
print('The percentage of jurisdictions with unknown zoning is ' + str(
        round(percentWithUnkwnZoning, 2)) + '%')

# ----------------- Pages of zoning text --------------------

# Calculate the total number of pages of zoning text
pgnum = za_spreadsheet['# of Pages in the Zoning Code']

totalpgnum = int(pgnum[pgnum.notnull()].sum())
print('The total number of pages with zoning text are ' + str(totalpgnum))

# ----------------- Export to .csv --------------------

# Create a dataframe
data = {'Total # of Jurisdictions': [totalNumJur],
        'Total # of Jursidictions With Zoning': [jurWithZoning],
        'Total # of Jurisdictions Without Zoning': [jurWithoutZoning],
        'Total # of Jurisdictions With Unknown Zoning': [jurWithUnkwnZoning],
        r'% of Jurisdictions With Zoning': [percentWithZoning],
        r'% of Jurisdictions Without Zoning': [percentWithoutZoning],
        r'% of Jurisdictions With Unknown Zoning': [percentWithUnkwnZoning],
        'Total # of Pages of Zoning Text': [totalpgnum]
        }

df = pd.DataFrame(data)

# Save the dataframe to a CSV file
df.to_csv('ZoningJurisdictionStatistics.csv', index=False)