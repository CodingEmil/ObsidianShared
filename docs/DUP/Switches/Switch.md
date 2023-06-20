>[!info] 
>- Layer 1 und 2
>- gibt auch Layer 3 Switches (Multilayerswitches) 
>- parallele Übertragung (Gegensatz zum Hub)

An einem Switch werden alle Netzwerkgeräte angeschlossen, auch andere Switches. Der Switch erzeugt eine [[Topologie|Sterntopologie]].
Der Switch schaltet Datenverkehr anhand von Ziel-MAC-Adressen (im Ethernetframe).
Bekommt er einen Frame, wo er die Ziel-MAC-Adresse nicht kennt, dann schickt er ihn an alle Ports (Flooding).

#### MAC-Address-Table
Der Switch hat eine Source-Address-Table (SAT), in welcher er sich merkt, welche MAC-Adresse, an welchem Port ist.
![[Pasted image 20230620154433.png| 400]]
Diese Tabelle kann man auch selber konfigurieren (Typ: static), allerdings lernt der Switch dies auch von selber, nach Zeit (Typ: dynamic).
Dazu liest er die Source-MAC-Adresse ein und schreibt diese in die Tabelle, zu dem Port, wo er den Frame erhalten hat.

#### Kaskadierung - Verbinden mehrerer Switches
Wenn wir mehrere Switches miteinander verbinden, dann ist das Kaskadierung.
Das kann man ohne Probleme machen, allerdings sollte man einen schnelleren Port als Verbindung wählen, da schließlich der ganze Traffic von einem Switch auf einen Port, des anderen Switches, geht. Oft haben Switches dazu SFP-Ports (Small Form-factor Pluggable) und SFP-Module, wodurch man auch Glasfaser nutzen kann.

#### Managed und Unmanaged Switches
Oft reicht ein unmanaged Switch, also ein Switch bei dem man nicht über ein Konsolenkabel in eine Konsole kommt. Hier kann man dann aber natürlich auch keine VLANs erstellen.
Managed Switches haben eine Konfigurationsschnittstelle (Konsolen Port), worüber man diese konfigurieren kann.