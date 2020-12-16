# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:08:18 2020

@author: nyunu
"""
import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library

tempC= []
ser = serial.Serial('COM3', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

    

while True: # While loop that loops forever
    while (ser.inWaiting()==0): #Wait here until there is data
        pass #do nothing
  #  arduinoString = arduinoData.readline() #read the line of text from the serial port
   # dataArray = arduinoString.split(r',')   #Split it into an array called dataArray
   
    data = ser.readline().decode("utf -8") # read lines
    dataArray = data . split (',')
    temp = dataArray[0]        #Convert first element to floating number and put in temp
    
    tempC.append(temp)                    #Build our tempC array by appending temp readings
    sorted(tempC)                    
    plt.ylabel('Temp C')
    
    plt.plot(tempC, 'ro-', label='Degrees C')       #plot the temperature live graph
                                
    plt.legend(loc='upper left')
    plt.title('Real-Time Degree C Plotting via Temperature Sensor')
    plt.grid(True) 
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>10):                            #If you have 10 or more points, delete the first one from the array
        tempC.pop(0)                       #This allows us to just see the last 10 data points
    
serial.close()