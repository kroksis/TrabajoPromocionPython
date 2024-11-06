#trabajo de promoción de gestión de software
#crear un programa de preguntas con opciones de respuesta a cerca de python, cada respuesta correcta suma 2 puntos
#informar si el alumno aprobó o desaprobó
import time
preguntas = ["¿Qué comando muestra texto en la pantalla en Python?" , "¿Con qué símbolo comienzan los comentarios en Python?" , "¿Cómo defines una variable en Python?" , "¿Cómo se indica el final de una línea de código en Python?" , "¿Cuál de estos números es de tipo float en Python?"]
respuestas = ["b" , "b" , "c" , "b" , "d"]
opciones=["""a) escribir
b) print 
c) mostrar
d) display""" ,
"""a) // 
b) #
c) **
d) @""" ,
"""a) var x
b) int x
c) x = 5
d) x := 5""" ,
"""a) ;
b) Nueva Linea
c) ,
d) :""" ,
"""a) 3
b) 10
c) -5
d) 4,5"""]
nota = 0
correctas = 0
incorrectas= 0
print ("""█████▄░█████▄░▄█████░▄██████░██░░░██░██████▄░████████░▄████▄░██████▄░▄█████▄░▄██████░██
██░░██░██░░██░██░░░░░██░░░░░░██░░░██░██░░░██░░░░██░░░░██░░██░██░░░██░██░░░██░██░░░░░░██
█████▀░█████▀░█████░░██░░███░██░░░██░██░░░██░░░░██░░░░██░░██░██░░░██░██░░░██░▀█████▄░██
██░░░░░██░░██░██░░░░░██░░░██░██░░░██░██░░░██░░░░██░░░░██████░██░░░██░██░░░██░░░░░░██░░░
██░░░░░██░░██░▀█████░▀█████▀░▀█████▀░██░░░██░░░░██░░░░██░░██░██████▀░▀█████▀░██████▀░██
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                            1---> Jugar
                            2---> Salir""")
numero=int(input("introducir elección: "))
if numero == 2:
    print ("has decidido no jugar,nos apena tu decision ;( ")
    exit()
else:
    for x in range(5):
        print (preguntas[x])
        print ("")
        print (opciones[x])
        print ("")
        respuesta=input("ingresar respuesta:")
        if respuesta == respuestas[x]:
            nota = nota + 2
            correctas = correctas + 1
            print ("Correcto! (+2)")
        else:
            incorrectas= incorrectas + 1
            print("Incorrecto 💔 (+0)")     


print ("Felicidades! has llegado al final del juego,a continuacion se mostrara tu puntaje")
time.sleep(2)
print ("")
print (f"a traves de tus correctas ({correctas}) y tus incorrectas ({incorrectas}) se define que acertaste {correctas}/5")
print (f"tu puntaje final fue: {nota}")

