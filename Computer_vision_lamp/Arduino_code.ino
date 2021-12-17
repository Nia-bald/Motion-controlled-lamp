#include <Servo.h>

Servo serX;
Servo serY;
String serialData;


void setup() {
  serX.attach(9); //attaches variable to pin 10
  serY.attach(6); //attaches varaible to pin 11
  Serial.begin(9600); // rate at which information gets transferred in a communication channel
  //what is serial communication : sending data one bit at a time
  //9600 baud implies, it transferrs 9600 bits per second
  Serial.setTimeout(10); //to reduce delay
}


void loop() {
  //r
}
//what is event listenter?
// a particular function or programme that waits for a certain event to occur

void serialEvent(){
  serialData = Serial.readString();
  //what is the serial connection connected to?
  //I am guessing Serial.readstring() returns some string like "X100Y90"
  //but where does it read it from?
  serX.write(parseDataX(serialData));
  serY.write(parseDataY(serialData));
}

// I believe below function gets the X value as integer from string "X100Y90"

int parseDataX(String data){
  data.remove(data.indexOf("Y")); 
  data.remove(data.indexOf("X"), 1); 

  //data.remove removes every character starting from the character with index = first argument
  //second argument tells, how many characters to remove, if it left empty it will remove every character

  
  return data.toInt();

}

int parseDataY(String data){

  data.remove(0, data.indexOf("Y")+1);

  return data.toInt();
  
}
