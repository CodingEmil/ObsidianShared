ARP ermöglicht die Zuordnung von IP Adressen zu MAC-Adressen.
Die Hauptfunktion in ARP besteht darin, die MAC-Adresse einer bekannten IP-Adresse zu ermitteln. Denn ohne der MAC-Adresse, können keine Daten zu einem anderen Gerät übertragen werden.

1. Hosts sendet **ARP-Request** mit FF-FF-FF-FF-FF-FF. Jedes Gerät kriegt dieses Paket.  
2. In dem Ethernet-Frame steht nun die gesuchte IP.  
3. Wird der Hosts, mit dieser IP, gefunden, schickt er eine **ARP-Replay**.

#### ARP-Table
Jeder Host hat eine ARP-Tabelle, in welcher IP-Adressen zu MAC-Adressen zugeordnet sind.
![[Pasted image 20230620151739.png]]
Wie wir sehen, haben wir einige statische Adressen, das sind z.B. Broadcast Adressen (192.168.0.255) oder auch Multicast Adressen (224.0....).
Dynamische Einträge verfallen nach einer Zeit.

##### Fehlender Eintrag
Fehlt eine IP in der ARP-Tabelle, dann löst ARP eine ARP-Request aus, welches ein Paket an (FF:FF:FF:FF:FF:FF Broadcast Adresse in Layer 2) an alle Geräte im Netz schickt. Nun überprüfen alle Hosts in dem Netzwerk, ob sie die Adresse haben und falls ja, antwortet dieser Host und trägt die eigene MAC Adresse in den Ethernet-Frame ein. Die Ziel-Adresse ist entweder wieder die Broadcast Adresse, oder die des Hosts, der die Request geschickt hat. 
Beim Empfang wird die MAC-Adresse in die Tabelle eingetragen.
