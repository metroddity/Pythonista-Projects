import ui
import os

#this is the initial value of the gift card, in my case I had an initial $217 balance.
originalSum = 217.00

#creates a text file to store the changing amounts, that way the amount does not revert to the initial value when the program is run later.
try:
	with open('.giftcard.txt') as f:
		originalSum = float((f.read()))
except IOError:
	pass

#changes the initial value by the amount entered, no need to indicate negative numbers, a negative number will increase the remaining balance instead of reducing it.
def purchaseAction(self):
	global originalSum
	purchase = v['textfield1'].text
	originalSum -= float(purchase)
	v['textview1'].text = str(originalSum)
	with open('.giftcard.txt', 'w') as f:
		f.write(str(originalSum))

v = ui.load_view()
#shows the remaining balance immediately after entering a purchase. 
v['textview1'].text = str(originalSum)
v.present('sheet')