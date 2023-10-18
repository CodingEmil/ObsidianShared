### Servo + Poti
```C
#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int potpin = A0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin

void setup() {
  myservo.attach(9);  // dem Arduino sagen, wo der Servo angeschlossen ist
}

void loop() {
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 180);     // Poti gibt Wert von 0 <-> 1023, skalieren auf <-> 180 für Servosteuerung
  myservo.write(val);                  
  delay(15);                           // waits for the servo to get there
}
```

### eingebaute LED
```C
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```

### Serielle Schnittstelle
```C
void setup(){
  Serial.begin(9600); //9600 (Baudrate) Datenbits pro Sekunde
}

void loop() {
  Serial.println("Hello");
  delay(1);
}
```

### Taster
```C
const int buttonPin = 2;
int buttonState = 0;

void setup(){
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  
}

void loop(){
  buttonState = digitalRead(buttonPin);
  
  if (buttonState == HIGH){
    Serial.println("Taster wurde gedrückt");
  }
  
}
```


### Analogwerte einlesen
```C
int sensorPin = A0; //Pin wo der Sensor angeschlossen ist
int sensorValue = 0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
}
```

### LCD-Display
```C
#include <Wire.h>  // Einbinden der Wire-Bibliothek für die I2C-Kommunikation
#include <rgb_lcd.h>  // Einbinden der rgb_lcd-Bibliothek

// Initialisieren des LCD-Objekts
rgb_lcd lcd;

void setup() {
  lcd.begin(16, 2);  // Initialisieren des LCD mit 16 Zeichen und 2 Zeilen
  lcd.setRGB(255, 0, 0);  // Hintergrundbeleuchtung auf Rot setzen

  // Anzeigen einer Begrüßungsnachricht
  lcd.print("Hallo,");
  lcd.setCursor(0, 1);
  lcd.print("Arduino!");
}

void loop() {
  // Hier können Sie kontinuierlich aktualisierte Informationen auf dem Display anzeigen.
}

```

