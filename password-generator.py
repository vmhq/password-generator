import random

def generar_contrasena(longitud, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    letras_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if usar_mayusculas else ''
    numeros = '0123456789' if usar_numeros else ''
    simbolos = '!@#$%^&*()-_=' if usar_simbolos else ''
    
    # Combinando todos los caracteres posibles
    caracteres_posibles = letras_minusculas + letras_mayusculas + numeros + simbolos

    # Generando la contraseña
    contrasena = ''.join(random.choice(caracteres_posibles) for i in range(longitud))
    
    return contrasena

# Interacción con el usuario
def main():
    longitud = int(input("Longitud de la contraseña: "))
    contrasena = generar_contrasena(longitud)
    print("Tu nueva contraseña es:", contrasena)

if __name__ == "__main__":
    main()
