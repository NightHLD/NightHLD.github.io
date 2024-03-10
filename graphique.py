import streamlit as st
import numpy as np
import base64
import time
from random import randint
import Game_1.py



emotion = "heureux"
sante = "ok"
etat = "vivant"

# Initialise les variables
if ('energie' and 'nourriture' and 'bonheur' and 'proprete' and 'crotte') not in st.session_state:
    st.session_state['energie'] = 100
    st.session_state['nourriture'] = 100
    st.session_state['bonheur'] = 100
    st.session_state['proprete'] = 100
    st.session_state['crotte'] = 0

# Bouttons et les effets
if st.button('CLEAR'):
    st.cache_data.clear()

if st.button('CLEAR BOURRIN'):
    st.session_state['energie'] = 100
    st.session_state['nourriture'] = 100
    st.session_state['bonheur'] = 100
    st.session_state['proprete'] = 100
    st.session_state['crotte'] = 0

if st.button('SOMMEIL'):
    st.session_state['energie'] += 15


if st.button('NOURRIR'):
    st.session_state['nourriture'] += 25

if st.button('DOPAMINE'):
    st.session_state['bonheur'] += 15

if st.button('LINGUETTE DESINFECTANTE'):
    st.session_state['crotte'] = 0
    st.session_state['proprete'] += 5

if st.button('DOUCHE'):
    st.session_state['proprete'] += 10

# Affiche les stats
st.write("Energie actuelle :", st.session_state['energie'])
st.write("Faim actuel :", st.session_state['nourriture'])
st.write("Bonheur actuel :", st.session_state['bonheur'])
st.write("Proprete actuelle :", st.session_state['proprete'])
st.write("Crotte actuelle :", st.session_state['crotte'])
st.write("Etat : vivant")
st.write("Sante actuelle :", sante)

# Modifie les variables

st.session_state['energie'] -= 10
st.session_state['nourriture'] -= 20
st.session_state['bonheur'] -= 10
st.session_state['proprete'] -= (2 + 0.5*st.session_state['crotte'])
    
if randint(1, 5) == 3:
    st.session_state['crotte'] += 1

# Evite que les variables depassent
if st.session_state['energie'] >= 100:
    st.session_state['energie'] = 100
if st.session_state['energie'] < 0:
    st.session_state['energie'] = 0

if st.session_state['nourriture'] >= 100:
    st.session_state['nourriture'] = 100
if st.session_state['nourriture'] < 0:
    st.session_state['nourriture'] = 0

if st.session_state['bonheur'] >= 100:
    st.session_state['bonheur'] = 100
if st.session_state['bonheur'] < 0:
    st.session_state['bonheur'] = 0

if st.session_state['proprete'] >= 100:
    st.session_state['proprete'] = 100
if st.session_state['proprete'] < 0:
    st.session_state['proprete'] = 0

if st.session_state['crotte'] >= 10:
    st.session_state['crotte'] = 10

# Pour la maladie
if st.session_state['proprete'] < 45:
    chance = randint(1, 2)
    if chance == 1:
        sante = "malade"

# Conditions pour la mort
if st.session_state['energie'] == 0 and st.session_state['nourriture'] == 0 and st.session_state['bonheur'] == 0 and st.session_state['proprete'] == 0:
    etat = "mort"
    


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


if etat == "mort":
    autoplay_audio("oof.mp3")
    

if st.session_state['energie'] == 100 and st.session_state['nourriture'] == 100 and st.session_state['bonheur'] == 100 and st.session_state['proprete'] == 100:
    st.image('normal.png')

if etat == "malade":
    st.image('malade.png')

if st.session_state['energie'] == 50 and st.session_state['nourriture'] == 20 and st.session_state['bonheur'] == 30 and st.session_state['proprete'] == 50:
    etat= "Triste"
    st.image('triste.png')

time.sleep(10)

st.rerun()
