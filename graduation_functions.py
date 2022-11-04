import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('..','Resources','graduation_data.csv')

# Define the function and have it accept the 'state_data' as its sole parameter

def print_percentages(state_data:list) -> None:

    # Find the total students (for the given state)
    total_students = int(state_data[1] + state_data[3] + state_data[5])
    # Find the total graduates
    total_graduates = int(state_data[2] + state_data[4] + state_data[6])
    # Find the public school graduation rate
    public_graduates = int(state_data[2]/state_data[1]) 
    # Remember that some states do not have nonprofit or forprofit private schools
    # Find the non-profit school graduation rate
    if float(state_data[3])==0:
        nonprofit_graduates = 'UNDEFINED!"'
    else:
        nonprofit_graduates = float(state_data[4])/float(state_data[3])
    # Find the for-profit school graduation rate
    forprofit_graduates = int(state_data[6]/state_data[5]) 
    # Calculate the overall graduation rate
    overall_grad_rate = total_graduates/total_students
    # Print out the state's name and its graduation rates
    print('Sate name : {} \n Public School grad rate: {} \n NP grad rate: {} \n FP grad rate: {}'.format(state_data[0],public_graduates,nonprofit_graduates,forprofit_graduates,overall_grad_rate))




# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
