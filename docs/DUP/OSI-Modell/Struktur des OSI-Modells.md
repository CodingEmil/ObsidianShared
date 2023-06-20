Wir haben Millionen von verschiedenen Endgeräten in unseren Netzen, aber irgendwie muss schließlich regeln, wie diese miteinander kommunizieren. Das macht man mit dem OSI-Modell. Dieses gibt eine Struktur an.
Das Modell ist aus **7 Schichten** aufgebaut, wobei 1-4 als "*Transportschichten*" und 5-7 als "*Anwendungsschichten*" bezeichnet werden. 
Die **Transportschichten** haben die Aufgabe Daten von einem Gerät zum anderen zu übertragen und die **Anwendungsschichten** den Inhalt im Betriebssystem und den Applikationen zu verteilen.

#### 1. (Bitübertragungsschicht, Physical-Layer)
- nur Hardware
Hardware wie Leitungstypen, Steckerverbinder und Medien (WLAN, Kupfer oder Glas)

#### 2.(Sicherungsschicht, Data Link Layer)
- Punkt-zu-Punkt
- Fehlererkennung (CRC)
- Zugriffssteuerung auf physische Medien
Hat die Aufgabe eine einen zuverlässigen Datenfluss zwischen dem nächsten Netzwerkgerät herzustellen (Punkt-zu-Punkt).

#### 3. (Vermittlungsschicht, Network Layer)
- Ende-zu-Ende
- logische Adressierung
- Routing
Stellt sicher, dass das Ziel über mehrere Daten erreicht wird (Ende-zu-Ende). Wie Daten ihren Weg, durch/s Netzwerk/e zu finden.