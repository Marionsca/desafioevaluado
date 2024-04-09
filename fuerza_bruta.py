def fuerza_bruta(password):
    intentos = 0
    letras = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(password)):
        for letra in letras:
            intentos += 1
            if letra == password[i]:
                break
    return intentos

password_oculto = input("ingresa la contraseña oculta")
intentos = fuerza_bruta(password_oculto)
print(f"se necesitaron {intentos} intentos para encontrar la contraseña {password_oculto}")