# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:11:30 2021

@author: JOSE
"""

from tkinter import *
import pygame
from tkinter import ttk, messagebox
import turtle
import tools


ventana = Tk()
ventana.iconbitmap('navidad.ico')
ventana.title("FELIZ NAVIDAD 2021")
ventana.geometry("800x820")

botonplay= PhotoImage(file="play32.png")
botondetener= PhotoImage(file="stop32.png")
#tools.tkcenter(ventana)
ventana.config(bg='#5B0E2D')


#MUSIC
pygame.mixer.init()
def play():
    pygame.mixer.music.load("audio/jingle.mp3")
    pygame.mixer.music.play(loops=0)
    
def stop():
    pygame.mixer.music.stop()


#CANVAS
canvas = Canvas(ventana, width=800, height=750)
canvas.grid(row=0, columnspan=50)




#Botones

my_button = Button(ventana, image = botonplay, height=60, width=60, compound="top",text="Reproducir",bg="#FFA781", command=play)
stop_button = Button(ventana, image = botondetener , height=60, width=60 , compound="top" , text="Detener",bg="#FFA781", command=stop)

my_button.grid(row=1, column=1)
stop_button.grid(row=1, column=2)


#EMPIEZA EL DIBUJO
t = turtle.RawTurtle(canvas)
t.getscreen().bgcolor("#143D59") #fondo del dibujo


t.penup()
t.goto(-50,-60) #colocar al inicio la pantalla
#comandos -> fd fordward / lt left / bk backward -retroceso / rt right /  círculo -> t.circle(60) / t.dot(20) 
#/ t.penup - ocultar línea / t.pendown - mostrar flecha
# t.undo - deshace el último comando / t.clear / t.rest - reseteo  / t.setheading / 
#árbol de navidad
t.pendown()
#tallo del árbol
t.pen(pencolor="purple",fillcolor="saddlebrown",pensize=2,speed=3)
t.begin_fill()
for i in range(4):
    t.fd(90)
    t.rt(90)
t.end_fill()
t.bk(75) # retroceder

#árbol triángulo 1
t.pen(pencolor="darkolivegreen",fillcolor="darkolivegreen",pensize=2,speed=3)
t.begin_fill()

for i in range(3):
    t.fd(240)
    t.lt(120)
t.end_fill() #fin de triángulo 1

#dirigirse al siguiente triángulo
t.penup()
t.lt(90)
t.fd(120)
t.rt(90)
t.fd(20)
t.pendown()

#árbol triángulo 2
t.begin_fill()
for i in range(3):
    t.fd(200)
    t.lt(120)
t.end_fill()

#dirigirse al siguiente triangulo
t.penup()
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(20)
t.pendown()

#árbol triángulo 3
t.begin_fill()
for i in range(3):
    t.fd(160)
    t.lt(120)
t.end_fill()

# mover hacia la estrella
t.penup()
t.lt(62)
t.fd(120)
t.rt(26)
t.pendown()

#estrella
t.pen(pencolor="yellow",fillcolor="yellow",pensize=2,speed=3)
t.begin_fill()
a = 1
while a<5:
    t.fd(72)
    t.lt(145)
    a= a+1
t.end_fill() #fin de estrella

#mover para las bolas
t.pen(pencolor="red",fillcolor="orangered",pensize=2,speed=3)
t.penup()
t.fd(170)
t.pendown()
t.begin_fill()#1er círculo
t.circle(15)
t.end_fill()
t.lt(90) #rotar entre más alto más arriba
t.penup()
t.fd(85)
t.pendown()
t.begin_fill()#2do círculo
t.circle(15)
t.end_fill()
t.rt(80)#mover 60 - 80
t.penup()
t.fd(90)
t.pendown()
t.begin_fill()#3er círculo
t.circle(15)
t.end_fill()
t.rt(100)
t.penup()
t.fd(80)
t.pendown()
t.begin_fill()#4to círculo
t.circle(15)
t.end_fill()
t.lt(85)
t.penup()
t.fd(100)
t.pendown()
t.begin_fill()#5to círculo
t.circle(15)
t.end_fill()
t.lt(100) #más alto el valor se mueve para arriba
t.penup()
t.fd(130)
t.pendown()
t.begin_fill()#6to círculo
t.circle(15)
t.end_fill()

t.penup()
t.rt(90) #100
t.fd(200) #190
t.pendown()

t.pen(pencolor="dodgerblue",fillcolor="#143D59",pensize=2,speed=0.5) #dodgerblue
t.speed(0.2)
style = ("bold",18,"italic")
style1 = ("Tahoma",52)
t.write("¡FELIZ NAVIDAD!" ,font=style1, align="center")
t.penup()
t.fd(35)
t.pendown()
t.write("Que el espíritu de amor, paz y esperanza de las fiestas" ,font=style,align="center")
t.penup()
t.fd(30)
t.pendown()
t.write("te acompañe durante todo el año. Recuerda que la Navidad" ,font=style,align="center")
t.penup()
t.fd(30)
t.pendown()
t.write("no es solo una fecha sino un estado de ánimo. Te deseo mucha" ,font=style,align="center")
t.penup()
t.fd(30)
t.pendown()
t.write("felicidad y bendiciones para ti y tu familia. Atte. Jose Guzmán" ,font=style,align="center")


t.penup()
t.goto(200,250)
t.pendown()
t.speed(5)

def snowflake(color,x,y):
    t.color(color)
    t.lt(90) #160
    
    for i in range(0,6):
        t.fd(100)
        t.fd(-40)
        t.lt(40)
        t.fd(30)
        t.fd(-30)
        t.rt(80)
        t.fd(30)
        t.fd(-30)
        t.lt(40)
        t.fd(-60)
        t.rt(60)

snowflake("#FF0000",100,100) #FF0000
snowflake("#F4B41A",-100,-100) ##0000FF


ventana.mainloop();