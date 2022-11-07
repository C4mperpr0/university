### Wer hat Go erfunden
- von Robert Griesener, Rob Pike und Ken Tompson unter Google, 2009
- für Server und erffiziente parallele Prozesse

### Prozeduale Programmierung

### Strukturelle Programmierung

### Deklarieren
Zusweisen von Datentyp, reservierung von Speicher mit einem Namen
Bsp: *var i int* oder *i := 10* (wird automatisch zu int) 

### Definieren
Zuweisen eines Wertes einer Konstante oder Funktion
Bsp: *const pi = 3.14 

### Was ist der Unterschied zwischen "Compiletime" und "Run-Time"

### Zusammengesetzte Datentypen
- **Struct** *heterogen*
	- Beispiel: 3D-Vector: {x, y, z} oder Datum
	- Deklaration: *var point struct {x,y,z float64}*
	- Definition: *type PointStruct struct {x,y,z float64}*
- **Array** *homogen statisch*
- **Slice** *homogen dynamisch*
- **Maps** *Tabelle mit 2-Tupel*
