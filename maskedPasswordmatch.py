# This is a simple script to mask a password whilst inputing a password twice.
# getpass is a module for working with passwords in python. Please check Python.org for more information.
# The password will not show at a terminal window but will show in IDLE with a warning when editing. 
# Will error if input is not an exact match
# a snippet script to help Network Engineers.
# feel free to use and share. Amend to suit your needs.
# written by NetworkCorner


import getpass

while True:
      secretP = getpass.getpass(prompt="Please input User MSSOPS password: ")
      print('****Password Masked****' + "\r\n")

      secretP2 = getpass.getpass(prompt="Please input same MSSOPS password again: ")
      print('****Password Masked****' + "\r\n")

      if secretP == secretP2:
          break 
      else:
          print('Error!!! ***Password doesnt Match****')

print("password match script has run")
print('your password is ', secretP)
