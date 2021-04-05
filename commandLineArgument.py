# This is a simple script in which you put your arguments on the commandline.(Dos Prompt/Linux Prompt)
# Enter a name colour age 
#  
#  C:\Users\Laptop\Documents\Python_scripts>commandLineArgument.py joeblogs blue 99
#  Hello joeblogs blue 99
#
# 
# Will error if the wrong amount of arguments are not on the commandline.
# a snippet script to help Network Engineers.
# feel free to use and share. Amend to suit your needs.
# written by NetworkCorner

import sys

q1 = sys.argv[1] #input("what is your name ? :")
q2 = sys.argv[2] #input("what colour is the sky ? :")
q3 = sys.argv[3] #input("How old are you ? :")


print(" Hello" + " " + q1 + " " + q2 + " "  + q3 )
