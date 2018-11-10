import csv 
import os

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print ("Financial Analysis")
    print ("------------------------")
    total = sum(1 for _ in csvfile)
    print("Total Months: " + str(total))
    totalchanges = total - 1
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    prof = 0
    for row in csv.reader(csvfile):
        prof += int(row[1])
    print ("Total: $" + str(prof))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    act = 0
    for row in csv.reader(csvfile):
        first = int(row[1])
        for row1 in csv.reader(csvfile):
             second = int(row1[1])
    act += second - first   
    ac = act/totalchanges
    x = "%.2f" % ac  
    print ("Average Change: $" + str(x))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    rows = []
    for i, row in enumerate(csvreader):
        first = int(row[1])
        for row in csv.reader(csvfile):
            dater = str(row[0])
            second = int(row[1])
            #print(first)
            #print(second)
            act = first - second
            mydict = {"date": dater, "difference": act} 
            mylist= [dater, act] 
            rows.append(mylist)
            #print (mydict)
        print ("Greatest Increase in Profits:") 
        print ("Greatest Decrease in Profits:") 

#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
