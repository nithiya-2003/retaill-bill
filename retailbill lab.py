n=int(input("enter the no item"))
total=0
for i in range (n):
    itemname=input("enter the name          :")
    cost=int(input("cost of item            :"))
    quantity=int(input("enter the quantity      :"))
    amount=cost*quantity
    total=total+amount
    print("==========================================================")
print("toal amount of your purchase is:",total)    
print("****************************THANK YOU**********************************")
