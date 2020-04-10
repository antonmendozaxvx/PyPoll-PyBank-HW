import os
import csv

bank_csv = os.path.join('budget_data.csv')

with open(bank_csv, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    analyze_bank(csvreader)

    # define variables
    month_count = 0
    total_profit = 0
    month_list = []
    month_profit = 0
    change = 0
    change_list = []
    
    # start loop
    for row in data:
       
       #months
        month_count += 1
        
       #profit
        total_profit += int(row[1])
        
        # add each month to list
        month_list.append(str(row[0]))
        
        #changes in profit
        if change != 0:
            
            # set month_profit to value
            month_profit = int(row[1])
            
            # fine monthly change in profits
            change = month_profit - change
            change_list.append(change)
            
            # reset change variable
            change = int(row[1]) 
            
    # skip first month because there is no change 
    month_list.pop(0)
    
    # find greatest increase in profits
    indxmax = change_list.index(max(change_list))

    # find greatest decrease in profits
    indxmin = change_list.index(min(change_list))

    # find month that corresponds to the values
    max_change = (month_list[int(indxmax)], max(change_list))
    min_change = (month_list[int(indxmin)], min(change_list))
    
    # average
    average = sum(change_list)/float(len(change_list))
    average = round(average,2)
    
    # print results
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {month_count}')
    print(f'Net Profit: {total_profit}')
    print(f'Average Monthly Change: {average}')
    print(f'Greatest Increase in Profits: {max_change}')
    print(f'Greatest Loss In Profits: {min_change}')

    # set exit path
    bank_output = os.path.join("PyBankResults.txt")    
    
    # write results
    with open(bank_output, 'w') as txtfile:
        txtfile.write('Financial Analysis')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Months: {month_count}')
        txtfile.write(f'\nNet Profit: {total_profit}')
        txtfile.write(f'\nAverage Monthly Change: {average}')
        txtfile.write(f'\nGreatest Increase In Profits: {max_change}')
        txtfile.write(f'\nGreatest Loss In Profits: {min_change}')
