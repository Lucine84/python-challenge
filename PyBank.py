import csv
import os

budget_table=os.path.join("Resources","budget_data.csv")
file_output=os.path.join('Analysis','output.txt')
total_months = 0
total_netprofit = 0
net_change = []
greatest_increase = ['',0]
greatest_decrease = ['',99999999]

with open(budget_table) as csvfile:
    spamreader = csv.reader(csvfile)
    header=next(spamreader)
    first_row=next(spamreader)
    total_netprofit = int(first_row [1])
    total_months = total_months+1
    previous_value=int(first_row[1])
    for row in spamreader:
        total_months+=1
        total_netprofit = total_netprofit+int(row[1])
        value_change = int(row[1])-previous_value
        net_change = net_change + [value_change]
        previous_value = int(row[1])
        # print(previous_value)
        if value_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = value_change
        if value_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = value_change
print (total_months)
print (total_netprofit)
print (net_change)
print (greatest_increase)
print (greatest_decrease)
net_change_average = sum(net_change)/len(net_change)
print (net_change_average)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_netprofit}\n"
    f"Average  Change: ${net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open(file_output, 'w') as output_file:
    output_file.write(output)