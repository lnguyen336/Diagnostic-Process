# Technician Check-In Form Input
# Each category will have its own data type, converted to other types for calculations and such
# Use the input function to get input from the keyboard

# Import dependencies
import pandas as pd
from os import path

# Print Title
print("Technician Diagnostic Check-In Form!")

# Variables to control the loops below
repeat = "no"
repeat_2 = "no"

# Additional Variables
default = "N/A"
default_2 = "TBA"

while repeat.lower() == "no":
    # Customer Information Lists
    name_list = []
    company_list = []
    cell_phone_list = []
    other_phone_list = []
    os_password_list = []
    os_pin_list = []
    zip_code_list = []
    problem_list = []
    initial_estimate_list = []
    system_list = []
    initial_customer_list = []

    # Front Side of Check-In Form
    # These categories hold the results of what is typed from the technician
    # For each component of the customer information list, the inputs have the technician enter the information
    # For each component of the customer information list, the inputs will be added to each component's list
    Name = input(f"\nName: ") or default
    name_list.append(Name)

    Company = input("Company: ") or default
    company_list.append(Company)

    Cell_Phone_Number = input("Cell Phone Number: ") or default
    cell_phone_list.append(Cell_Phone_Number)

    Other_Phone_Number = input("Other Phone Number: ") or default
    other_phone_list.append(Other_Phone_Number)

    OS_Password = input("Operating System Password: ") or default
    os_password_list.append(OS_Password)

    OS_Pin = input("Operating System PIN: ") or default
    os_pin_list.append(OS_Pin)

    Zip_Code = input("Zip Code: ") or default
    zip_code_list.append(Zip_Code)

    Problem = input("Problem: ") or default
    problem_list.append(Problem)

    Initial_Estimate = (input("Initial Estimate of Cost: ")) or default
    initial_estimate_list.append(Initial_Estimate)

    System = input("System (Brand & PC): ") or default
    system_list.append(System)

    # Add each sublist element to the initial customer information input list 
    for lst in (name_list, company_list, cell_phone_list, other_phone_list, os_password_list, os_pin_list, zip_code_list, 
                problem_list, initial_estimate_list, system_list):
        initial_customer_list.append(lst)

    # Back Side of Check-In Form
    # These categories hold the results of 'TBA' if the technician only obtained customer information

    # Computer Specifications Lists
    cpu_list = []
    ram_list = []
    os_list = []
    storage_drive_list = []
    security_soft_list = []
    product_soft_list = []
    system_issue_list = []
    initial_check_list = []

    cpu = default_2
    cpu_list.append(cpu)

    ram = default_2
    ram_list.append(ram)

    os = default_2
    os_list.append(os)

    storage_drives = default_2
    storage_drive_list.append(storage_drives)

    security_soft = default_2
    security_soft_list.append(security_soft)

    product_soft = default_2
    product_soft_list.append(product_soft)

    system_issue = default_2
    system_issue_list.append(system_issue)

    # Add each sublist element to the inital check form input list if the technician ONLY obtained customer information
    for lst in (name_list, company_list, cell_phone_list, other_phone_list, os_password_list, os_pin_list, zip_code_list, 
                problem_list, initial_estimate_list, system_list, cpu_list, ram_list, os_list, storage_drive_list, security_soft_list, 
                product_soft_list, system_issue_list):
        initial_check_list.append(lst)

    # Ask the technician to verify the current customer information criteria
    repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

# Display the final customer information input list as a dataframe
# If the technician obtained customer information and can turn on the computer and see the desktop screen, this dataframe will be merged with pc_info_df
print(f"\nFinal Customer Information Table: ")
customer_df = pd.DataFrame(initial_customer_list, index = ['Customer Name', 'Company', 'Cell Phone Number', 'Other Phone Number',
                                                        'Login Password', 'Login PIN', 'Zip Code', 'Problem', 'Initial Estimate',
                                                        'System'])
customer_info_df = customer_df.transpose()

