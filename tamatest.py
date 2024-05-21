import streamlit as st
import numpy as np
import base64
import time
from random import randint
import pages



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
st.write("Etat :", etat)
st.write("Sante actuelle :", sante)

# Evite que les variables depassent
if st.session_state['energie'] > 100:
    st.session_state['energie'] = 100
if st.session_state['energie'] < 0:
    st.session_state['energie'] = 0

if st.session_state['nourriture'] > 100:
    st.session_state['nourriture'] = 100
if st.session_state['nourriture'] < 0:
    st.session_state['nourriture'] = 0

if st.session_state['bonheur'] > 100:
    st.session_state['bonheur'] = 100
if st.session_state['bonheur'] < 0:
    st.session_state['bonheur'] = 0

if st.session_state['proprete'] > 100:
    st.session_state['proprete'] = 100
if st.session_state['proprete'] < 0:
    st.session_state['proprete'] = 0

if st.session_state['crotte'] > 10:
    st.session_state['crotte'] = 10

time.sleep(7)

# Modifie les stats
while st.session_state['energie'] > 0:
    st.session_state['energie'] -= 10
    
while st.session_state['nourriture'] > 0:
    st.session_state['nourriture'] -= 20

while st.session_state['bonheur'] > 0:
    st.session_state['bonheur'] -= 10

while st.session_state['proprete'] > 0:
    st.session_state['proprete'] -= (2 + 0.5*st.session_state['crotte'])
    
if randint(1, 5) == 3:
    st.session_state['crotte'] += 1

# Pour la maladie
if st.session_state['proprete'] < 45:
    chance = randint(1, 2)
    if chance == 1:
        sante = "malade"

# Conditions pour la mort
if st.session_state['energie'] == 0 and st.session_state['nourriture'] == 0 and st.session_state['bonheur'] == 0 and st.session_state['proprete'] == 0:
    etat = "mort"
    autoplay_audio("oof.mp3")



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


if st.session_state['energie'] == 100 and st.session_state['nourriture'] == 100 and st.session_state['bonheur'] == 100 and st.session_state['proprete'] == 100:
    st.image('normal.png')

if sante == "malade":
    st.image('malade.png')

if st.session_state['energie'] == 50 and st.session_state['nourriture'] == 20 and st.session_state['bonheur'] == 30 and st.session_state['proprete'] == 50:
    emotion = "Triste"
    st.image('triste.png')

# Mini-jeux

# Pile ou Face
st.write("Jeu du Pile ou Face")

choix_joueur_PF = ""
choix_ordi_PF = 0

if st.button('PILE'):
    choix_joueur_PF = 1
    choix_ordi_PF = randint(1, 2)
if st.button('FACE'):
    choix_joueur_PF = 2
    choix_ordi_PF = randint(1, 2)

if choix_joueur_PF == choix_ordi_PF:
    st.write("victoire")
elif choix_joueur_PF != "" and choix_joueur_PF != choix_ordi_PF:
    st.write("defaite")

# Which Ace ?
st.write("Which Ace ?")

choix_joueur_ace = ""
choix_ordi_ace = randint(1, 4)

if st.button('&#9824;'):
    choix_joueur_ace = 1
    choix_ordi_ace = randint(1, 4)
    
if st.button('&#9827;'):
    choix_joueur_ace = 2
    choix_ordi_ace = randint(1, 4)

if st.button('&#9830;'):
    choix_joueur_ace = 3
    choix_ordi_ace = randint(1, 4)

if st.button('&#9829;'):
    choix_joueur_ace = 4
    choix_ordi_ace = randint(1, 4)

if choix_joueur_ace == choix_ordi_ace:
    st.write("victoire")
    if choix_joueur_ace == 1:
        st.write("Ace of Spades for AroAces (Aromantic Asexuals) !")
    elif choix_joueur_ace == 2:
        st.write("Ace of Clubs for questionning people on the Aro/Ace spectrum !")
    elif choix_joueur_ace == 3:
        st.write("Ace of Diamonds for GreyAces and DemiAces (Grey Asexuals and Demi Asexuals)")
    elif choix_joueur_ace == 4:
        st.write("Ace of Hearts for Aces (Asexuals) !")

elif choix_joueur_ace != "" and choix_joueur_ace != choix_ordi_PF:
    st.write("defaite")

# N'oubliez pas les paroles
st.write("N'oubliez pas les paroles (version cheap)")

chanson = randint(1, 4)
reponse = ''

if st.button('LANCER'):
    
    if chanson == 1:
        st.write('Never Gonna Give You Up, Rick Astley, 1987')
        st.write('Never gonna give you up  \nNever gonna let you down  \nNever gonna run around and desert you  \nNever gonna ____________  \nNever gonna say goodbye  \nNever gonna tell a lie and hurt you')
        
        if st.button('make you cry'):
            reponse = 'correct'
        elif st.button('laugh at you') or st.button('run away'):
            reponse = 'incorrect'
            
    if chanson == 2:
        st.write('My Actual Code from There Is No Game : Wrong Dimension, 2020  \n(if you don&rsquo;t know about this non-game already then go watch a gameplay or play to it yourself NOW)')
        st.write('Color is set to 0  \nPrint &rsquo;cry&rsquo; and trace &rsquo;sorrow&rsquo;  \nFor Gigi - You  \nType end  \nWhat&rsquo;s a game with no pleasure ?  \nLoop until us = together  \nIf ____ is what we earn  \nThen go to me and press return')
        
        if st.button('xp') or st.button('love'):
            reponse = 'incorrect'
        elif st.button('home'):
            reponse = 'correct'
            
    if chanson == 3:
        st.write('Bad Liar, Imagine Dragons, 2018')
        st.write('Look me in the eyes, tell me what you see  \n_____________, tearin&rsquo; at the seams  \nI wish I could escape it, I don&rsquo;t wanna fake if  \nWish I could erase it, make your heart believe')
            
        if st.button('Lovely life') or st.button('Perfect family'):
            reponse = 'incorrect'
        elif st.button('Perfect paradise'):
            reponse = 'correct'
    
    if chanson == 4:
        st.write('Lemon Tree, Fool&rsquo;s Garden, 1996')
        st.write('I wonder how  \nI wonder why  \n_______ you told me &rsquo;bout the blue, blue sky  \nAnd all that I can see is just a yellow lemon tree  \n  \nI&rsquo;m turning my head up and down  \nI&rsquo;m turning, turning, turning, turning, turning around  \nAnd all that I can see is just another lemon tree')
        
        if st.button('Yesterday'):
            reponse = 'correct'
        elif st.button('Once') or st.button('A year ago'):
            reponse = 'incorrect'

    if reponse == 'correct':
        st.write('Victoire')
    elif reponse == 'incorrect':
        st.write('Perdu')



st.rerun()