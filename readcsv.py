import csv
import gst_calc as g
with open('persons.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in myreader:
        
        x=g.my_cal(row[0],row[1])
        #print(x)
        print(row[0],row[1],x)