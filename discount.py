#A software company sells a package that retails for $99. Quantity discounts are given according to the following table. Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.

#Quantity	Discount
#10-19	10%
#20-49	20%
#50-99	30%
#100 or more	40%

unit_price = 99
discount = 0
price = 0
quantity = int(input("Enter quantity of items"))
if 10 <= quantity <= 19:
    price = quantity * unit_price * 0.9
    discount = 10
elif 20 <= quantity <= 49:
    price = quantity * unit_price * 0.8
    discount = 20
elif 50 <= quantity <= 99:
    price = quantity * unit_price * 0.7
    discount = 30
elif quantity >= 100:
    price = quantity * unit_price * 0.6
    discount = 40
elif quantity < 0:
    print("Invalid")
print("Discount: "+str(discount)+"%")
print("Price: £"+str('{0:.2f}'.format(price)))