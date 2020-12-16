#define TEMPERATURE A0
#define fan 3
#define led 12
void setup(){
  Serial.begin(9600);
  pinMode(fan, OUTPUT);
  pinMode(led, OUTPUT); 
}



void loop(){
  float temp = analogRead(TEMPERATURE);    //Read the analog pin
  temp = temp * 0.48828125;   // convert output (mv) to readable celcius
 
  Serial.print(temp);
   //print the temperature status
   Serial.print('\n');
   delay(1000);  


     if (temp<=24){
      analogWrite(fan, 511);
      //lcd.print("Fan Speed: 20 %");
      delay(1000);
     // lcd.clear();
    }
    else if (temp<=26 && temp>24){
      analogWrite(fan,101);
      //lcd.print("Fan Speed: 40 %");
      delay(1000);
      //lcd.clear();
    }
     else if (temp<=30 && temp>26){
      digitalWrite(led,HIGH);
      analogWrite(fan,151);
     // lcd.print("Fan Speed: 60 %");
      delay(1000);
     // lcd.clear();
    }
    else if (temp>30){
      analogWrite(fan,255);
     // lcd.print("Fan Speed: 100 %");
      delay(2000);
     // lcd.clear();
    }
}