# If the technician ONLY obtained customer information, there will only be one dataframe to work with
client_info_df = pd.DataFrame(initial_check_list, index = ['Customer Name', 'Company', 'Cell Phone Number', 'Other Phone Number',
                                                        'Login Password', 'Login PIN', 'Zip Code', 'Problem', 'Initial Estimate',
                                                        'System', 'CPU', 'RAM', 'Operating System', 'Storage Drive Info', 'Security Software',
                                                        'Productivity Software', 'System Issues'])
check_info_df = client_info_df.transpose()

print(check_info_df)

# Ask the technician to verify that they can turn on the computer and see the desktop screen to input the computer information
computer_check = input("\n\nCan you turn on the computer and see the desktop screen? Enter 'yes' to input the computer information: ")
if computer_check.lower() == "yes":
    while repeat_2.lower() == "no":
        # Computer Specifications Lists
        cpu_list = []
        ram_list = []
        os_list = []
        storage_drive_list = []
        security_soft_list = []
        product_soft_list = []
        system_issue_list = []
        initial_computer_list = []

        # Back Side of Check-In Form
        # These categories hold the results of what is typed from the technician
        # For each component of the computer information list, the inputs have the technician enter the information
        # For each component of the computer information list, the inputs will be added to each component's list
        cpu = input(f"\nCPU (Brand, Modifier, Generation, SKU, Product Line, Speed): ") or default
        cpu_list.append(cpu)

        ram = input("RAM (Total GB, Type of PC, Number of Slots): ") or default
        ram_list.append(ram)

        os = input("Operating System (Name, Edition, Version, OS Build): ") or default
        os_list.append(os)

        storage_drives = input("Storage Drives (Total Capacity, Type, Capacity Used, Partitions): ") or default
        storage_drive_list.append(storage_drives)

        security_soft = input("Security Software (Name, Edition): ") or default
        security_soft_list.append(security_soft)

        product_soft = input("Productivity Software (Name, Edition): ") or default
        product_soft_list.append(product_soft)

        system_issue = input("\nFor Windows, list any device manager issues. \nFor MacOS, list any Settings issues. \nFor other OS, list the issues: ") or default
        system_issue_list.append(system_issue)

        # Add each sublist element to the initial computer specifications input list
        for lst in (cpu_list, ram_list, os_list, storage_drive_list, security_soft_list, 
                    product_soft_list, system_issue_list):
            initial_computer_list.append(lst)

        # Ask the technician to verify the current computer specifications criteria
        repeat_2 = input("\nIs the following information above correct?\n\nEnter 'no' to redo the computer information input, anything else to move on: ")

    # Display the final computer specifications input list as a dataframe
    print("\nFinal Computer Information Table: ")
    computer_info_df = pd.DataFrame(initial_computer_list, index = ['CPU', 'RAM', 'Operating System', 'Storage Drive Info', 'Security Software',
                                                            'Productivity Software', 'System Issues'])
    pc_info_df = computer_info_df.transpose()

    print(pc_info_df)

# Merge the two dataframes if the technician obtained the customer information and computer information
# If not, the final dataframe will just be the customer information with computer information as 'TBA'
try:
    final_df = pd.concat([customer_info_df, pc_info_df], axis = "columns")
    print("\n\nFinal DataFrame: ")
    print(f'{final_df}')
except NameError:
    print("\n\nFinal DataFrame: ")
    final_df = check_info_df
    print(f'{final_df}')

# First, save the final dataframe as a CSV file
# If CSV file is already written, append the new final dataframe to the existing CSV file
if not path.exists('D:\Personal Projects\Personal Work\Diagnostic Process\CheckForm_Logs.csv'):
    final_df.to_csv("D:\Personal Projects\Personal Work\Diagnostic Process\CheckForm_Logs.csv", header = "columns", index = False)
else:
    final_df.to_csv("D:\Personal Projects\Personal Work\Diagnostic Process\CheckForm_Logs.csv", mode = 'a', header = False, index = False)