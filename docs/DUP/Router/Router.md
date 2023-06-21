!!! note
    Arbeitet auf Layer 3

Verschiedene Netzwerke werden über Router miteinander verbunden. Ein Router arbeitet auf Layer 3, kommuniziert also mit IP-Adressen.

#### Default-Gateway
Ein Beispiel für ein Default Gateway ist der Router, der mit dem lokalen Netzwerk verbunden ist und die Verbindung zum Internet herstellt. Wenn ein Gerät im lokalen Netzwerk eine Anfrage an eine externe IP-Adresse sendet, wird die Anfrage an das Default Gateway (den Router) weitergeleitet. Der Router leitet dann die Anfrage an das externe Netzwerk weiter und ermöglicht so den Zugriff auf Ressourcen außerhalb des lokalen Netzwerks, wie z.B. das Surfen im Internet.

#### Adressierung von Paketen
Haben wir Pakete im lokalen Netz, dann ist die Ziel-MAC und Ziel-IP von dem gleichen Gerät.
Gehen wir aber nun aus unserem Netzwerk hinaus, über den Router, dann ist die Ziel-IP, die von dem eigentlichen Ziel (z.B. Website) und die Ziel-MAC, die von unserem Router.

!!! note "IP-Adresse"
    Gibt das endgültige Ziel an, den ein Paket erreichen soll (Ende-zu-Ende)

!!! note "MAC-Adresse"
    Gibt den nächsten Host an, den ein Paket erreichen soll (Punkt-zu-Punkt)

!!! note
    Test 22


