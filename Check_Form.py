# Technician Check-In Form Input
# Each category will have its own data type, converted to other types for calculations and such
# Use the input function to get input from the keyboard

# Import dependencies
import pandas as pd

# Print Title
print("Technician Diagnostic Check-In Form!")

# Variables to control the loops below
repeat = "no"
repeat_2 = "no"

# Additional Variables
default = "N/A"

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

    # Ask the technician to verify the current customer information criteria
    repeat = input("\nIs the following information above correct?\n\nEnter 'no' to redo the customer information input, anything else to move on: ")

    # Get the last element of each sublist from the multiple customer information input lists
    last_elements = []
    for sublist in initial_customer_list:
        last_elements.append(sublist[len(sublist)-1])

# Display the final customer information input list as a dataframe
print(f"\nFinal Customer Information Table: ")
customer_info_df = pd.DataFrame(last_elements, index = ['Customer Name', 'Company', 'Cell Phone Number', 'Other Phone Number',
                                                        'Login Password', 'Login PIN', 'Zip Code', 'Problem', 'Initial Estimate',
                                                        'System'], columns = ['Most Recent Customer'])
print(customer_info_df)

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

        cpu = input(f"\nCPU (Brand, Modifier, Generation, SKU, Product Line, Speed): ")
        cpu_list.append(cpu)

        ram = input("RAM (Total GB, Type of PC, Number of Slots): ")
        ram_list.append(ram)

        os = input("Operating System (Name, Edition, Version, OS Build): ")
        os_list.append(os)

        storage_drives = input("Storage Drives (Total Capacity, Type, Capacity Used, Partitions): ")
        storage_drive_list.append(storage_drives)

        security_soft = input("Security Software (Name, Edition): ")
        security_soft_list.append(security_soft)

        product_soft = input("Productivity Software (Name, Edition): ")
        product_soft_list.append(product_soft)

        system_issue = input("\nFor Windows, list any device manager issues. \nFor MacOS, list any Settings issues. \nFor other OS, list the issues: ")
        system_issue_list.append(system_issue)

        # Add each sublist element to the initial computer specifications input list
        for lst in (cpu_list, ram_list, os_list, storage_drive_list, security_soft_list, 
                    product_soft_list, system_issue_list):
            initial_computer_list.append(lst)

        # Ask the technician to verify the current computer specifications criteria
        repeat_2 = input("\nIs the following information above correct?\n\nEnter 'no' to redo the computer information input, anything else to move on: ")

        # Get the last element of each sublist from the multiple computer information input lists
        final_elements = []
        for sublist in initial_computer_list:
            final_elements.append(sublist[-1])

    # Display the final computer specifications input list as a dataframe
    print(f"\nFinal Computer Information Table: ")
    computer_info_df = pd.DataFrame(final_elements, index = ['CPU', 'RAM', 'Operating System', 'Storage Drive Info', 'Security Software',
                                                            'Productivity Software', 'System Issues'], columns = ['Most Recent Computer'])
    print(computer_info_df)