## Terrance Andrew Davis
- Vortrag heute soll zwar um TempleOS gehen, aber zuerst etwas über dessen Schaffer, Terrance Andrew Davis, kurz Terry
* 1969-2018
* als schizophren diagnostiziert
* sah sich selbst als in direkter Kommunikation mit Gott
* Gott befahl ihm, ihm ein Betriebssystem als Tempel zu schreiben
* Begonn 2003 an TempleOS zu entwickeln

## TempleOS
* urspr. J Operating System, Losethos, SparrowOS
* Komplett von Terry geschrieben, hatte sich als Ziel gesetzt, auf Befehl von Gott, max 100k LOC, kam dann aber auf ca 118k
* Laut T: Betriebssytem zum herumprobieren, rumspielen und zur Interaktion mit Gott
* T empfiehlt, das Betriebssystem in einer VM laufen zu lassen, es ist nicht als Daily Driver gedacht

# Technisches
## Architektur
* Für x64 CPUs geschrieben
* non-preemptive multitasking -> bedeutet: Programme müssen von selbst CPU-Zeit an andere Programme "abgeben", statt (wie bei z.B. Linux oder Windows NT) dass das OS die CPU-Zeit zwischen Prozessen balanciert
* ring-0-only -> bedeutet "alles läuft im Kernel Mode" / wird nicht unterschieden zwischen Kernel space oder User space
* single address space -> alle Programme teilen sich den gleichen Adressraum im System
* kein Netzwerk-Stack
* 16 Farben, 640x480 <- Gotts Auflösung
* Support für FAT32, ISO-9660, RedSea Dateisystem (letzteres ist von Terry selbst entwickelt)
* Alle Prozesse kommen aus Adam

* Warum so unsicher? -> Warum sollte es sicher sein? Laut T anfangs primär entwickelt zum "recreational programming", jedes Programm hat full kernel mode access "because it's fun"
> The CIA encourages code obsfucation.  They make it more complicated than 
necessary.  TempleOS is, literally, more simple than necessary.  It is 
obnoxiously simple... to the point it hurts.
> I capped the 
line-of-code count at 100,000 and God said it must be perfect, so it will never 
be an ugly monstrocity.

von der faq seite

## HolyC
* Meiste Software des Systems in HolyC geschrieben
* von T entwickelte Sprache, zwischen C und C++, hieß daher urspr. C+
* Eigener JIT-Compiler
* auch Als Shell-Sprahe
* Code Editor hat Support für 3D Meshes, Bilder in Textdateien, z.B. als Kommentare im HolyC Code

## Softwares
* Bootloader
* Compiler/Assembler für HolyC, support für JIT und AOT Kompilation
* Maus und Tastaturtreiber
* VGA Grafiktreiber für 640x480 mit 16 Farben
* Festplattentreiber für ATA-Festplatten
* CD/DVD-Laufwerktreiber für ATAPI PIO-Laufwerke
* Window Manager
* Dateimanager
* AutoCompletion
* Partitionierungswerkzeug
* Editor und Browser für eigenes Dokument-Format
* Grafiken und Ressourcen direkt im SourceCode
* 2D+3D Grafik-Bibliotheken
* Code profiler mit merge und diff utils
* PC-Lautsprecher-Support mit Musik-Kompositions-programm
* Demo-3D-Spiele 
* .Z -> eigene TempleOS Compression

* Komplettes Betriebssystem erschaffen von Grund auf von einer Person ist unglaubliche Aufgabe, auch wenn das Betriebssystem "altbacken" aussieht steckt trotzdem unendlich viel Arbeit dahinter
* Für Leute die sich nicht ganz vorstellen kann wie aufwendig es ist: Entwickler in Interview meinte "Es ist nicht, als würde eine Person ein Haus bauen, sondern, als würde eine Person einen ganzen Wolkenkratzer bauen"

# Live-Demo

# Quellen
https://www.vice.com/en/article/wnj43x/gods-lonely-programmer
https://web.archive.org/web/20180928201148/https://thenewstack.io/the-troubled-legacy-of-terry-davis-gods-lonely-programmer/
https://web.archive.org/web/20201108002150/https://www.columbiagorgenews.com/thedalleschronicle/news/man-killed-by-train-had-tech-following/article_1f03fc0d-c223-5f20-a915-460fce4299f1.html
https://www.youtube.com/watch?v=UCgoxQCf5Jg <- tu das mal in die letzte folie oder so als empfehlung zur vertiefung