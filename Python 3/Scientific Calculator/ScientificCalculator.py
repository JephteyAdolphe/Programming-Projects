import tkinter as tk
import math

HEIGHT = 500
WIDTH = 400

TITLE = "Jeff's Scientific Calculator"

rows = 6
columns = 4


operationDict  = {
	"addition": False,
	"subtraction": False,
	"multiplication": False,
	"division": False,
	"errCheck": False,
	"equal": False
}



def set_text(text):
	errCheck = entry.get()
	if (errCheck.count(".") == 1 and text == "."):	# prevents multiple decimal points
		return

	if (operationDict["errCheck"] == True) or (errCheck == "Err"):
		entry.delete(0, tk.END)
		operationDict["errCheck"] = False

	if (operationDict["equal"] == True):		# prevents results from being altered
		entry.delete(0, tk.END)
		operationDict["equal"] = False

	if (errCheck.count("0") == 1 and len(errCheck) == 1 and text == "0"):		# prevents unneccessary zeros
		return

	if (errCheck == "0" and len(errCheck) == 1):
		entry.delete(0, tk.END)
		entry.insert(tk.END, text)
	else:
		entry.insert(tk.END, text)


def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num

class Operations:
	def __init__(self):
		self.temp = None
		self.queueArr = []		# saves val waiting to be manipulated

	def operationPressed(self):
		self.temp = float(entry.get())
		self.queueArr.append(self.temp)
		self.temp = None
		entry.delete(0, tk.END)

	def equalPressed(self):
		otherTemp = float(entry.get())
		self.queueArr.append(otherTemp)
		entry.delete(0, tk.END)

		if (operationDict['addition'] == True):
			res = sum(self.queueArr)
			self.queueArr.clear()
			print(res)
			res = formatNumber(res)
			entry.insert(tk.END, res)

		elif (operationDict['subtraction'] == True):
			res = self.queueArr[0] - self.queueArr[1]
			self.queueArr.clear()
			print(res)
			res = formatNumber(res)
			entry.insert(tk.END, res)

		elif (operationDict['multiplication'] == True):
			res = self.queueArr[0] * self.queueArr[1]
			self.queueArr.clear()
			print(res)
			res = formatNumber(res)
			entry.insert(tk.END, res)

		elif (operationDict['division'] == True):
			try:
				res = self.queueArr[0] / self.queueArr[1]
				self.queueArr.clear()
				print(res)
				res = formatNumber(res)
				entry.insert(tk.END, res)
			except:
				self.clearEverything()
				set_text("0")
				operationDict["errCheck"] = True

		for i in operationDict:
			operationDict[i] = False
		operationDict["equal"] = True

	def addition(self):
		operationDict['addition'] = True
		self.operationPressed()

	def subtraction(self):
		operationDict['subtraction'] = True
		self.operationPressed()

	def multiplication(self):
		operationDict['multiplication'] = True
		self.operationPressed()

	def division(self):
		operationDict['division'] = True
		self.operationPressed()

	def clearEverything(self):
		self.queueArr.clear()
		entry.delete(0, tk.END)
		set_text("0")
		for i in operationDict:
			operationDict[i] = False

	def clearCurrentEntry(self):
		entry.delete(0, tk.END)
		set_text("0")

	def backSpace(self):
		entry.delete(len(entry.get())-1)

	def square(self):
		curVal = float(entry.get())
		squareVal = curVal ** 2
		entry.delete(0, tk.END)
		squareVal = formatNumber(squareVal)
		print(squareVal)
		entry.insert(tk.END, squareVal)
		operationDict["errCheck"] = True

	def reciprocal(self):
		try:
			curVal = float(entry.get())
			recipVal = 1 / curVal
			entry.delete(0, tk.END)
			recipVal = formatNumber(recipVal)
			print(recipVal)
			entry.insert(tk.END, recipVal)
			operationDict["errCheck"] = True
		except:
			self.clearEverything()
			set_text("Err")
			operationDict["errCheck"] = True

	def squareRoot(self):
		try:
			curVal = float(entry.get())
			rootedVal = math.sqrt(curVal)
			entry.delete(0, tk.END)
			rootedVal = formatNumber(rootedVal)
			print(rootedVal)
			entry.insert(tk.END, rootedVal)
			operationDict["errCheck"] = True
		except:
			self.clearEverything()
			set_text("0")
			operationDict["errCheck"] = True

	def plusMinus(self):
		curVal = float(entry.get())
		curVal = curVal * -1
		entry.delete(0, tk.END)
		curVal = formatNumber(curVal)
		entry.insert(tk.END, curVal)

	def percent(self):
		if (not self.queueArr or operationDict["multiplication"] == True or operationDict["division"] == True):
			curVal = (float(entry.get())) / 100
			entry.delete(0, tk.END)
			curVal = formatNumber(curVal)
			print(curVal)
			entry.insert(tk.END, curVal)
		else:
			curVal = ((float(entry.get())) * self.queueArr[0]) / 100
			entry.delete(0, tk.END)
			curVal = formatNumber(curVal)
			print(curVal)
			entry.insert(tk.END, curVal)


obj = Operations()


class Button:		# creats instances for button values
	def __init__(self, value):
		self.value = value


zero = Button('0')
one = Button('1')
two = Button('2')
three = Button('3')
four = Button('4')
five = Button('5')
six = Button('6')
seven = Button('7')
eight = Button('8')
nine = Button('9')

pm = Button('+/-')
dec = Button('.')
plus = Button(' + ')
minus = Button(' - ')
div = Button(' ÷ ')
equal = Button('=')
back = Button('⌫')
mult = Button(' x ')
clearEntry = Button('CE')
clear = Button('C')
recip = Button('1/x')
square = Button('x^2')
sqrt = Button('2√x')
percent = Button('%')

