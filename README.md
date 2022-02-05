# simple_restaurant

## Analyse:
Das Programm basiert wieder auf dem ***EVA Prinzip***, wobei dieses mal die Eingaben nicht wie bei den
letzten Programmen durch ein Textfenster passieren und der User Texteingaben macht, sondern der
Großteil der Eingaben passiert durch die Maus, da vieles in Graphischer Form auftritt.

Als erstes soll beim Programmstart ein Fenster geöffnet werden, in dem man einen Tisch aussuchen
kann und die Anzahl der Personen angibt. Durch diese Angaben soll sich ein neues Fenster öffnen, in
dem dann das Menü mit den verschiedenen Gerichten auftaucht, sodass für diesen Tisch eine
Rechnung erstellt werden kann. Das Fenster für das Menü sollte offen bleiben, damit mehrere Tische
mit Bestellungen gleichzeitig offen sein können. Im Fenster für das Menü, sind dann alle Gerichte
aufgelistet, mit dem Namen und allem anderen, was in der food.csv Datei angegeben ist. Dort
besteht dann die Möglichkeit, etwas zur Bestellung hinzuzufügen und dort auch extra Wünsche
anzugeben. In dem Fenster der Bestellung kann man diese Bestellung dann auch abschließen, und
wenn man diesen Knopf gedrückt hat, kann man das Fenster schließen und im Hauptmenü auf
Orders klicken, um eine Übersicht aller Bestellungen zu sehen. Dort wird dann auch der Preis
angezeigt und was bestellt wurde.

Das Programm sollte so aufgebaut sein, dass man erst Klassen für die verschiedenen Dinge wie
Gerichte und Tische erstellt. Diese haben dann als Variablen ihre verschiedenen Attribute. Auch
werden als nächstes Funktionen für die grundsätzliche Struktur erstellt, also z.B. wie ein Menü
aufgebaut ist und wie ein neues Fenster geöffnet wird. Die Funktion des geöffneten Fensters ist
dabei sehr groß, da in ihr der großteil des ablaufs beschrieben wird. Durch das Graphische werden
hier die design optionen beschrieben, wie ein Fenster aussieht, was für Farben verwendet werden,
wie groß Knöpfe und ähnliches sind. Dafür wird tkinter importiert, da man damit in Python ein GUI
erstellen kann. In dieser Funktion geht es dann weiter mit dem erstellen des Menüs und den
Funktionen für Gerichte hinzufügen und wieder löschen, genauso wie Gerichte verändern. Auch
werden die Error anzeigen erstellt, wenn z.B. ein Tisch erstellt werden soll aber keine Tischnummer
oder Personenanzahl beschrieben wurde.

![alt text](https://github.com/googlpasha/simple_restaurant/tree/main/UMLDiagramm.png?raw=true)

Dieses *UML Diagramm* haben wir uns als Grundstruktur erstellt, um einmal zu überlegen wie am
Ende das Programm aufgebaut sein soll und mit was für Klassen wir arbeiten.

## Test:
Auch hier funktioniert ein Ablauf nach Benutzerhandbuch wieder ohne Probleme, deshalb diese
Testfälle:

Test 1: Man erstellt einen Tisch, ohne die Tischnummer anzugeben; Error Meldung: Something went
wrong

Test 2: Man erstellt einen Tisch, ohne die Personenanzahl anzugeben; Error Meldung: Something
went wrong

Test 3: Man Customized ein Gericht, ohne etwas zur Bestellung hinzugefügt zu haben; Nichts
passiert, es kommt auch kein Fehler.

Test 4: Man fügt nichts zu Bestellung hinzu, aber klickt auf order; Es wird eine leere Bestellung
hinzugefügt, die auch nichts kostet.

## Doku:
Das Programm läuft auf Python 3.10 und benutzt imports aus der Standart Bibliothek von der
Standart-Installation auf www.python.org
Der erste Import ist csv, mit dem man die excel Tabelle, die uns angegeben wurde einlesen kann.
Damit wird dann das Menü erstellt. Der zweite Import ist tkinter, mit dem das GUI erstellt wird.

### Benutzerhandbuch:

Ein User der das Programm ausführt, soll für die Tischnummer und die Personenanzahl einen Integer
eingeben und kommt dann in das Menü wo er eine Bestellung aufgeben kann. Dort gibt klickt er
dann immer die verschiedenen Gerichte an, die er bestellen will und klickt dann auf add um es
hinzuzufügen. Wenn er etwas wieder löschen will, muss er das Gericht unten in der Liste der
hinzugefügten Gerichte anklicken und auf delete. Wenn er einen Sonderwunsch hat, soll er auch
wieder da Gericht unten in der Liste anklicken und dann unten bei Custom feature seinen Wunsch
eintragen und auf Customize klicken. Wenn der User zufrieden mit der Bestellung ist, muss er ganz
unten auf Make Order klicken und ihm wird dann gesagt, dass er das Fenster schließen kann. Wenn
er eine neue Bestellung machen will, kann er diesen Prozess wieder durchlaufen. Im Hauptmenü gibt
es aber auch noch die Option auf Orders zu klicken, wo jeweils eine Liste der Bestellungen mit dem
jeweiligen Tisch ist. Wenn also der User fertig ist mit den Bestellungen, kann er auf diese Liste gehen
und dort stehen alle Preise mit den Tischen um eine Rechnung zu erstellen. Dieses Fenster kann er
auch wieder schließen, wenn er fertig ist und vom Hauptmenü kann er immer alles wieder aufrufen
und wiederholen.

Dieses Programm soll wieder mit der *Cmd* ausgeführt werden oder mit einer *Shell*, die Python
ausführen kann. Dieses mal läuft das Programm mit Eingaben dann aber nicht dort, sondern es
öffnen sich graphische Fenster mit Klick-Eingaben.
Die Import csv und tkinter waren wie oben erklärt, dafür da um erstens die Tabelle für die Gerichte
einzulesen und um ein graphisches Interface zu erstellen.

Es wurde im laufe des Codens veränderungen an der Grundstruktur vorgenommen, deshalb ist das
Programm nicht mehr 1 zu 1 so aufgebaut, wie unser erstes UML Diagramm es vorsieht. Die großen
unterschiede waren bei dem Bezahlen und der Rechnung.

Auch sind manche Dinge nicht zu 100% in unserem Programm implementiert, wie z.B. das erstellen
einer Rechnung, dafür haben wir nur eine Liste der Bestellungen für einen Tisch mit den jeweiligen
Preisen. Auch sind Sonderwünsche nicht genau wie in der Aufgabe, da man sie zwar hinzufügen
kann, allerdings wird leider nicht unteschieden zwischen wegnehmen und hinzufügen und somit
auch dort nicht preislich.

Die restliche Doku, also wie alles aufgebaut ist und wie der Ablauf ist, wurde in der Analyse
beschrieben und die verschiedenen Tests von unterprogrammen wurde in Tests vorgenommen. An
diesem Ablauf wurde nichts mehr verändert.

*Doku wurde erstellt von Fynn Kanja.*
