
# Generador de Contraseñas en Python 🐍🔐

Este proyecto es un simple pero efectivo generador de contraseñas en Python. Puede generar contraseñas seguras y aleatorias, personalizables según tus necesidades.

## Funcionalidades 🌟

- **Generación de Contraseñas Aleatorias**: Crea contraseñas que combinan letras, números y símbolos.
- **Personalización**: Elige la longitud de la contraseña y qué tipos de caracteres incluir.

## Cómo Funciona 🤖

El programa consta de varias partes:

1. **Importación de la Biblioteca Random**: Usamos `random` para generar caracteres aleatorios.
2. **Definición de Caracteres**: Establecemos cadenas de caracteres que se pueden usar en la contraseña, incluyendo letras mayúsculas, minúsculas, números y símbolos.
3. **Función Generar Contraseña**: Se crea una función que selecciona aleatoriamente caracteres de las cadenas definidas para formar la contraseña.
4. **Interacción con el Usuario**: El usuario puede especificar la longitud de la contraseña y qué tipos de caracteres incluir.

### Ejemplo de Código

```python
import random

def generar_contrasena(longitud, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    # ... (definición de la función)
    return contrasena

# Código para interacción con el usuario
longitud = int(input("Longitud de la contraseña: "))
contrasena = generar_contrasena(longitud)
print("Tu nueva contraseña es:", contrasena)
```

## Cómo Empezar 🚀

1. Clona este repositorio o descarga el archivo `.py`.
2. Ejecuta el programa en tu entorno de Python.
3. Sigue las instrucciones en pantalla para generar tu contraseña.

## Contribuciones 🤝

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o mejora, siéntete libre de hacer un 'pull request' o abrir un 'issue'.

## Licencia 📄

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---
Creado con ❤️ y Python.
```
