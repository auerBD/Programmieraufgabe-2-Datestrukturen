# Programmieraufgabe 2 – Sortieralgorithmen

**Lehrveranstaltung:** Datenstrukturen und Algorithmen  
**Abgabe:** 27.05.2026 via GitHub  

---

## Aufgabenstellung

Implementierung und Laufzeitanalyse von vier Sortieralgorithmen in Python:

| Algorithmus      | Erwartete Komplexität (Average Case) | Zuständig |
|------------------|--------------------------------------|-----------|
| Insertion Sort   | O(n²)                                | Bence     |
| Selection Sort   | O(n²)                                | Bence     |
| Merge Sort       | O(n log n)                           | Lukas     |
| Quick Sort       | O(n log n)                           | Kevin     |

---

## Projektstruktur

```
.
├── assignment_2.py     # Hauptdatei mit allen Implementierungen
├── ERGEBNISSE.md       # Laufzeitmessungen und Auswertung
├── README.md           # Diese Datei
└── .gitignore
```

---

## Setup & Ausführen

### Voraussetzungen

- Python 3.10+
- NumPy

### Installation

# Python installieren

# Abhängigkeiten installieren
pip install numpy
```

### Ausführen

```bash
python assignment_2.py
```

Die Ausgabe zeigt für jede Algorithmus/Eingabe-Kombination die Laufzeit in Sekunden.  
Die Ergebnisse bitte in [`ERGEBNISSE.md`](ERGEBNISSE.md) eintragen.

### Verifikationstests

Sobald alle Implementierungen fertig sind, die Zeile in `assignment_2.py` einkommentieren:

```python
run_basic_verification_tests()
```

---

## Git-Workflow

```bash
# Vor dem Arbeiten: aktuellen Stand holen
git pull

# Nach Änderungen: committen und pushen
git add assignment_2.py
git commit -m "feat: selection_sort implementiert"
git push
```

**Bitte keine direkte Commits auf `main`.** Feature-Branches verwenden:

```bash
git checkout -b feature/merge-sort
# ... Änderungen ...
git push origin feature/merge-sort
# → Pull Request auf GitHub öffnen
```
