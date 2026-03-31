import turtle
from time import sleep
from turtle import *

c = Turtle()

#funções das formas geométricas 

#função para contornar as bandeiras
def contorno(x, y ,largura , comprimento):
    c.color('black')
    c.pu()
    c.goto(x , y)
    c.down()
    for _ in range(2):
            c.fd(largura)
            c.left(90)
            c.fd(comprimento)
            c.left(90)

#função para desenhar um circulo
def circulo(x , y , cor , raio):
    c.pu()
    c.goto(x, y)
    c.down()
    c.color(cor)
    c.begin_fill()
    c.circle(raio)
    c.end_fill()

#função para desenhar um retangulo
def retangulo(x , y , cor , largura , comprimento):
    c.pu()
    c.goto(x , y)
    c.down()
    c.color(cor)
    c.begin_fill()
    for _ in range(2):
        c.left(90)
        c.fd(largura)
        c.left(90)
        c.fd(comprimento)
    c.end_fill()
   
#função para desenhar um triangulo
def triangulo(x , y , cor , largura ):
    c.pu()
    c.goto( x , y)
    c.down()
    c.color(cor)
    c.begin_fill()
    for _ in range(3):
        c.fd(largura)
        c.left(120)
    c.end_fill()
  
#função para desenhar uma estrela
def estrela(x, y , cor , largura, comprimento):
    c.pu()
    c.goto(x , y)
    c.color(cor)
    c.begin_fill()
    c.fillcolor()
    c.down()
    c.right(35)
    for _ in range(5):
        c.fd(largura)
        c.right(72)
        c.fd(comprimento)
        c.left(144)
    c.end_fill()
    c.left(35)

# Funções das bandeiras

def japao():
    contorno(- 150 , 0 , 300 , 200)
    circulo(0 , 50 , 'red', 50)
    sleep(5)
    c.clear()

def irlanda():
    retangulo(- 50 , 0 , 'green' , 200 , 100)
    retangulo(150 , 0 , 'orange' , 200 , 100)
    contorno(- 150 , 0 , 300 , 200)
    sleep(5)
    c.clear()

def niger():
    c.right(90)
    retangulo( - 150 , 0 , 'green' , 300 , 70 )
    retangulo( - 150 , 140, '#FF8C00' , 300 , 70)
    c.left(90)
    circulo(0 , 75 , '#FF8C00' , 30)
    contorno( -150 , 0 , 300, 210)
    sleep(5)
    c.clear()

def emirados_arabes():
    c.right(90)
    retangulo( - 150 , 0 , 'black' , 300 , 70)   
    retangulo( - 150 , 140 , '#006400' , 300 , 70)  
    retangulo( - 250 , 0 , '#8B0000' , 100 , 210) 
    c.left(90)
    contorno( - 250 , 0 , 400 , 210)
    sleep(5)
    c.clear()

def bahamas():
    c.right(90)
    retangulo(-150 , 0  , '#4682B4' , 300 , 210)
    retangulo(-150 , 70 , 'yellow' , 300 , 70)
    triangulo(- 150 , 210 , 'black', 210) 
    c.left(90)
    contorno( - 150 , 0 , 300 , 210)
    sleep(5)
    c.clear()
     
def senegal():
    c.right(90)
    retangulo( - 150 , 0 , 'yellow' , 300 , 200)
    c.left(90)
    retangulo( - 50 , 0 , 'green' , 200, 100)
    retangulo(150 , 0 , 'red' , 200 , 100)
    estrela(-25,100 , 'green',20 , 20)
    contorno(-150 , 0 , 300 , 200)
    sleep(5)
    c.clear()

def cuba():
    c.right(90)
    retangulo(- 150 , 0 , '#140778' , 300 , 200)
    retangulo(-150 , 40 , 'white' , 300 , 40)
    retangulo(-150,120, 'white' , 300 , 40)
    triangulo(- 150,200 , '#ad0707' , 200)
    c.left(90)
    estrela(- 120,110, 'white' , 20, 20)
    contorno(-150 , 0 , 300 , 200)
    sleep(5)
    c.clear()
    

def noruega():
    c.right(90)
    retangulo(-150 , 0 , 'red' , 300 , 200)
    retangulo(-150 , 75 , 'white', 300 , 50)
    c.left(90)
    retangulo(-50, 0 , 'white' , 300 , 50)
    c.right(90)
    retangulo(-150 , 88, '#09078a', 300 , 25)
    c.left(90)
    retangulo(- 65 , 0  , '#09078a' , 200 , 20)
    contorno(-150 , 0 , 300 , 200)
    sleep(5)
    c.clear()

def africa_do_sul():
    c.right(90)
    retangulo(-150 , 0 , '#1e0a8f' , 300 , 70)
    retangulo(- 150 , 140 , '#b01409' , 300 , 70)
    triangulo( - 150 , 210 ,'white', 210)
    retangulo(- 150 , 85 , '#1f800b' , 300 , 40)
    triangulo(- 150 , 195 ,'#1f800b' , 180 )
    triangulo( - 150 , 165 , '#e8b62c' , 120 )
    triangulo( - 150 , 140 , 'black' , 70) 
    c.left(90)
    contorno(-150 , 0 , 300 , 210)
    sleep(5)
    c.clear()

def republica_centro_africana():
    c.right(90)
    retangulo(- 150 , 0  , '#e8c61e' , 300  , 50)
    retangulo(- 150 , 50 , '#369920' , 300 ,50)
    retangulo(- 150 , 150 , '#202899' , 300 , 50)
    c.left(90)
    retangulo( 30 , 0 , '#b8170b' , 200 , 60)
    estrela(- 120 , 180 , '#e8c61e' , 15, 15 )
    contorno(- 150 , 0 , 300 , 200)
    sleep(5)
    c.clear()

#chamando as funções das bandeiras com textinput (extra)

bandeira_escolhida = textinput('Bandeiras', 'Escolha uma bandeira entre: Japão, Irlanda, Niger, Bahamas, Emirados Árabes , Senegal , Cuba , Noruega , África do Sul e República Centro Africana')

if bandeira_escolhida == 'Japão':
    japao()
elif bandeira_escolhida == 'Irlanda':
    irlanda()
elif bandeira_escolhida == 'Niger':
    niger()
elif bandeira_escolhida == 'Bahamas':
    bahamas()
elif bandeira_escolhida == 'Emirados Árabes':
    emirados_arabes()
elif bandeira_escolhida == 'Senegal':
    senegal()
elif bandeira_escolhida == 'Cuba':
    cuba()
elif bandeira_escolhida == 'Noruega':
    noruega()
elif bandeira_escolhida == 'África do Sul':
    africa_do_sul()
elif bandeira_escolhida == 'República Centro Africana':
    republica_centro_africana
else: 
    print('Não é possível desenhar essa bandeira')    