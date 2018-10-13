import csv
 
with open('persons.csv','w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'contact_num'])
    #LOOP FOR UNLIMITED VALUE 

    while(1):
        name=input("Enter the Name : ")
        if name!='q':
            contact_num=input("Enter the contact number : ")
            filewriter.writerow([name, contact_num])
        else:
            break    

    
    
