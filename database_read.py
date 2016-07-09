import os
from time import *
from send_email import *

#directory_path = "/home/nmerc54/Documents/Python_Files/Email_Writer/_event_database/"
directory_path = '_event_database/'
data_file = directory_path + 'data.txt'
address = "nick.fausto.pi@gmail.com"


try:
   while True:
      try:
         with open(data_file) as f:
            for line in f:
               if "Event Flag" in line:
                 # send_email(address, address, "Event flag raised", "Event: Discovered")
                  print line
               else:
                  print line
   
         print '---------------------'
         os.remove(data_file)
         sleep(1.0)
      except:
         True
except KeyboardInterrupt:
   pass


