def my_cal(pri_gst,tax):
        tax=100+18
        price=int(pri_gst)*100/tax
        #print("{0:.2f}".format(price))
        
        return (round(price,2))
    