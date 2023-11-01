from random import choice
from turtle import *



def carre(n):
    for i in range(4):
        forward (n)
        left(90)

def ligne_de_carre(nb,t):
    for i in range(nb):
        carre(t)
        up()
        forward(t+10)
        down()

def dessin(nb,t):
    for i in range(nb):
        ligne_de_carre(nb,t)
        up()
        left(90)
        right(10)
        forward(t+20)
        down()        
    
    
    
        
        

