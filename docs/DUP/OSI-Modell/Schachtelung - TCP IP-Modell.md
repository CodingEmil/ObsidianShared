Schachteln ist das Verpacken von Paketen höherer Schichten in Pakete niedriger Schichten.
Streng genommen ist das unten abgebildete Modell nicht das OSI-Modell, sondern das **DoD-Schichtenmodell oder TCP/IP-Modell**.
![[Pasted image 20230620122613.png| center | 400]]
In diesem Modell wird visualisiert, wie das Internet funktioniert.
Wir haben irgendwelche Nutzdaten auf der ==**Applikationsschicht**==. Diese wollen wir nun an einen Computer, irgendwo im Internet, senden. 
Dazu kommen die Nutzdaten in die unterliegende Schicht, ==**Transportschicht**==, wo sie einen TCP-Header bekommen. Hier wird zum Beispiel TCP oder UDP genutzt. Im Beispiel von TCP wird hier sichergestellt, dass die Datenpakete in der richtigen Reihenfolge ankommen und Fehler korrigiert werden.
Nun kommen die Daten in die ==**Internetschicht**==, hier sind also alle Daten, welcher zuvor hinzugefügt wurden. An diese Daten kommt jetzt noch ein IP-Header. Die Internetschicht ist für die Weiterleitung von Daten, über verschiedenen Netzwerke, zuständig. Dazu wird oft das IP-Protokoll genutzt.
Zuletzt kommen all diese Daten in die ==**Netzzugangsschicht**==, welche sich darum kümmert, dass die Datenpakete in ein Format kommen, welches für die Übertragung über ein physikalisches Medium geeignet ist (z.B. in Bits
