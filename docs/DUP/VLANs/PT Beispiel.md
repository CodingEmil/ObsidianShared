[[https://github.com/CodingEmil/ObsidianShared/blob/main/docs/DUP/VLANs/attachments/PT_VLAN.pkt]]

	[]

![[Pasted image 20230706170728.png]]

## Kommunikation innerhalb der VLANs
Um eine Kommunikation innerhalb der VLANs zu ermöglichen (also nicht VLAN zu VLAN):
#### 1. VLAN Datenbank (Switch)
Die jeweiligen VLANs hinzufügen![[Pasted image 20230706170934.png]]
![[Pasted image 20230706183114.png]]

#### 2. VLAN Ports zuweisen (Switch)
Den einzelnen Ports ein VLAN zuweisen:
	Hier Access Mode, da wir nur ein VLAN an einem Port haben. Das natürlich für alle Ports machen, an dem VLANs sind. In dem Beispiel wären das 4, pro Switch 2.
![[Pasted image 20230706171059.png]]
![[Pasted image 20230706183158.png]]

#### 3. Trunk Mode zwischen Switches
Zuletzt noch erlauben, dass die VLAN von einem zum anderen Switch übertragen werden können:
	Dazu müssen beide Interfaces, zwischen den Switches, im Trunk Mode sein und min. VLAN 10 und VLAN 20 erlauben 
![[Pasted image 20230706171314.png]]
![[Pasted image 20230706183236.png]]
Jetzt sind die VLANs in der Lage untereinander zu kommunizieren.

## Kommunikation zwischen VLANs
Wenn wir zwischen zwei VLANs kommunizieren wollen, dann brauchen wir einen Router. In diesem Router müssen wir nun Subinterfaces erstellen. Das bedeutet, dass wir unser Interface, an dem der Switch liegt, in mehrere Interfaces aufteilen (diese sind natürlich dann nur virtuell). 

#### 1.Subinterfaces (Router)
Mit `interface FastEthernet 0/0.1` erstellen wir z.B. schon ein Subinterface. 
Jetzt weisen wir diesem Subinterface ein VLAN zu:
![[Pasted image 20230706173342.png]]
Somit ist VLAN 10 nun dem Subinterface 0.1 zugewiesen. Dieses Subinterface bracht natürlich noch einen IP, welche das Default-Gateway für die Gerät im VLAN 10 ist.
![[Pasted image 20230706173512.png]]
Pro VLAN erstellen wir ein Subinterface, das heißt wir haben hier zwei Subinterfaces. Diese werden analog zueinander erstellt. 
So sollte unsere Config aussehen:
![[Pasted image 20230706173632.png]]

#### 2. Trunk Mode von Switch zu Router
Damit unsere VLANs nun auch deren Gateway (den Router, bzw. Subinterfaces) erreichen können, müssen wir natürlich den Port des Switches, zum Router, in Trunkmode setzen und beide VLANs erlauben.
![[Pasted image 20230706173932.png]]
![[Pasted image 20230706183330.png]]

#### 3. Gateway 
Zuletzt muss jeder Host die Gateway Adresse (IP der Subinterfaces) haben.
Jetzt können die Geräte VLAN übergreifend kommunizieren.