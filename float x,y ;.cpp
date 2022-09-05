float x,y ;
const int pingPin = 7;

int red=11;
int blue=10;
int green=9;

void setup ()
{
  pinMode( 8, INPUT);
  pinMode( 5, OUTPUT);
  pinMode( A5, INPUT);
 
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);
  Serial.begin(9600);
}
void loop ()
{
  x= digitalRead(8);
  y= analogRead(A5);
  //Serial.println(x);
  //Serial.println(y);
  if ( (x>0) && (y<550))
  { 
    digitalWrite(5, HIGH);
    Serial.println("Bulb ON");
    delay (5000);
  }
  else
    digitalWrite(5, 0);
    Serial.println("Bulb OFF :)");
  
  
  long duration, inches, cm;

  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  
  inches = microsecondsToInches(duration);
  cm = microsecondsToCentimeters(duration);
  if(inches<20)
  {
    digitalWrite(red,HIGH);
    digitalWrite(green,LOW);
	digitalWrite(blue,LOW);
    //Serial.println (" DOOR OPEN ");
     
  	//Serial.println(inches);
  }
  if(inches>70)
  {
    digitalWrite(red,LOW);
    digitalWrite(green,HIGH);
	digitalWrite(blue,LOW);
  }
  if(inches>20 && inches<70)
  {
    digitalWrite(red,LOW);
    digitalWrite(green,LOW);
	digitalWrite(blue,HIGH);
  }

  Serial.print("Distance- ");
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();

  delay(100);
}

long microsecondsToInches(long microseconds) {  
  return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
  
}