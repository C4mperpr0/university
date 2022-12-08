/* Datenbank zurücksetzen */
DROP TABLE Mitarbeiter;
DROP TABLE Projekt;
DROP TABLE Arbeitszeit;

CREATE TABLE Mitarbeiter
(
	MitarbeiterID INTEGER, /* Primärschlüssel */
	Vorname TEXT,
	Nachname TEXT
);
CREATE TABLE Projekt
(
	ProjektID INTEGER, /* Primärschlüssel */
	Name TEXT,
	Kunde TEXT,
	Prioritaet INTEGER
);
CREATE TABLE Arbeitszeit
(
	MitarbeiterID INTEGER, /* Fremdschlüssel */
	ProjektID INTEGER, /* Fremdschlüssel */
	Datum INTEGER, * Primärschlüssel *
	Dauer INTEGER
);

INSERT INTO Mitarbeiter VALUES (1, "Carl", "Bellgardt");
INSERT INTO Mitarbeiter VALUES (69, "Lucas", "Heinschke");
INSERT INTO Mitarbeiter VALUES (420, "Nichlas", "Schmitz");

INSERT INTO Projekt VALUES (1, "Bankcompiler", "Deutsche Parkbank", 3);
INSERT INTO Projekt VALUES (2, "Virus.exe", "Intern", 1);
INSERT INTO Projekt VALUES (7, "YoutubeVanced Clone", "Google", 2);

INSERT INTO Arbeitszeit VALUES (1, 7, 1671490800, 8);
INSERT INTO Arbeitszeit VALUES (69, 2, 1615503600, 9);
INSERT INTO Arbeitszeit VALUES (420, 1, 1612566000, 3);
