# import the files of budget_data csv/modules
import  os
import csv
#creating a pathway to access the file
csvpath = os.path.join('Resources','budget_data.csv')
#Assigning the values and creating the lists
total_months = 0
profit = []
dates = []
Average_change = 0 
Total_net_amount = 0 
value = 0
# opening the csv file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # reading the header - 'next" helps to skip the header row
    csv_header = next(csvreader)
    # reading the first row
    first_row = next(csvreader)
    total_months += 1
    Total_net_amount += int(first_row[1])
    value = int(first_row[1])
    # looping through the first row & header
    for row in csvreader:
        # appending the row 0 to dates
        dates.append(row[0])
        # Calculate the changes 
        Average_change = int(row[1])-value
        profit.append(Average_change)
        value = int(row[1])
        # to calculate total months
        total_months += 1
        # to calculate total net amount
        Total_net_amount = Total_net_amount + int(row[1])
# to calculate greatest increase of profits
GPI = max(profit)
GPI_index = profit.index(GPI)
GPI_month = dates[GPI_index]

# to calculate greatest decrease of profits
GPD = min(profit)
GPD_index = profit.index(GPD)
GPD_month = dates[GPD_index]

#finally clalutate the average change
Avg_change = sum(profit)/len(profit)

# print the results
print("Financial Analysis")
print("----------------------")
print(f"Total Months : {str(total_months)}")
print(f"Total net amount : {str(Total_net_amount)}")
print(f"Average change : $ {str(round(Avg_change,2))}")
print(f"Greatest Increase in Profits : {GPI_month} (${str(GPI)})")
print(f"Greatest Decrease in Profits : {GPD_month} (${str(GPD)})")

# export to .txt file
output = open("output.txt", "w")
line1 = ("Financial Analysis")
line2 = ("----------------------")
line3 = str(f"Total Months : {str(total_months)}")
line4 = str(f"Total net amount : {str(Total_net_amount)}")
line5 = str(f"Average change : $ {str(round(Avg_change,2))}")
line6 = str(f"Greatest Increase in Profits : {GPI_month} (${str(GPI)})")
line7 = str(f"Greatest Decrease in Profits : {GPD_month} (${str(GPD)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
