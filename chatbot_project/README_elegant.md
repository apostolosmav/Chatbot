
# Einfacher Chatbot mit Python, Scikit-learn und Tkinter

Dieses Projekt implementiert einen einfachen textbasierten Chatbot, der mithilfe eines Naive Bayes Modells trainiert wird, um auf Benutzereingaben zu antworten. Die Benutzeroberfläche basiert auf Tkinter.

---

## Features

- Training eines Multinomial Naive Bayes Klassifikators auf Basis von Textmustern
- Verwendung von TF-IDF Vektorisierung zur Textrepräsentation
- Einfache grafische Benutzeroberfläche (GUI) mit Tkinter
- Zufällige Antwortauswahl aus vordefinierten Antworten je Kategorie (Tag)

---

## Projektstruktur

- `chatbotTraining.csv`  
  CSV-Datei mit den Trainingsdaten, bestehend aus den Spalten:  
  - `patterns`: Beispielhafte Benutzereingaben  
  - `tag`: Kategorie des Satzes  
  - `responses`: Mögliche Antworten (meist mehrere Antworten pro Tag)  

- `chatbot.py`  
  Hauptskript mit dem Training des Modells, Vorhersagefunktion und GUI-Implementierung.

---

## Voraussetzungen

- Python 3.x  
- Benötigte Python-Bibliotheken:  
  ```
  pandas
  scikit-learn
  tkinter (meist bereits bei Python enthalten)
  ```

Du kannst die benötigten Bibliotheken mit folgendem Befehl installieren:

```bash
pip install pandas scikit-learn
```

---

## Verwendung

1. Stelle sicher, dass die Datei `chatbotTraining.csv` im selben Verzeichnis wie das Skript `chatbot.py` liegt.
2. Starte das Skript:

```bash
python chatbot.py
```

3. Das Chatfenster öffnet sich. Gib deine Nachricht in das Eingabefeld ein und drücke Enter oder klicke auf "Senden".
4. Der Chatbot antwortet basierend auf dem trainierten Modell.

---

## Hinweise

- Das Modell basiert auf einem einfachen Naive Bayes Algorithmus und funktioniert am besten bei klar definierten und häufig vorkommenden Eingaben.
- Die Trainingsdaten können nach Bedarf erweitert oder angepasst werden, um die Antworten zu verbessern.
- Die Antworten werden zufällig aus den möglichen Antworten des jeweiligen Tags ausgewählt.

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.

---

