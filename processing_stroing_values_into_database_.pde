import processing.serial.*;

import processing.serial.*;
import cc.arduino.*;
import de.bezier.data.sql.*;
Serial myPort;
Arduino arduino;
MySQL db;


//int pinTemp = 1;
String data;

void setup()
{
  //arduino = new Arduino(this, Serial.list()[0],9600);
  //arduino.pinMode(pinTemp, Arduino.INPUT);
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 9600);
  String user = "root";
  String pass = "";
  String database = "temperaturesensordata";


  db = new MySQL(this, "localhost", database , user , pass);
}

void draw()
{
  data = myPort.readString(); // read the value 

  println(data);
  
  if ( db.connect() )
  {
    db.execute("INSERT INTO `temperaturesensordata`.`tempsensing` (`Temperature`) VALUES ('" + data + "');");
    }
    
  else
{
    println("Error in the connection :-( ");
}

    delay(1000); // Wait 1 minutes
}
