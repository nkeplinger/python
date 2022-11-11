import os 
import csv
import sys

monthlist =[]
profitlist = []
'''Part 1'''
csvPyBankpath = os.path.join('PyBank','Resources','budget_data.csv')
with open(csvPyBankpath) as csvPyBankfile:
    csvreader = csv.reader(csvPyBankfile, delimiter=',')
    # skip first row/header row
    next(csvreader)
        
    #append the first item in col1 of csv list to monthlist 
    monthlist = [x[0] for x in csvreader]
    #total number of month i.e. number of items in list
    num_of_months = len(monthlist)


'''Part 2'''
#sum_of_profits = sum(item for item in profitlist)
with open(csvPyBankpath) as csvPyBankfile:
    csvreader = csv.reader(csvPyBankfile, delimiter=',')
    # skip first row/header row
    next(csvreader)
    
    months_in = []
    profitlist = []
    for col in csvreader:
        months_in.append(col[0])
        profitlist.append(col[1])
   

    #append the first item in col1 of csv list to profitlist
    ###profitlist = [x[1] for x in csvreader]
    #turn all alements in list into new int list instead of strings 
    profitnum = [int(y) for y in profitlist]
   #sum of all profits
    total_profit = sum(profitnum) 
    #find average change from begin to end
    mean_profit = (profitnum[-1]) - (profitnum[0])
    #ask for help in office hours
    '''WORKS!! MODIFY TO ANSER QUESTIONS'''
    change = []
    previous_item = 0
    for item in profitnum:
        #print('current item is {} and previous_iten is {}'.format(previous_item, item))
        ####find the greatest 
        changeitem = [ (item) - previous_item]
        change.append(changeitem)
        previous_item = item
    
    #print(change)
    max_value = max(change)
    indexmax = change.index(max_value)
    #print(indexmax)
    min_value = min(change)
    indexmin = change.index(min_value)
    #print(indexmin)


    #print(months_in)
    greatest_increase_month = months_in[indexmax]
    greatest_decrease_month = months_in[indexmin]
    greatest_increase_value = change[indexmax]
    greatest_decrease_value = change[indexmin]

print(' Financial Analysis \n ---------------------------- \n Total Months: {} \n Total: ${} \n Average Change: ${} \n Greates Increase in Profits: {} ({}) \n Greates Decrease in Profits: {} ({})'.format(num_of_months,total_profit,mean_profit,greatest_increase_month,greatest_increase_value,greatest_decrease_month,greatest_decrease_value))

#lines = [' Financial Analysis', '----------------------------','Total Months: {}'format(num_of_months),' Total: ${}'.format(total_profit),'Average Change: ${} '.format(mean_profit),'Greates Increase in Profits: {} ({}) '.format(greatest_increase_month,greatest_increase_value),'Greates Decrease in Profits: {} ({})'.format(greatest_decrease_month,greatest_decrease_value)]
#with open('OUTPUT_PyBANK.txt', 'w') as f:
#    f.writelines(lines)
