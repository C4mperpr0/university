#Relationen #Restklassen #Modulo

## Relationen
Eine Relation R auf M x N ist eine Teilmenge R --c mit strich drunter-- M x N und damit eine Menge von Paaren. Im Falle M = N spricht man auch von Relationen über M. Statt (a, b) Element R schreibe man auch a Rb - und lies: "R gilt zwischen a und b" bzw "a steht (mittels R) in Relation zu b".
U.U. wird auf die explizite Angabe von M und N verzichtet, so dass eine Relation als eine Menge von Paaren dargestellt wird, nämilch als die Menge von Paaren, für die die Relation erfüllt/wahr ist.

### Beispiel für Relationen
Für die natürlichen Zahlen, die rationalen Zahlen und die reellen Zahlen gibt es eine Relation "<", die wie folgt definiert ist:
x < y: <--> Es gibt ein (echt) positives x, so dass gilt x + z = y
Damit lässt sich die Ordnungsrelation "<=" definieren durch x <= y oder x = y
D.h. sowohl die Kleiner-oder-gleich-Beziehung als auch die Echt-Kleiner-Beziehung auf N x N (bzw. auf R x N bzw auf Q x Q bzw. auf R x R) sind Relationen.

### Beispiel für Relationen (am Beispiel der Studenten)
"ist im gleichen Jahrgang und in der gleichen Gruppe"
"ist Bruder von"
"teilt" über N
"sitzt neben" über der Menge der Studierenden des Kurses

## Eigenschaften von Relationen
1. R heißt **reflexif**, wenn aRa für alle a Element M gilt.
2. R heißt **symmetrische**, wenn aus aRb folgt bRa für alle a, b Element M.
3. R heißt **antisymmetrisch**, wenn aus aRb und bRa folgt a=b für alle a, b Element M.
4. R heißt **trasitiv**, wenn aus aRb und bRc folgt aRc für alle a, b, c Element M. 
5. R heißt **Äquivalenzrelation**, wenn R reflexiv, symmetrisch und transitiv ist. In diesem Fall nennt man für a ∈ M [a]R := {b ∈ M | aRb} die Äquivalenzklasse von a.
6. R heißt **Ordnungsrelation**, wenn R reflexiv, antisymmetrisch und transitiv ist.
Äquivalenzklassen liefern eine **disjunkte** Zerlegung von M, d.h. eine Zerlegung in Teilmengen mit paarweise leerem Durchschnitt.

## Restklassen
Definition 1.9 (Kongruenz) Sei a > 1 eine natürliche Zahl. Wir sagen, dass die ganzen Zahlen  
x und y kongruent modulo a sind (x ≡ y mod a), wenn es ein q ∈ Z gibt, so dass x = y + qa.  
Dies ist genau dann der Fall, wenn a Teiler von x−y ist (sie unterscheiden sich um ein vielfaches von a), was wiederum genau dann der Fall ist, wenn x und y bei Division durch a denselben Rest haben.  
Die Kongruenz x ≡ y mod a definiert eine Äquivalenzrelation in Z, denn:  
• Sie ist reflexiv: x ≡ x mod a  
denn: x = x + 0 · a  
• Sie ist symmetrisch: x ≡ y mod a ⇒ y ≡ x mod a  
denn: x = y + qa ⇒ y = x + (−q)a  
• Sie ist transitiv: x ≡ y mod a und y ≡ z mod a ⇒ x ≡ z mod a  
denn: x = y + q1a und y = z + q2a ⇒ x = z + q2a + q1a = z + (q2 + q1)a  
Z zerfällt in die Äquivalenzklassen  
\[z\]a := {x ∈ Z | x ≡ z mod a} (0 ≤ z < a),  
die Restklassen modulo a, da für festes a ≥ 0 jede ganze Zahl in genau einer Restklasse modulo  
a enthalten ist.  
Beispielsweise ist \[3\]10 = {x ∈ Z | x ≡ 3 mod 10} = {. . . , −7, 3, 13, 23, . . .}.  
Wir schreiben die Menge aller Restklassen modulo a als Za := {\[z\]a | 0 ≤ z < a}.
