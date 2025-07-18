import pandas as pd
from tkinter import *
from tkinter import scrolledtext
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from random import choice
import os

# ----- Datenvorbereitung -----
def get_vokabular(df):
    vokabular = []
    for satz in df['patterns']:
        worte = satz.lower().split()
        vokabular.extend(worte)
    vokabular = sorted(set(vokabular))
    return vokabular

def get_bow(df, vokabular):
    bow = []
    for satz in df['patterns']:
        satz_bow = [1 if wort in satz.lower().split() else 0 for wort in vokabular]
        bow.append(satz_bow)
    return bow

# CSV laden
data_path = os.path.join(os.path.dirname(__file__), "chatbotTraining.csv")
df = pd.read_csv(data_path)

vokabular = get_vokabular(df)
X = get_bow(df, vokabular)
y = df['tag']

# ML Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
decisionTree = DecisionTreeClassifier()
decisionTree.fit(X_train, y_train)

# ----- Vorhersagefunktion -----
def predict(userinput):
    user_bow = [1 if wort in userinput.lower().split() else 0 for wort in vokabular]
    kategorie = decisionTree.predict([user_bow])[0]
    antworten = df[df['tag'] == kategorie]['responses'].tolist()
    return choice(antworten) if antworten else 'Ich weiß leider nicht, was du meinst.'

# ----- GUI -----
def nachricht():
    userinput = entry.get()
    if userinput.strip() == '':
        return
    chat_text.config(state='normal')
    chat_text.insert(END, f'Du: {userinput.strip()}\n')
    antwort = predict(userinput.strip())
    chat_text.insert(END, f'Chatbot: {antwort}\n')
    chat_text.config(state='disabled')
    chat_text.see(END)
    entry.delete(0, END)

fenster = Tk()
fenster.title('Chatbot')
chat_text = scrolledtext.ScrolledText(fenster, wrap=WORD, width=40, height=20, state='disabled')
chat_text.pack(padx=10, pady=10)

entry = Entry(fenster, width=40)
entry.pack(padx=10, pady=(0, 10))
entry.bind('<Return>', lambda event: nachricht())

bt = Button(fenster, text='Send', command=nachricht)
bt.pack()

fenster.mainloop()
