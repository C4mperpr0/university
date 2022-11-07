g:ycm_enable_inlay_hints## Elektromechanische Gattermodelle
- Gattermodelle als Block Box, Transistormodell, TTL, CMOS
- elektromagnetische Relais
- Netz aus Relais, die gleichberechtigt schalten und durch externe Sensoren steuerbar sind.

## 1. Schritt
- Lediglich Verwendung von Schaltnetzen (ohne Speicher, Zähler, Register)
- Zuführung aller Bits auf Leitungen: Schalterreihen
- 3 Bit pro Operand
- 1 Bit für Operationen

## Rechenwerk mit Register
- Ausgang des Rechenwerkes wird im Register gespeichert und zum Eingang rückgekoppelt
- Zur Speicherung des Ergebnis wird ein Takt benötigt
- Weitere Steuerleitung für das Löschen des Registers

## 2. Befehle
### Steuerleitung
- 00: addiert
- 01 subtrahiert
- 10 löscht den Akku

### Assembler
- Add n -> 00nnn
- Sub M 01nnn
- CLA 10xxx

## 3. Vollständige Schaltung
- Verwendung von *aufgestapelten Registern* für die Ablage des Programmcodes
- Verwendung eines Zählers zur Ausführung der einzelnen Befehle
- negative Zahlen meist durch Zweier-Komplementdarstellung (es gibt auch einer Komplementdarstellung aber die hat 0 und -0 und ist deshalb kacke)

# Speicherhierachie
- CPU hat einen Cache (bei 4GHz sind das 250ps (picosek.) pro Befehl)
- RAM braucht ~30ns (nanosek.) (120 Mal langsamer) (RAM hat aber auch einen eigenen Cache zum optimieren)
- HDD oder SSD (sehr viel langsamer, hat auch einen eigenen Cache zum optimieren)

# jedes Programm besteht aus 5 Segmenten
- Text -> der Programmcode, in der Regel read only
- Daten (initialisiert -> Variablen wie in i=0;)
- Daten (nicht initialisiert) -> Variablen wie in data\[1000\];
- Stack -> Variablen innerhalb von Funktionen
- Heap -> für malloc oder neuen angeforderten Speicher

# Datenabstraktionen, Datentypen, Objecktorientierte Programmierung
- Spezielle Daten, auf die nur mit bestimmten Operationen zugegriffen werden können
- Mit Modula (Nachfolger von Pascal) wurden abstrakte Datentypen als Konzep eingeführt
- Stack: Push, Pop, Top
- Warteschlagen (Queue): Einfügen, Nächster
- Pascal basierte Strukturen (Records)

# Daten in Programmen
- Bezeichner
- Literale
