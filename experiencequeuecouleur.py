#!/usr/bin/env python
#-*- coding: utf-8 -*-
import __future__
#import pygame
from psychopy import core, visual, event
import csv
import random
import time
from psychopy.sound import Sound

## SETUP
win = visual.Window([1080, 720], monitor="testMonitor", fullscr = False
)
counter = 0

## Input
stim_list = []
datafile = open("/Users/sophie/Desktop//guppy/queuecouleur.csv", "r",encoding="utf-8")
reader = csv.reader(datafile, delimiter=";")
for row in reader:
    stim_list.append((row[0], row[1]))
datafile.close()
#print(len(stim_list))
## Output
datafile = open("data_xp.csv", "w", encoding="utf-8")
writer = csv.writer(datafile, delimiter=";")

start = time.time()

def list2file(x):
    r = x[0]+"_"+x[1]
    return r
def list2str(x):
    r = ''
    for i in x : r = r + str(i)
    return r

## BEGIN

def mess(x ,pos=False):
    message = visual.TextStim(win, text=x, units='norm', color='white', pos=(0,0))
    if pos != False : message.pos = pos
    message.draw()
    win.flip()
    c = None
    while c != 'return':
        c = event.waitKeys()
        c = c[0]
    win.flip()

def boucle(x=True, y=True):
    c, answer = None, []
    while c != 'return':
        c = event.waitKeys()
        c = c[0] ## DO NOT FORGET !!
        if c == 'backspace' :
            try : answer.pop()
            except : pass
        else : answer.append(c)
        messageR.text = 'Votre reponse : '+ list2str(answer)
        if x : pic.draw()
        if y : messageQ.draw()
        messageR.draw()
        win.flip()
    answer.pop()
    win.flip()
    return answer

message0 = visual.TextStim(win, text='Welcome in this experiment on the beauty perception of fishes ! (Bienvenue dans cette expérience en perception visuelle sur la Beauté des poissons!)', units='norm', color='blue', pos=(0,0.4))
message0.draw()
#message1 = visual.TextStim(win, text='Les mesures sont a donner en centimetres.', units='norm', color='white', pos=(0,0))
#message1.draw()

hello = "Please switch to AMERICAN keyboard. (Merci de passer en clavier americain). To start press ENTER- (Pour commencer : appuyer sur Entrée)"
mess(hello,(0,-0.4))

## INITIALISATION

messageQ = visual.TextStim(win, text='Your name/Votre prenom (without special characters (sans caracteres spéciaux)) :', units='norm')
messageQ.pos = (0, +0.3)
messageQ.draw()
messageR = visual.TextStim(win, text='', units='norm')
messageR.pos = (0, +0)
messageR.draw()
win.flip()
prenom = list2str(boucle(x=False))

messageQ = visual.TextStim(win, text='Your family name/votre nom de famille (without special characters/sans caracteres speciaux) :', units='norm')
messageQ.pos = (0, +0.3)
messageQ.draw()
messageR = visual.TextStim(win, text='', units='norm')
messageR.pos = (0, +0)
messageR.draw()
win.flip()
nom = list2str(boucle(x=False))

anonymat = random.randint(1000,9999)
print("Your anonymatity number / Votre Numero d'anonymat : %s" %anonymat)
mess(" Your anonymatity number / Votre numero d'anonymat : %s" %anonymat,(0,-0.2))

datafile = open("data_xp_%s_%r.csv" %(nom,anonymat), "w", encoding="utf-8")
writer = csv.writer(datafile, delimiter=";")

textString1 = "Rate the BEAUTY of this image on a scale 1-10. 1 : the least beautiful - - - / 10 : the most beautiful + + +/"
textString2 = "Notez la Beauté de cette image sur une échelle de 1-10; 10 la plus belle"
#textString3 = "Quelle est la taille de cet OBJET ?"
random.shuffle(stim_list)

# mise en place des randomisations

u,v = [textString1 for i in range(len(stim_list)//2)], [textString2 for i in range(len(stim_list)//2)]
rando = u + v
random.shuffle(rando)

## EXPERIMENT TIME
for stimulus in stim_list[:] :
    ## BEGIN ITERATION
    pic = visual.ImageStim(win, "/Users/sophie/Desktop//guppy/queuecouleur/"+list2file(stimulus)+".jpg", ori = 1)
    pic.size = pic.size*(0.14, 0.14)
    pic.pos = (0,0)
    print(counter)

    ## QUESTION 1
    text1 = rando[counter]
    text1 = textString1
    #text1 = "Sur une echelle de 1 à 4, évaluez la beauté de cette image. 1 : la plus belle - 4 la moins belle. Ex : 2314"
    messageQ = visual.TextStim(win, text=text1, units='norm', color='blue')
    messageQ.pos = (0, +0.8)
    messageQ.draw()
    messageR = visual.TextStim(win, text='Your answer/ Votre reponse :', units='norm')
    messageR.pos = (0, -0.8)
    messageR.draw()
    pic.draw()
    win.flip()
    answer1 = list2str(boucle())

    ## QUESTION 2
    text2 = textString2
    pic.draw()
    messageQ = visual.TextStim(win, text=text2, units='norm',color='blue')
    messageQ.pos = (0, +0.8)
    messageQ.draw()
    messageR = visual.TextStim(win, text='Votre reponse :', units='norm')
    messageR.pos = (0, -0.8)
    messageR.draw()
    win.flip()
    answer2 = list2str(boucle())

    ## END ITERATION

    #print([counter, answer1, stimulus[0], stimulus[1]])
    writer.writerow([counter,answer1, [counter], stimulus[0], stimulus[1]])
    counter += 1
    core.wait(1)


## CLOSING SECTION
duration = time.time() - start

messageQ = visual.TextStim(win, text='Your nationality/ Votre nationalité :', units='norm')
messageQ.pos = (0, +0.3)
messageQ.draw()
messageR = visual.TextStim(win, text='', units='norm')
messageR.pos = (0, +0)
messageR.draw()
win.flip()
nationalite = list2str(boucle(x=False))

messageQ = visual.TextStim(win, text='Votre age :', units='norm')
messageQ.pos = (0, +0.3)
messageQ.draw()
messageR = visual.TextStim(win, text='', units='norm')
messageR.pos = (0, +0)
messageR.draw()
win.flip()
age = list2str(boucle(x=False))
print(" The experiment lasted %s minutes."%round(duration/60, 2))
writer.writerow([nom, prenom, nationalite, age, anonymat, round(duration, 2)])
datafile.close()

message1 = visual.TextStim(win, text=' Thanks for your participation ! Merci de votre participation !', units='norm', color='blue', pos=(0,0.3))
message1.draw()
bye =  " To end press ENTER / Pour finir : appuyer sur ENTREE."
mess(bye,(0,-0.3))

win.close()
core.quit()
