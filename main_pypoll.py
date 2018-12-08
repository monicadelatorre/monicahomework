import os
import csv
import operator

# Find the csv file
csvpath = os.path.join("..", "Resources", "election_data_short.csv")

#create output file
dataout = open("election_results.txt",'w')
dataout.close()
csvout = os.path.join("..", "Resources", "election_results.txt")

#lists
voterid = []
county = []
candidate = []


# Read the csv and convert it into a list of dictionaries
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #read the csv file
    
    header = next(csvreader)
    
    # Loop through each row, re-grab each field and store in a new list
    for row in csvreader:

        # Get voter_ids and store it into a list
        #voterid = voterid + [row[0]]
        
        # Get county and store it into a list
        #county = county + [row[1]]
        
        # Grab candidate and store it into a list
        candidate = candidate + [row[2]]
        
    #calculations using python list called candidate
    totalvotes = len(candidate)
        
    #count how many votes each candidate received
    countkahn = candidate. count('Khan')
    countCorrey = candidate. count('Correy')
    countLi = candidate. count('Li')
    countTooley = candidate. count("O'Tooley")
        
    #calculate percentage
    pk = (countkahn/totalvotes)*100
    formatpk = "{0:.3f}".format(pk)
        
    pc = (countCorrey/totalvotes)*100
    formatpc = "{0:.3f}".format(pc)
        
    pl = (countLi/totalvotes)*100
    formatpl = "{0:.3f}".format(pl)
        
    pt = (countTooley/totalvotes)*100
    formatpt = "{0:.3f}".format(pt)
        
#    print(countkahn)
#    print(totalvotes)
#    print(formatpk)
    print ("Election Results")
    print ("--------------------")
    print ("Total Votes = " + str(totalvotes))
    print ("--------------------")
    print ("Kahn: " + str(formatpk)+"%"+" ("+ str(countkahn)+")")
    print ("Correy: " + str(formatpc)+"%"+" ("+ str(countCorrey)+")")
    print ("Li: " + str(formatpl)+"%"+" ("+ str(countLi)+")")
    print ("O'Tooley: " + str(formatpt)+"%"+" ("+ str(countTooley)+")")
       
    #create a dictionary with results from calculations
    cand_dict = {"Kahn":countkahn,"Correy":countCorrey,"Li":countLi,"O'Tooley":countTooley}
    
    #find the max value in the dictionary called cand_dict to find the winner
    b = max(cand_dict.items(), key=operator.itemgetter(1))[0]
    print ("Winner: " + str(b))
    
    #print to the txt file that was created 
    with open(csvout,"w") as candout:  
        candout.write("Election Results"+"\n")
        candout.write("--------------------"+"\n")
        candout.write("Total Votes = " + str(totalvotes)+"\n")
        candout.write("--------------------"+"\n")
        candout.write("Kahn: " + str(formatpk)+"%"+" ("+ str(countkahn)+")"+"\n")
        candout.write("Correy: " + str(formatpc)+"%"+" ("+ str(countCorrey)+")"+"\n")
        candout.write("Li: " + str(formatpl)+"%"+" ("+ str(countLi)+")"+"\n")
        candout.write("O'Tooley: " + str(formatpt)+"%"+" ("+ str(countTooley)+")"+"\n")
        candout.write("Winner: " + str(b))