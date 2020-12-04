# This is a simple script to help make a Data Centre Selection
# will error if input is not an exact match
# a snippet script to help Network Engineers.
# feel feel to use and share amend to suit your needs
# written by NetworkCorner

DataCenter = {'DC1': '  1.1.1.1', 'DC2':'  2.2.2.2', 'DC3':'  3.3.3.3','DC4':'  4.4.4.4',
          'DC5':'  5.5.5.5', 'DC6':'  6.6.6.6', 'DC7':'  7.7.7.7', 'DC8':'  8.8.8.8', 'DC9':'  9.9.9.9'} 
for k, v in DataCenter.items():
      print(k + ' ' + v)


while True:
      DC_SELECT = input('Please Enter the Data Center and press enter eg. DC1  :')
      if DC_SELECT in DataCenter :
            print(DC_SELECT + ' location  chosen with IP' + DataCenter[DC_SELECT])
            break
      else:
            print('Error !!!!  invalid choice!!!! Try Again or press q to quit')