root = tk.Tk()
root.title(TITLE)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backFrame = tk.Frame(root, bg='#485c75')
backFrame.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#bcc4cf')
frame.place(relx=0.05, rely=0.05, relheight=0.95, relwidth=0.9)

pad = tk.Frame(root)
pad.place(relx=0.1, rely=0.3, relheight=0.7, relwidth=0.8)

zeroVar = tk.Button(pad, text=zero.value, bg='#dceef5', command=lambda: set_text(zero.value))
zeroVar.place(relx=0.25, rely=(5/6), relheight=(1/6), relwidth=0.25)

oneVar = tk.Button(pad, text=one.value, bg='#dceef5', command=lambda: set_text(one.value))
oneVar.place(relx=0, rely=(4/6), relheight=(1/6), relwidth=0.25)

twoVar = tk.Button(pad, text=two.value, bg='#dceef5', command=lambda: set_text(two.value))
twoVar.place(relx=0.25, rely=(4/6), relheight=(1/6), relwidth=0.25)

threeVar = tk.Button(pad, text=three.value, bg='#dceef5', command=lambda: set_text(three.value))
threeVar.place(relx=0.5, rely=(4/6), relheight=(1/6), relwidth=0.25)

fourVar = tk.Button(pad, text=four.value, bg='#dceef5', command=lambda: set_text(four.value))
fourVar.place(relx=0, rely=(3/6), relheight=(1/6), relwidth=0.25)

fiveVar = tk.Button(pad, text=five.value, bg='#dceef5', command=lambda: set_text(five.value))
fiveVar.place(relx=0.25, rely=(3/6), relheight=(1/6), relwidth=0.25)

sixVar = tk.Button(pad, text=six.value, bg='#dceef5', command=lambda: set_text(six.value))
sixVar.place(relx=0.5, rely=(3/6), relheight=(1/6), relwidth=0.25)

sevenVar = tk.Button(pad, text=seven.value, bg='#dceef5', command=lambda: set_text(seven.value))
sevenVar.place(relx=0, rely=(2/6), relheight=(1/6), relwidth=0.25)

eightVar = tk.Button(pad, text=eight.value, bg='#dceef5', command=lambda: set_text(eight.value))
eightVar.place(relx=0.25, rely=(2/6), relheight=(1/6), relwidth=0.25)

nineVar = tk.Button(pad, text=nine.value, bg='#dceef5', command=lambda: set_text(nine.value))
nineVar.place(relx=0.5, rely=(2/6), relheight=(1/6), relwidth=0.25)

plusMinus = tk.Button(pad, text=pm.value, bg='#dceef5', command=lambda: obj.plusMinus())
plusMinus.place(relx=0, rely=(5/6), relheight=(1/6), relwidth=0.25)

plusVar = tk.Button(pad, text=plus.value, bg='#b1bfc4', command=lambda: obj.addition())
plusVar.place(relx=0.75, rely=(4/6), relheight=(1/6), relwidth=0.25)

minusVar = tk.Button(pad, text=minus.value, bg='#b1bfc4', command=lambda: obj.subtraction())
minusVar.place(relx=0.75, rely=(3/6), relheight=(1/6), relwidth=0.25)

equalVar = tk.Button(pad, text=equal.value, bg='#89bad9', command=lambda: obj.equalPressed())
equalVar.place(relx=0.75, rely=(5/6), relheight=(1/6), relwidth=0.25)

backspaceVar = tk.Button(pad, text=back.value, bg='#b1bfc4', command=lambda: obj.backSpace())
backspaceVar.place(relx=0.75, rely=(0/6), relheight=(1/6), relwidth=0.25)

decimalVar = tk.Button(pad, text=dec.value, bg='#dceef5', command=lambda: set_text(dec.value))
decimalVar.place(relx=0.5, rely=(5/6), relheight=(1/6), relwidth=0.25)

divisionVar = tk.Button(pad, text=div.value, bg='#b1bfc4', command=lambda: obj.division())
divisionVar.place(relx=0.75, rely=(1/6), relheight=(1/6), relwidth=0.25)

multVar = tk.Button(pad, text=mult.value, bg='#b1bfc4', command=lambda: obj.multiplication())
multVar.place(relx=0.75, rely=(2/6), relheight=(1/6), relwidth=0.25)

percVar = tk.Button(pad, text=percent.value, bg='#b1bfc4', command=lambda: obj.percent())
percVar.place(relx=0, rely=(0/6), relheight=(1/6), relwidth=0.25)

ceVar = tk.Button(pad, text=clearEntry.value, bg='#b1bfc4', command=lambda: obj.clearCurrentEntry())
ceVar.place(relx=0.25, rely=(0/6), relheight=(1/6), relwidth=0.25)

cVar = tk.Button(pad, text=clear.value, bg='#b1bfc4', command=lambda: obj.clearEverything())
cVar.place(relx=0.5, rely=(0/6), relheight=(1/6), relwidth=0.25)

squareVar = tk.Button(pad, text=square.value, bg='#b1bfc4', command=lambda: obj.square())
squareVar.place(relx=0.25, rely=(1/6), relheight=(1/6), relwidth=0.25)

recipVar = tk.Button(pad, text=recip.value, bg='#b1bfc4', command=lambda: obj.reciprocal())
recipVar.place(relx=0, rely=(1/6), relheight=(1/6), relwidth=0.25)

sqrtVar = tk.Button(pad, text=sqrt.value, bg='#b1bfc4', command=lambda: obj.squareRoot())
sqrtVar.place(relx=0.5, rely=(1/6), relheight=(1/6), relwidth=0.25)

entry = tk.Entry(root, font="Calibri 32")
entry.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.8)

set_text("0")	# sets default value when app is ran

root.mainloop()