#input sale amount
amt = int( input("enter sale amount :"))
#checking conditions and calculating discount
    if(amt > 0) : 
           if amt <= 5000 :
              disc = amt * 0.05
           else if amt <= 15000 :
               disc = amt * 0.12
            else if amt <= 25000 :
               disc = amt * 0.2
            else :
                   disc = amt * 0.3
            print("Discount :", disc)
            print("Net Pay :", amt-disc)

            else :
                  print("invalid amount")
