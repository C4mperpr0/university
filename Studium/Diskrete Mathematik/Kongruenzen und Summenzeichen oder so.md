#Kongruenz #Hash #Haskfunktion #funktionenabbildungen #abbildunngen

Bsp: ISBN-10

S. 12

Prüfgleichung: $\sum_{i = 1}^{10} i a_{i} \equiv 0 mod 11$
und es gilt: $-10 a_{10} \equiv -10 a_{10} mod 11$

gemäß (1.5): beide Kongruenzen addieren
$\sum_{i = 1}^{10} i a_{i} - 10 a_{10} \equiv (0-10 a_{10}) mod 11$
↓
$\sum_{i = 1}^{9} i a_{i} + 10 a_{10} - 10 a_{10}$
↓
$\sum_{i = 1}^{9} i a_{i} \equiv - 10 a_{10} mod 11$ und es gilt $0 \equiv 11 a_{10} mod 11$

wieder beide Kongruenzen addieren:
$\sum_{i=1}^{9} i a_{i} + 0 \equiv (-10a_{10} + 11a_{10}) mod 11$
$\sum_{{i=1}}^{9} i a_{i} \equiv a_{10} mod 11$

$a_{10} \equiv \sum_{i = 1}^{9} i a_{i} mod 11$

gemäß (1.5): beide Kongruenzen addieren

∑i=110iai−10a10≡(0−10a10)mod11
↓
∑i=19iai+10a10−10a10
↓
∑i=19iai≡−10a10mod11 und es gilt 0≡11a10mod11
Drawing 2022-11-02 09.58.34.excalidraw
ISBN 3-519-22053
$\sum_{i = 1}^{9} i a_{i} = 141 \equiv 9 mod 11$

# Haschischfunktionen

- p = 7
- k1 = BERLIN -> Summieren von allem, A=1, B=2, ... $\sum_{{i=1}}^{6} i a_{i}mod 7$
- = 2+5+18+12+9+14 = 60 $\equiv$ 4 mod 7
- k2 = BONN = 2+15+14+14 = 45 -> 45 mod 7 = 3

# Funktionen Abbildung
- Hat das mit Bildern zu tun? Code-Screenshot?
- file:///home/carl/Documents/university/diskrete%20mathematik/DiskreteMathematik_f_Informatiker_2022_Skript_print.pdf Seite 14

- Komposition: g nach f; A -> D (g nach f)(a) = g(f(a))
- Eine Abbilding f : A -> B ist eine Realtion f auf A x B mit folgenden Eigentschaften:
1. Für alle a $\in$ A existiert ein b $\in$ B mit a f b.
2. Aus a f b und a f c folgt b = c für alle a $\in$ A und alle b, c $\in$ B.
Es lassen sich folgende Eigenschaften von Funktionen definieren:
### Definition 1.11 (Injektivität, Surjektivität, Bijektivität)
1. Eine Funktion f : A → B heißt injektiv genau dann, wenn für alle a1, a2 ∈ A, a1 6 = a2  
folgt, dass f (a1) 6 = f (a2). (Oder auch: Aus f (a1) = f (a2) folgt, dass a1 = a2.)  
2. Eine Funktion f : A → B heißt surjektiv genau dann, wenn f (A) = B ist.  
3. Eine Funktion f : A → B heißt bijektiv genau dann, wenn f sowohl injektiv als auch  
surjektiv ist.

### Beispiel f Funktionen
1. Konstante F z.B. f(x)=1
2. identische F, f(x)=x
3. lineare Funktion f(x)=ax z.B. f(x)=5x
4. Affin-linear f(x)=ax+b z.B. f(x)=69x+420 (ist nicht linear weil sie nicht f(0)=0 ist (nicht durch den Nullpunkt geht))
5. Ganzrationale Funktion (Polynom):  f (x) = a0 + a1x + a2x2 + . . . + anxn 
	 mit a0, a1, . . . , an ∈ R für alle x ∈ D  
1. Gebrochen rationale Funktion:  
f (x) = a0 + a1x + a2x2 + . . . + anxn
b0 + b1x + b2x2 + . . . + bmxm  
mit a0, a1, . . . , an, b0, b1, . . . , bm, ∈ R für alle x ∈ D  
7. Wurzelfunktion: f (x) = n  
√x mit n ∈ N für alle x ∈ D mit x ≥ 0  
8. Betragsfunktion: f (x) =| x | für alle x ∈ D5