dict = {}
ch = 'y'
while ch == 'y' or ch == 'Y':
	name = input("Enter the product name : ")
	price = float(input("Enter price in rupees : "))
	dict[name] = price
	ch = input("Do you want to add more items (Y/N) : ")
print(dict)
prod_name = input("Enter the product to be searched : ")
for i in dict:
	if i == prod_name:
		print("Product found", i,"with price as:",dict[i])
