### 1) Allgemeine Fragen zu Subnetzmasken
PC: 
192.168.10.10
255.255.255.0

Server:
192.168.14.10
255.255.255.0

Ersichtlich, dass beide Geräte nicht im gleichen Netz sind. 

a) <u>Subnetzmaske in Binär:</u> `11111111 11111111 11111111 00000000`

b) <u>Netzadresse des PCs:</u> 192.168.10.0

c) <u>Broadcastadresse des PC Netzes:</u> 192.168.10.255

d) <u>Anzahl der Hosts:</u> 254 Hosts

c) Server und Client können nicht ohne Router kommunizieren, das sie in unterschiedlichen Netzen sind.

#### Neue Subnetzmaske des PCs
PC:
192.168.10.10
255.255.0.0

f) <u>Netzadresse:</u> 192.168.0.0

  <u>Broadcastadresse:</u> 192.168.255.255
  
g) <u>Anzahl der Hosts:</u> 65534 Hosts

h) Server und Client können nicht miteinander kommunizieren, da sie sich immer noch in verschiedenen Subnetzen befinden.

#### Neue Subnetzmaske des PCs
PC:
192.168.10.10
255.255.128.0

i) <u>Subnetzmaske in Binär:</u> `11111111 11111111 10000000 00000000`

j) <u>Netzadresse des Netzes:</u> 192.168.0.0

k) <u>Broadcastadresse des Netzes:</u> 192.168.127.255

l) Die Geräte können auch nicht kommunizieren, da sie wieder in unterschiedlichen Subnetzen sind.

### 2) Unterteilung eines IP-Bereiches in verschiedene Subnetze
d) Unser gegebener IP-Adressbereich fängt bei 192.170.0.0 an.

192.170.0.0/19

<--> *Netz A*

192.170.32.0/19

<--> *Netz B*

192.170.64.0/19

<--> *Netz C*

192.170.96.0/19

<--> *Netz D*

192.170.128.0

![[Pasted image 20230706192720.png]]

### 3) Ergänzende Aufgaben zum Subnetting
a) <u>Netzadressen im 255.255.255.224 Netz:</u> 0, 32, 64, $\color{red}96$, 128, 160, ...

Beide PCs sind im 4ten Subnetz (192.168.222.96/27 ($\color{red}192.168.222.96-192.168.222.127$))

b) <u>Netzadressen im 255.255.255.240:</u> 0, $\color{violet}16$, $\color{green}32$, 48, ...

PC1 ist im 2ten Subnetz und PC2 im 3ten, somit sind sie in unterschiedlichen Subnetzen.

### 4) VLANs
a) 
- IP-Adressen + Subnetzmaske an ==Subinterfaces== vergeben
- 
- Encapsulation: Zuordnung von Subinterface zu VLAN-ID
- 
- Falls DHCP-Relay genutzt werden soll: Helper-Adresse konfigurieren
- 
- Interface einschalten

b)
![[Pasted image 20230705164300.png]]
![[Pasted image 20230705164243.png]]
Die beiden Gigabitverbindungen sind zwar im trunk mode, allerdings sind nur VLANs von 20-1001 erlaubt, wodurch VLAN 10 nicht weitergegeben wird. So kann VLAN 10 auch nicht über die Switches kommunizieren.

### 5) Statisches Routing zwischen zwei Subnetzen
![[Pasted image 20230706135552.png]]
![[Pasted image 20230706135620.png]]
### 11)
![[Pasted image 20230706142009.png]]
### 13)
![[Pasted image 20230706140513.png]]
### 15)
![[Pasted image 20230706185311.png]]

### 16)
- Ein möglicher Fehler ist, dass in diesem Host, keine ==Gateway-IP== vergeben wird und dieser somit nicht der Router findet. 
- 
	  Dazu könnte man sich einfach der Netzwerkkonfigurationen auf dem Host anschauen und gucken, ob die richtige bzw. überhaupt eine Gateway IP vergeben wurde.
	  
- ==Firewall:== Blockierte Ports/IPs
- 
		Dazu muss man sich die Firewall-settings anschauen
### 17)
![[Pasted image 20230706142518.png]]
