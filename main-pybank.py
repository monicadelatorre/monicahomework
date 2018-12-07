import os
import csv

# Find the csv file
csvpath = os.path.join("..", "Resources", "budget_data.csv")
budget_data_out = open("budget_data_out.txt",'w')
budget_data_out.close()
csvout = os.path.join("..", "Resources", "budget_data_out.txt")

#variables
total_months = 0
total_net = 0

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #read the csv file
    headers = next(csvreader) #skip the first row
    #print (headers)
    total_months = sum(1 for row in csvreader) #count the rows
    #print (total_months)
    print ("Financial Analysis")
    print ("--------------------")  
    print ("Total Months = " + str(total_months)) #print the number of months

    
# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #read the csv file

    #get total net
    #first_row = next(csvreader)#skip first row
    
    for row in csvreader:

        #create a list consisting of elements in column2
        all_data = [float(row[1]) for row in csvreader]
        sall_data = sum(all_data)
        #create another list called diff_months with the differences of 
        #month to month using an offset list from all_data, offset by 1
        diff_months = [(y-x) for x, y in zip(all_data, all_data[1:])]
        #print (len(diff_months))
        average_change = sum(diff_months)/len(diff_months)
        format = "{0:.2f}".format(average_change)
        #print(diff_months)
        #print (average_change)
        max_change = max(diff_months)
        min_change = min(diff_months)
        
    print("Total Net = " + str(sall_data))
    print("Average Change = " + str(format))
    print("Greatest Increase = " + str(max_change))
    print("Greatest Decrease = " + str(min_change))

    with open(csvout,"w") as bdout:  
        bdout.write("Financial Analysis")
        bdout.write("\n")
        bdout.write("--------------------")
        bdout.write("\n")
        bdout.write("Total Months = " + str(total_months)) #print the number of months
        bdout.write("\n")
        bdout.write("Total Net = " + str(sall_data))
        bdout.write("\n")
        bdout.write("Average Change = " + str(format))
        bdout.write("\n")
        bdout.write("Greatest Increase = " + str(max_change))
        bdout.write("\n")
        bdout.write("Greatest Decrease = " + str(min_change))
        
            
    
        
