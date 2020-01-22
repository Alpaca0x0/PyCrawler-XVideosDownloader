# -*- coding: utf-8 -*
import time
import sys

def auto_load(bar_width=40):
	# setup toolbar
	sys.stdout.write(u"\u250b"+"%s"+u"\u250b" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line

	for i in range(bar_width):
	    time.sleep(0.1) # do real work here
	    # update the bar
	    sys.stdout.write(u"\u2588")
	    sys.stdout.flush()

	sys.stdout.write(u"\u250b"+"\n") # this ends the progress bar

def create_bar(bar_width=40,bar_text=''):
	sys.stdout.write(bar_text+u"\u250b"+(" " * bar_width)+u"\u250b")
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line
	
def load(bar_flow=1):
	sys.stdout.write(u"\u2588"*bar_flow)
	sys.stdout.flush()

def end_bar(bar_text=''):
	sys.stdout.write(u"\u250b"+"\n"+bar_text+"\n") # this ends the progress bar

def loading(now=100,tol=100,bar_width=100):
	rate=int((tol/now)*bar_width)
	sys.stdout.write(u"\u250b"+"%s"+u"\u250b" % (" " * bar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (bar_width+1)) # return to start of line
