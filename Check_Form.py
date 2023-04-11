# Technician Check-In Form Input
# Each category will have its own data type, converted to other types for calculations and such
# Use the input function to get input from the keyboard

# Import Dependencies
import pandas as pd
from os import path

# Print Title
print("Technician Diagnostic Check-In Form!")

# Additional Variables (Used in Functions)
default = "N/A"
default_2 = "TBA"

# Automatically find the full path of the file you wish to import into your code
absolute_path = path.dirname(__file__)
relative_path = "CheckForm_Logs.csv"
full_path = path.join(absolute_path, relative_path)

# Asking for Yes/No Questions User Input
# Depending on your answer, your final output can result in different outcomes
ready_check = input("\nAre you ready to input the customer information? Enter 'yes' to begin: ")
if ready_check.lower() == "yes":
    client_check = input("Can you obtain customer information AND computer information? Enter 'yes' to move on, anything else to stay: ")
    if client_check.lower() == "yes":
        
        # Function to obtain customer information 
        def get_customer_input():

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

                # Ask the technician to verify the customer information and redo the process if it is incorrect
                repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

            # Send this function's result (initial_customer_list) to the caller function: get_customer_df()
            return(initial_customer_list)

        # After obtaining the customer information, this function will create a customer info dataframe
        def get_customer_df():

            # Use the value returned from get_customer_input() function inside get_customer_df() function
            initial_customer_list = get_customer_input()

            # Create dataframe from initial_customer_list and transpose the dataframe (rows are columns, columns are rows)
            customer_df = pd.DataFrame(initial_customer_list, index = ['Customer Name', 'Company', 'Cell Phone Number', 'Other Phone Number',
                                                        'Login Password', 'Login PIN', 'Zip Code', 'Problem', 'Initial Estimate',
                                                        'System'])
            customer_info_df = customer_df.transpose()

            # Display the final customer information dataframe
            print(f"\nFinal Customer Information Table: ")
            print(customer_info_df)

            # Send this function's result (customer_info_df) to the caller function: get_merge_df()
            return(customer_info_df)
        
        # Store the result of this function in a variable (df_1)
        df_1 = get_customer_df()
        df_1

        # Yes/No Question (If yes, technician will input computer information. If no, system prints message)
        pc_check = input("\n\nCan you turn on the computer and see the desktop screen? Enter 'yes' to input the computer information: ")
        if pc_check.lower() == "yes":

            # Function to obtain computer information
            def get_computer_input():

                # Variable to control the loop below
                repeat = "no"

                while repeat.lower() == "no":

                    # Make a list of computer information that will be entered
                    initial_computer_list = []

                    # Have the technician enter the computer information for their check form log
                    initial_computer_list.append(input("\nCPU (Brand, Modifier, Generation, SKU, Product Line, Speed): ") or default)
                    initial_computer_list.append(input("RAM (Total GB, Type of PC, Number of Slots): ") or default)
                    initial_computer_list.append(input("Operating System (Name, Edition, Version, OS Build): ") or default)
                    initial_computer_list.append(input("Storage Drives (Total Capacity, Type, Capacity Used, Partitions): ") or default)
                    initial_computer_list.append(input("Security Software (Name, Edition): ") or default)
                    initial_computer_list.append(input("Productivity Software (Name, Edition): ") or default)
                    initial_computer_list.append(input("For Windows, list any device manager issues. \nFor MacOS, list any Settings issues. \nFor other OS, list the issues: ") or default)

                    # Ask the technician to verify the customer information and redo the process if it is incorrect
                    repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the computer information input, anything else to move on: ")

                # Send this function's result (initial_customer_list) to the caller function: get_computer_df()
                return(initial_computer_list)

            # After obtaining the computer information, this function will create a computer info dataframe
            def get_computer_df():

                # Use the value returned from get_computer_input() function inside get_computer_df() function
                initial_computer_list = get_computer_input()

                # Create dataframe from initial_computer_list and transpose the dataframe (rows are columns, columns are rows)
                computer_df = pd.DataFrame(initial_computer_list, index = ['CPU', 'RAM', 'Operating System', 'Storage Drive Info', 'Security Software',
                                                            'Productivity Software', 'System Issues'])
                computer_info_df = computer_df.transpose()

                # Display the final computer information dataframe
                print(f"\nFinal Computer Information Table: ")
                print(computer_info_df)

                # Send this function's result (customer_info_df) to the caller function: get_merge_df()
                return(computer_info_df)
            
            # Store the result of this function in a variable (df_2)
            df_2 = get_computer_df()
            df_2

            # Function to concat the two dataframes from the functions: get_customer_df() and get_computer_df()
            def get_concat_df():

                # Create final dataframe from df_1 and df_2 (function stored results) inside get_concat_df() function
                final_df = pd.concat([df_1, df_2], axis = "columns")

                # Display the final check form log dataframe
                print("\n\nFinal Information Table: ")
                print(f'{final_df}')

                # Send this function's result (final_df) to the caller function: save_df_as_csv()
                return(final_df)
            
            # Store the result of this function in a variable (df_3)
            df_3 = get_concat_df()
            df_3

        # Ends code program and prints message when technician doesn't enter the correct input for the pc_check user input YES/NO question
        else:
            print("\nYou said you can obtain both customer and computer information, so WHY did you NOT enter 'yes'?\nYou did not follow directions. Start Over!")

    # If the technician can ONLY obtain customer information since the technician didn't enter the correct input for client_check user input YES/NO question
    else:

        # Function to obtain ONLY customer information
        def get_all_input():

            # Variable to control the loop below
            repeat = "no"

            while repeat.lower() == "no":

                # Make a list of customer information that will be entered and computer information values will default to 'TBA'
                initial_overall_list = []

                # Have the technician enter the customer information while the computer information will be entered as 'TBA' for their check form log 
                initial_overall_list.append(input("\nName: ") or default)
                initial_overall_list.append(input("Company: ") or default)
                initial_overall_list.append(input("Cell Phone Number: ") or default)
                initial_overall_list.append(input("Other Phone Number: ") or default)
                initial_overall_list.append(input("Operating System Password: ") or default)
                initial_overall_list.append(input("Operating System PIN: ") or default)
                initial_overall_list.append(input("Zip Code: ") or default)
                initial_overall_list.append(input("Problem: ") or default)
                initial_overall_list.append(input("Initial Estimate of Cost: ") or default)
                initial_overall_list.append(input("System (Brand & PC): ") or default)
                initial_overall_list.append(default_2)
                initial_overall_list.append(default_2)
                initial_overall_list.append(default_2)
                initial_overall_list.append(default_2)
                initial_overall_list.append(default_2)
                initial_overall_list.append(default_2)
                initial_overall_list.append(default_2)

                # Ask the technician to verify all the information and redo the process if it is incorrect
                repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

            # Send this function's result (initial_overall_list) to the caller function: get_overall_df()
            return(initial_overall_list)

        # After obtaining the customer information and default computer information, this function will create a final dataframe
        def get_overall_df():

            # Use the value returned from get_all_input() function inside get_overall_df() function
            initial_overall_list = get_all_input()

            # Create dataframe from initial_overall_list and transpose the dataframe (rows are columns, columns are rows)
            overall_df = pd.DataFrame(initial_overall_list, index = ['Customer Name', 'Company', 'Cell Phone Number', 'Other Phone Number',
                                                        'Login Password', 'Login PIN', 'Zip Code', 'Problem', 'Initial Estimate',
                                                        'System', 'CPU', 'RAM', 'Operating System', 'Storage Drive Info', 'Security Software',
                                                        'Productivity Software', 'System Issues'])
            final_df = overall_df.transpose()

            # Display the final check form log dataframe
            print(f"\nFinal Information Table: ")
            print(final_df)

            # Send this function's result (final_df) to the caller function: save_df_as_csv()
            return(final_df)
        
        # Store the result of this function in a variable (df_4)
        df_4 = get_overall_df()
        df_4

# Function to save the final check log dataframe as a CSV file if the file yet exists
# If the CSV file already exists, append the new final dataframe to the created CSV file
def save_df_as_csv():

    # This try/except tests the block of code for errors and handles the errors
    try:
        # Execute this code block if the technician obtained customer and computer information
        # df_3 is the stored result from the get_concat_df() function
        if not path.exists(full_path):
            df_3.to_csv(full_path, header = "Columns", index = False)
        else:
            df_3.to_csv(full_path, mode = 'a', header = False, index = False)
    except:
        # Execute this code block if the technician obtained ONLY customer information
        # df_4 is the stored result from the get_overall_df() function
        if not path.exists(full_path):
            df_4.to_csv(full_path, header = "Columns", index = False)
        else:
            df_4.to_csv(full_path, mode = 'a', header = False, index = False)

    # Loads the created/existing CSV file into a dataframe
    df = pd.read_csv(full_path)

    # Display the new final dataframe in the created/existing CSV file
    print(f'\n\nUpdated CSV DataFrame: ')
    print(f'{df}')

# Store the result of this function in a variable (save_df)
# I don't see a purpose in storing it, but who knows?!
save_df = save_df_as_csv()
save_df