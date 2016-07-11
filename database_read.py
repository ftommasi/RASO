import os
from time import *
from send_email import *

#directory_path = "/home/nmerc54/Documents/Python_Files/Email_Writer/_event_database/"
directory_path = '_event_database/'
data_file = 'data.txt'
address = "nick.fausto.pi@gmail.com"


try:
   database = open(data_file)
   for line in database:
      if line.strip() == "EventFlag":
         #sendemail code goes here
         print "Email sent!"
      else:
         print "No flags raised. No action taken"
   database.close()
   os.rename(data_file,"READ"+data_file) #Mark the file as read
   
   
except IOError:
   print "Data not found"


