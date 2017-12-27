import ui
import random

def powerBall():
	#highest number that can be selected for the white balls
	to = 69
	#highest number that can be selected for the red balls
	powerball = 26
	#amount of white balls i.e. numbers
	numbers = 5
	
	#selects 5 numbers from 1 to 69 at random and saves them in a variable
	numbersPick = random.sample(list(range(1, to+1)), numbers)
	#selects 1 powerball number from 1 to 26 at random and saves it in a variable
	powerballPick = random.sample(list(range(1,powerball+1)),1)
	#the function returns a string consisting of the 5 white numbers plus the powerball from the previously mentioned variables
	return str(sorted(numbersPick)+ powerballPick)

def megaMillions():
	#same process as the powerball function but with different ranges for the white numbers and mega number
	to = 75
	mega = 15
	numbers = 5
	
	numbersPick = random.sample(list(range(1, to+1)), numbers)
	megaPick = random.sample(list(range(1,mega+1)),1)
	return str(sorted(numbersPick)+ megaPick)

def segment_action(sender):
	#allows for choosing which function to run when the button is pressed
	if v['segmentedcontrol1'].selected_index == 0:
		v['textview1'].text = powerBall()
	elif v['segmentedcontrol1'].selected_index == 1:
		v['textview1'].text = megaMillions()


v = ui.load_view()
v.present('full_screen')
