import pandas as pd
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from random import choice
import os

# ----------------------------
# 1. Dateneinlesung 
# ----------------------------

data_path = os.path.join(os.path.dirname(__file__), "chatbotTraining.csv")
df = pd.read_csv(data_path)

# ----------------------------
# 2. Daten Vorbereiten mit Vectorizer
# ----------------------------
vectorizer = TfidfVectorizer(stop_words='english',max_features=1000,lowercase=True)
X = vectorizer.fit_transform(df['patterns'])
y = df['tag']

# ----------------------------
# 2. Daten trainieren & modelieren
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# --- Vorhersagefunktion ---
def predict(user_input):
    user_vector = vectorizer.transform([user_input])

    tag = model.predict(user_vector)[0]
    antworten = df[df['tag'] == tag]['responses'].values

    if len(antworten) > 0:
        return choice(antworten)
    else:
        return "Ich weiß leider nicht, was du meinst."

# --- Nachricht senden ---
def nachricht():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_text.insert(END, "Du: " + user_input + "\n")
    antwort = predict(user_input)
    chat_text.insert(END, "Chatbot: " + antwort + "\n")
    entry.delete(0, END)

# --- GUI ---
fenster = Tk()
fenster.title("Chatbot")

chat_text = ScrolledText(fenster, wrap=WORD, width=60, height=20)
chat_text.pack(padx=10, pady=10)

entry = Entry(fenster, width=50)
entry.pack(padx=10, pady=10)
entry.bind("<Return>", lambda event: nachricht())

button = Button(fenster, text="Senden", command=nachricht)
button.pack(pady=5)

fenster.mainloop()
