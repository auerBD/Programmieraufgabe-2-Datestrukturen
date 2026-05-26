# Laufzeitmessungen – Programmieraufgabe 2

Dieses Dokument dient zur gemeinsamen Erfassung und Auswertung der gemessenen Laufzeiten.  
Bitte nach dem Ausführen von `assignment_2.py` die Tabellen ausfüllen.

---

## Theoretisch erwartete Laufzeiten

| Algorithmus    | Best Case  | Average Case | Worst Case  | Stabil? |
|----------------|-----------|--------------|-------------|---------|
| Insertion Sort | O(n)      | O(n²)        | O(n²)       | ✅ Ja   |
| Selection Sort | O(n²)     | O(n²)        | O(n²)       | ❌ Nein |
| Merge Sort     | O(n log n)| O(n log n)   | O(n log n)  | ✅ Ja   |
| Quick Sort     | O(n log n)| O(n log n)   | O(n²)       | ❌ Nein |

> **Best Case Insertion Sort:** bereits sortierte Eingabe → nur n-1 Vergleiche, keine Verschiebungen.  
> **Worst Case Quick Sort:** schlechte Pivot-Wahl (z. B. immer kleinster/größter Wert) → O(n²). Zu vermeiden durch randomisierten Pivot oder Median-of-Three.

---

## Gemessene Laufzeiten

> Einheit: Sekunden | Eingabe: aufsteigend / absteigend / zufällig  
> *(Felder mit `—` bedeuten: für diese Länge nicht gemessen, da quadratische Algorithmen bei n > 10.000 übersprungen werden)*

### Insertion Sort

| n       | aufsteigend (s)| absteigend (s) | zufällig (s) |
|---------|----------------|----------------|--------------|
| 10      |     0.00000437 |    0.00000967  |   0.00000517 |
| 100     |     0.00001529 |    0.00068675  |   0.00038183 |
| 1.000   |     0.00016842 |    0.08230017  |   0.04244138 |
| 10.000  |     0.00175137 |    8.21354717  |   4.06974621 |
| 50.000  | —              | —              | —            |
| 200.000 | —              | —              | —            |

### Selection Sort

| n       | aufsteigend (s)| absteigend (s) | zufällig (s) |
|---------|----------------|----------------|--------------|
| 10      |    0.00000754  |    0.00000721  |  0.00000667  |
| 100     |    0.00044546  |    0.00043717  |  0.00043862  |
| 1.000   |    0.04722771  |    0.04632313  |  0.04574371  |
| 10.000  |    4.52087092  |    4.61379229  |  4.51761517  |
| 50.000  | —              | —              | —            |
| 200.000 | —              | —              | —            |

### Merge Sort

| n       | aufsteigend (s) | absteigend (s) | zufällig (s) |
|---------|----------------|----------------|--------------|
| 10      |                |                |              |
| 100     |                |                |              |
| 1.000   |                |                |              |
| 10.000  |                |                |              |
| 50.000  |                |                |              |
| 200.000 |                |                |              |

### Quick Sort

| n       | aufsteigend (s) | absteigend (s) | zufällig (s) |
|---------|----------------|----------------|--------------|
| 10      |      0.00003030|      0.00002690|    0.00001450|
| 100     |      0.00024220|      0.00023860|    0.00023710|
| 1.000   |      0.00274650|      0.00333680|    0.00285370|
| 10.000  |      0.03812900|      0.03828250|    0.03675230|
| 50.000  |      0.21918250|      0.20951400|    0.21699540|
| 200.000 |      1.03181070|      1.02849080|    0.96816170|

---

## Auswertung

*(Hier nach dem Befüllen der Tabellen gemeinsam ausfüllen)*

### Entsprechen die Laufzeiten den Erwartungen?

**Insertion Sort:**  
> Ja

**Selection Sort:**  
> Ja

**Merge Sort:**  
> ...

**Quick Sort:**  
> Ja

### Auffälligkeiten

> z. B. Unterschiede zwischen aufsteigender und zufälliger Eingabe, Verhalten bei großen n, ...

---

## Wer hat was gemessen

| Name | Betriebssystem | Python-Version  | Datum       |
|------|----------------|-----------------|-------------|
|Bence |  Mac OS        |       3.13.5    |   22.05.2026|
|Kevin |  Windows 11    |       3.13.6    |   26.05.2026|
|      |                |                 |             |
