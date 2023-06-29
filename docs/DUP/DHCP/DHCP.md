Ein DHCP-Server vergibt automatisch IP-Adressen, aus festgelegten Adress-Pools, an Netzwerkteilnehmer. Dabei wird die Host-IP und Standardgateway (optional: Subnetzmaske, DNS-Server, TFTP-Server) übergeben.

1. **DHCP-Discover**
	Der Host, welcher eine IP braucht, schickt ein Anfrage ins Netz, mit der Suche nach einem DHCP-Server.
2. **DHCP-Offer**
	Der DHCP-Server sucht eine Adresse aus dem Pool aus und broadcastet, dass er diese IP vergeben könnte.
3. **DHCP-Request**
	Host broadcastet, dass er die IP nimmt.
4. **DHCP-Acknowledge**
	DHCP-Server broadcastet eine Bestätigung.

![[dhcp.png]]

#### Lease-Time
Die Lease-Time ist die Zeit, wie lange ein Host die gleiche IP-Adressen, von dem DHCP-Server, bekommt. Steht hier 2 Monate, dann würde der Host erst nach 2 Monaten eine neue IP Adresse bekommen.
Diese Zeit kann man im DHCP-Server konfigurieren.

