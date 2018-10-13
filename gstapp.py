import csv
import gst_calc as g 
with open('persons.csv','w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #filewriter.writerow(['Price ', 'tax'])
    #LOOP FOR UNLIMITED VALUE 

    while(1):
        price=input("Enter the Price : ")
        if price!='q':
            
            tax=int(input("Enter the Tax : "))
            p=int(price)
            raw_price=g.my_cal(p,tax)
            filewriter.writerow([p, tax,raw_price])
        else:
            break    

    
    
