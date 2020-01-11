import time
import sys


def auto_load(bar_width=40):
	# setup toolbar
	sys.stdout.write("[%s]" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line, after '['

	for i in range(bar_width):
	    time.sleep(0.1) # do real work here
	    # update the bar
	    sys.stdout.write("█")
	    sys.stdout.flush()

	sys.stdout.write("]\n") # this ends the progress bar

def create_bar(bar_width=40,bar_text=''):
	sys.stdout.write(bar_text+"[%s]" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line, after '['
	
def load(bar_flow=1):
	sys.stdout.write("█"*bar_flow)
	sys.stdout.flush()

def end_bar(bar_text=''):
	sys.stdout.write("]\n"+bar_text+"\n") # this ends the progress bar

def loading(now=100,tol=100,bar_width=100):
	rate=int((tol/now)*bar_width)
	sys.stdout.write("[%s]" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line, after '['
