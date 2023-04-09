# Technician Check Form Log Modifications Input

# Context:
# Based on the Check_Form python file, we saved the final dataframe as a CSV
# In addition, every time you restart the file, you can go through the form and the new final dataframe will be appended to the existing CSV
# This python file is meant to update the existing CSV, whether it be the column value/data

# Import Dependencies
import pandas as pd
import numpy

# Print Title
print("Technician Check Form Log Modification!")

# Variables to control the loops below
repeat = "yes"

# Read the existing CSV file
first_df = pd.read_csv('D:\Personal Projects\Personal Work\Diagnostic Process\CheckForm_Logs.csv')

# Additional Variables
num_list = first_df.index.values.tolist()
arr = numpy.array(num_list)

# Display CSV DataFrame Reference 
print("Original CSV DataFrame: ")
print(f"\n{first_df}")

# Update the column value or data in the existing CSV
# These categories hold the variables of what is typed from the technician
while repeat.lower() == "yes":
    
    # Have the technician enter the row number
    csv_row = int(input("\nWhich row is your column value in? (The header is not the first row & row number starts from 0): "))
    
    # Validate the csv_row input
    while csv_row not in arr:
        
        # Display an error, then get another input
        csv_row = int(input("\nInvalid Choice.\nWhich row is your column value in? (The header is not the first row & row number starts from 0): "))

    # Have the technician enter the column name
    csv_column_name = input("\nWhat is the name of the column that the column value is in? ")

    # Validate the csv_column_name
    while csv_column_name not in first_df.columns:

        # Display an error, then get another input
        csv_column_name = input("\nInvalid Choice.\nWhat is the name of the column that the column value is in? ")

    # Ask the technician what the modification value/data will be, when updating the column value/data
    csv_column_value = input("\nWhat will the new column value/data be? ")

    # The actual code to update the column value/data
    first_df.at[csv_row, f'{csv_column_name}'] = f'{csv_column_value}'

    # Display Revised CSV DataFrame
    print("Revised CSV DataFrame: ")
    print(f"\n{first_df}")

    # Ask the technician to verify the Revised CSV DataFrame
    repeat = input("\nIs the following information above correct?\n\nEnter 'yes' to update another column value/data, anything else to stop: ")

# Writing into the file
first_df.to_csv('D:\Personal Projects\Personal Work\Diagnostic Process\CheckForm_Logs.csv', index = False)

