import os
from time import *
from random import *

#directory_path = '/home/nmerc54/Documents/Python_Files/Email_Writer/_event_database/'
directory_path = '_event_database/'
picture_file = directory_path + 'test.jpg'
data_file = directory_path + 'data.txt'

try:
   while True:
      if choice([1,2,3,4,5]) == 1 :
         
         temp_file = open(data_file, 'w+')
         
         if choice([1,2,3]) == 1:
            temp_file.write("Event Flag\n\n")

         current     = 40.2 + uniform(-20.0, 20.0)
         voltage     = 7.30 + uniform(-3.0 , 3.0 )
         temperature = 29.4 + uniform(-20.0, 20.0)

         temp_file.write("Current:     " + str(current) + " mA\n")
         temp_file.write("Voltage:     " + str(voltage) + " V\n")
         temp_file.write("Temperature: " + str(temperature) + " C\n")
         temp_file.write("Timestamp:   " + strftime("%H:%M:%S") )

         # more code
         # Simulate the pi inputs
         temp_file.close()
         
         print("Reported")

      sleep(0.75)
except KeyboardInterrupt:
   pass

