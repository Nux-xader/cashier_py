import csv
from datetime import datetime

def readCsv(label):
	while True:
		path = str(input(label))
		try:
			with open(path) as f:
				reader = csv.reader(f)
				header = next(reader)
				return [{x[0]: x[1:]} for x in reader]
		except FileNotFoundError:
			print("File "+path+" not found")

def renderData(products, request):
	result = ""
	for x in request:
		key, value = list(x.keys())[0], list(x.values())[0][0]
		for y in products:
			if key in list(y.keys()):
				result+=y[key][0]+": "+value+" @ "+y[key][1]+"\n"
				break
	return result[:-1]


def rounding(data):
	data = str(data)
	result = data.split(".")[0]
	data = data.split(".")[1]
	if len(data) <= 2:
		return float(result+"."+data)
	subData = data[:2]
	if int(data[2]) > 5:
		subData = subData[0]+str(int(subData[1])+1)
	return float(result+"."+subData)

def compute(products, request, salestax=0.92):
	item, subtotal, total = 0, 0, 0
	for x in request:
		key, value = list(x.keys())[0], list(x.values())[0][0]
		for y in products:
			if key in list(y.keys()):
				item+=float(value)
				subtotal+=float(value)*float(y[key][1])
				break
	if int(item) == item: item = int(item)
	subtotal = rounding(subtotal)
	total = subtotal+salestax
	return item, subtotal, total


products = readCsv("Input file products.csv : ")
request = readCsv("Input file request.csv : ")

shopname = "loremipsum"
salestax = 0.06
item, subtotal, total = compute(products, request, salestax)
current_date_and_time = datetime.now()

print("\n"+shopname)
print("\n"+renderData(products, request)+"\n")
print("Number of Items: "+str(item))
print("Subtotal: "+str(subtotal))
print("Sales Tax: "+str(salestax))
print("Total: "+str(total))
print("\nThank you for shopping at the "+shopname+".")
print(f"{current_date_and_time:%A %b  %d %I:%M:%S %Y}")