# Import Dependencies
import pandas as pd
from os import path

# Print Title
print("Technical Diagnostic Check-In Form!")

# Additional Variables (Used in Functions)
default = "N/A"
default_2 = "TBA"

# Automatically find the full path of the file you wish to import into your code
absolute_path = path.dirname(__file__)
relative_path = "CheckForm_Logs.csv"
full_path = path.join(absolute_path, relative_path)

# Constants
CUSTOMER_FIELDS = customer_fields = ['Name', 'Company', 'Cell Phone Number', 'Other Phone Number',
                   'Operating System Password', 'Operating System PIN', 'Zip Code',
                   'Problem', 'Initial Estimate of Cost', 'System (Brand & PC)']
COMPUTER_FIELDS = computer_fields = ['CPU','RAM', 'Operating System', 'Storage Drives', 'Security Software',
                   'Productivity Software', 'System Issues']
ALL_FIELDS = all_fields = ['Name', 'Company', 'Cell Phone Number', 'Other Phone Number','Operating System Password', 
                           'Operating System PIN', 'Zip Code', 'Problem', 'Initial Estimate of Cost', 'System (Brand & PC)',
                           'CPU','RAM', 'Operating System', 'Storage Drives', 'Security Software', 'Productivity Software', 
                           'System Issues']

# Function to take in a list of field names and return a final dataframe 
def get_form_input():

    # Asking for Yes/No Questions User Input
    # Depending on your answer, your final output can result in different outcomes
    client_check = input("Can you obtain customer information AND computer information? Enter 'yes' to move on, anything else to stay: ")
    if client_check.lower() == "yes":

        # Variable to control the loop below
        repeat = "no"
        while repeat.lower() == "no":

            # Make a list of customer information that will be entered
            initial_customer_list = []

            # Have the technician enter the customer information for their check form log
            initial_customer_list.append(input("\nName: ") or default)
            initial_customer_list.append(input("Company: ") or default)
            initial_customer_list.append(input("Cell Phone Number: ") or default)
            initial_customer_list.append(input("Other Phone Number: ") or default)
            initial_customer_list.append(input("Operating System Password: ") or default)
            initial_customer_list.append(input("Operating System PIN: ") or default)
            initial_customer_list.append(input("Zip Code: ") or default)
            initial_customer_list.append(input("Problem: ") or default)
            initial_customer_list.append(input("Initial Estimate of Cost: ") or default)
            initial_customer_list.append(input("System (Brand & PC): ") or default)

            # Create dataframe from initial_customer_list and transpose the dataframe (rows are columns, columns are rows)
            client_df = pd.DataFrame(initial_customer_list, index = customer_fields)
            customer_df = client_df.transpose()

            # Display the final customer information dataframe
            print(f"\nFinal Customer Information Table: ")
            print(customer_df)

            # Ask the technician to verify the customer information and redo the process if it is incorrect
            repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

            # Yes/No Question (If yes, technician will input computer information. If no, system prints message)
            pc_check = input("\n\nCan you turn on the computer and see the desktop screen? Enter 'yes' to input the computer information: ")
            if pc_check.lower() == "yes":
                
                # Variable to control the loop below
                repeat_2 = "no"
                while repeat_2.lower() == "no":

                    # Make a list of computer information that will be entered
                    initial_computer_list = []

                    # Have the technician enter the computer information for their check form log
                    initial_computer_list.append(input("\nCPU (Brand, Modifier, Generation, SKU, Product Line, Speed): ") or default)
                    initial_computer_list.append(input("RAM (Total GB, Type of PC, Number of Slots): ") or default)
                    initial_computer_list.append(input("Operating System (Name, Edition, Version, OS Build): ") or default)
                    initial_computer_list.append(input("Storage Drives (Total Capacity, Type, Capacity Used, Partitions): ") or default)
                    initial_computer_list.append(input("Security Software (Name, Edition): ") or default)
                    initial_computer_list.append(input("Productivity Software (Name, Edition): ") or default)
                    initial_computer_list.append(input("For any OS, list any system issues: ") or default)

                    # Ask the technician to verify the computer information and redo the process if it is incorrect
                    repeat_2 = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

                    # Create dataframe from initial_computer_list and transpose the dataframe (rows are columns, columns are rows)
                    pc_df = pd.DataFrame(initial_computer_list, index = computer_fields)
                    computer_df = pc_df.transpose()

                     # Create final dataframe from customer_df and computer_df
                    final_df = pd.concat([customer_df, computer_df], axis = "columns")

                    # Display the final check form log dataframe
                    print("\n\nFinal Information Table: ")

                    # Send this function's result (final_df) to the caller function: save_df_as_csv()
                    print(f'{final_df}')
                    return(final_df)
            
            # Restarts code program and prints message when technician doesn't enter the correct input for the pc_check user input YES/NO question
            else:
                print("\nYou said you can obtain both customer and computer information, so WHY did you NOT enter 'yes'?\nYou did not follow directions. Start Over!")

    # If the technician can ONLY obtain customer information since the technician didn't enter the correct input for client_check user input YES/NO question
    else:

        # Variable to control the loop below
        repeat = "no"
        while repeat.lower() == "no":

            # Make a list of customer information that will be entered and computer information values will default to 'TBA'
            initial_list = []

            # Have the technician enter the customer information while the computer information will be entered as 'TBA' for their check form log 
            initial_list.append(input("\nName: ") or default)
            initial_list.append(input("Company: ") or default)
            initial_list.append(input("Cell Phone Number: ") or default)
            initial_list.append(input("Other Phone Number: ") or default)
            initial_list.append(input("Operating System Password: ") or default)
            initial_list.append(input("Operating System PIN: ") or default)
            initial_list.append(input("Zip Code: ") or default)
            initial_list.append(input("Problem: ") or default)
            initial_list.append(input("Initial Estimate of Cost: ") or default)
            initial_list.append(input("System (Brand & PC): ") or default)
            initial_list.append(default_2)
            initial_list.append(default_2)
            initial_list.append(default_2)
            initial_list.append(default_2)
            initial_list.append(default_2)
            initial_list.append(default_2)
            initial_list.append(default_2)

            # Ask the technician to verify all the information and redo the process if it is incorrect
            repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

            # Create dataframe from initial_overall_list and transpose the dataframe (rows are columns, columns are rows)
            initial_df = pd.DataFrame(initial_list, index = all_fields)
            final_df = initial_df.transpose()

            # Display the final check form log dataframe
            print("\n\nFinal Information Table: ")
            print(f'{final_df}')

            # Send this function's result (final_df) to the caller function: save_df_as_csv()
            return(final_df)

# Store the result of this function in a variable (last_df) to the caller function: save_df_as_csv()
last_df = get_form_input()
last_df

# Function to save the final check log dataframe as a CSV file if the file yet exists
# If the CSV file already exists, append the new final dataframe to the created CSV file
def save_df_as_csv():
    if not path.exists(full_path):
        last_df.to_csv(full_path, header = "Columns", index = False)
    else:
        last_df.to_csv(full_path, mode = 'a', header = False, index = False)
    
     # Loads the created/existing CSV file into a dataframe
    df = pd.read_csv(full_path)

    # Display the new final dataframe in the created/existing CSV file
    print(f'\n\nUpdated CSV DataFrame: ')
    print(f'{df}')

# Execute the function
save_df_as_csv()