- Digitale Thermostatventilsteuerung
- 2 Boards: 
	- ATmega328P (auf Seeeduino V4-Board (rot))
	- ARM Cortex M0 (auf einem Arduino Due (grün))
- Erweitern mit Sensoren/Aktoren durch Grove-Starter Kit

!!! note
    title: Eingangsspannung
- Rotes Board -> 5V
- Grünes Board -> 3,3V


### Durchführung
1. IDE laden, verschieben und Ausführungsberechtigungen verteilen
```
cd ~/Downloads
wget https://downloads.arduino.cc/arduino-ide/arduino-ide_2.0.0_Linux_64bit.zip
unzip arduino-ide_2.0.0_Linux_64bit.zip
mv arduino-ide_2.0.0_Linux_64bit ~/arduino-ide
chmod +x ~/arduino-ide/arduino-ide
```
2. ==starten der IDE==
```
~/arduino-ide/arduino-ide
```
#### Konfiguration der IDE
1. Sketchbook location
`File->Preferences->Sketchbook location`
2. Arduino Due und Seeeduino über Board Manager installieren
	1. Rotes Board muss eingebunden werden:
		1. `https://raw.githubusercontent.com/Seeed-Studio/Seeed_Platform/master/package_legacy_seeeduino_boards_index.json`
3. Bibliotheken hinzufügen
	1. `Grove - LCD RGB Backlight` und `Servo by Michael Margolis, Arduino` 

#### Programm
Es soll ein Programm entworfen werden, welches folgende Komponenten ansteuern kann:
- Eingebaute LED
- serielle Schnittstelle über USB zum PC
- Taster
- Potentiometer
- Servo
- Temperatursensor
- LCDisplay