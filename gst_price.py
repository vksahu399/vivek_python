while(1):
    pri_gst=input("Enter the price with gst : ")
    #tax=int(input("enter the tax"))
    if pri_gst!='q':
        tax=100+18
        price=int(pri_gst)*100/tax
        print("{0:.2f}".format(price))
    else:
        print("quit")
        break
#print("%.2f" % a)
