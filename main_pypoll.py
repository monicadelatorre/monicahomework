import csv
import os
import operator

# Find the csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")

#create output file
dataout = open("election_results.txt",'w')
dataout.close()
csvout = os.path.join("..", "Resources", "election_results.txt")

#variables
candidate=[]

#open the csv file and read it
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    #convert the csv file you just read into a python list
    convert_list = list(reader)
    
    #test print row 1
    #print(convert_list[1])
    #test print element in row 1, col 3
    #print(convert_list[1][2])
    
#make a new list out of the candidate column only, sub[2] is the third column 
candidate = [sub[2] for sub in convert_list]
#print(candidate)


totalvotes = len(candidate)

#count how many votes each candidate received
countkahn = candidate.count('Khan')
countCorrey = candidate.count('Correy')
countLi = candidate.count('Li')
countTooley = candidate.count("O'Tooley")
        
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
        candout.write("--------------------"+"\n")
        candout.write("Winner: " + str(b)+"\n")
        candout.write("--------------------"+"\n")



    
#print(your_list)