# Discounted price exercise

price = int(input("Enter the price: "))
if (price >= 300):
	disscount = (price * 0.3)
	price = (price - disscount)
	print("30'%' disscount applied for price is,",disscount)
	print("The price after disscount is",price)
elif price in range(200,300):
	disscount = (price * 0.2)
	price = (price - disscount)
	print("20'%' disscount applied for the price is,",disscount)
	print("The price after disscount is",price)
elif price in range(100,200):
	disscount = (price * 0.1)
	price = (price - disscount)
	print("10'%' disscount applied for the price is,",disscount)
	print("The price after disscount is",price)
elif  (price < 100):
	disscount = (price * 0.05)
	price = (price - disscount)
	print("5'%' disscount applied for the price is,",disscount)
	print("The price after disscount is",price)
elif (price  < 0):
	print("No disscount for this price")
else:
	pass