import random

respuesta= int(input("¿Responde a estimulo?"))

if respuesta == "si":
    print("valorar la necesidad de llevarlo al hospital mas cercano")
elif respuesta == "no":
    print("Abrir la via aerea")

print("¿Respira?")
if respuesta == "si":
    print("Permitirle posicion de suficiente ventilacion")
elif respuesta == "no":
    print("Administrar 5 ventilaciones y llamar a ambulancia")

print("¿Signos de vida?")
if respuesta == "si":
    print("Reevaluar a la espera de la ambulancia")
elif respuesta == "no":
    print("Administrar compresiones toracicas hasta que llegue ambulancia")

