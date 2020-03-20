import os
import csv


filepath= os.path.join ('Resources','budget_data.csv') #append to create file path
pathout = os.path.join('Resources','budget_anyalsis.txt')

#intialize variable
totalrev = 0; totalmonths = 0; Prerevenue = 0; monthchange = []; Revchange_list = []; greatestincr = ["", 0]; greatestdecr = ["", 9999999999999]

budgetdata_csv = "budget_data.csv"
#reads csv and convert it to list dictionaries
with open(budgetdata_csv) as revenue_data:
    reader = csv.reader(revenue_data)
    header = next(reader)
    for row in reader: 
        #print(row)
        #track total
        totalmonths = totalmonths + 1
        totalrev = totalrev + int(row[1])

        #track revenue change
        Revchange = int(row[1])- Prerevenue
        Prerevenue = int(row[1])
        Revchange_list = Revchange_list + [Prerevenue]
        monthchange = monthchange + [row[0]]

        #calc great increase
        if(Revchange>greatestincr[1]):
            greatestincr[0] = row[1]
            greatestincr[1] = Revchange

        #calc greatest decr
        if(Revchange<greatestdecr[1]):
            greatestdecr[0] = row[0]
            greatestdecr[1] = Revchange

# calc average revenue change
Revchange_avg = sum(Revchange_list)/len(Revchange_list)

#get Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------"
    f"Total Months: {totalmonths}\n"
    f"Total Revenue: ${totalrev}\n"
    f"Average Revenue Change: ${Revchange_avg}\n"
    f"Greatest Increase in Revenue: {greatestincr[0]} (${greatestincr[1]})\n"
    f"Greatest Decrease in Revenue: {greatestdecr[0]} (${greatestdecr[1]})\n")

#print out to terminal
print(output)

#store to text file
with open('output') as text:
    text.write(output)








