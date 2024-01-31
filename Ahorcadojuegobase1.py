import time
import sys
import random

class AhorcadoGame:
    def __init__(self):
        self.palabras = {
            "python": "Lenguaje de programación popular",
            "programacion": "Creación de algoritmos para resolver problemas",
            "computadora": "Dispositivo electrónico para procesar datos",
            "codigo": "Conjunto de instrucciones en un programa",
            "tecnologia": "Conjunto de conocimientos técnicos aplicados",
            "ahorcado": "Juego clásico de adivinar palabras"
        }
        self.palabra_secreta, self.pista = self.obtener_palabra()
        self.letras_adivinadas = []
        self.letras_incorrectas = []
        self.intentos_maximos = 6
        self.intentos = 0
        self.tiempo_inicio = None  # Nueva variable para almacenar el tiempo de inicio

    def obtener_palabra(self):
        palabra = random.choice(list(self.palabras.keys()))
        pista = self.palabras[palabra]
        return palabra, pista

    def mostrar_palabra(self):
        resultado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado.strip()

    def dibujar_ahorcado(self):
        if self.intentos == 0:
            print("  __")
            print(" |    |")
            print(" |")
            print(" |")
            print(" |")
            print(" |___")
        elif self.intentos == 1:
            print("  __")
            print(" |    |")
            print(" |    O")
            print(" |")
            print(" |")
            print(" |___")
        elif self.intentos == 2:
            print("  __")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |")
            print(" |___")
        elif self.intentos == 3:
            print("  __")
            print(" |    |")
            print(" |    O")
            print(" |   /|")
            print(" |")
            print(" |___")
        elif self.intentos == 4:
            print("  __")
            print(" |    |")
            print(" |    O")
            print(" |   /|\\")
            print(" |")
            print(" |___")
        elif self.intentos == 5:
            print("  __")
            print(" |    |")
            print(" |    O")
            print(" |   /|\\")
            print(" |   /")
            print(" |___")
        elif self.intentos == 6:
            print("  __")
            print(" |    |")
            print(" |    O")
            print(" |   /|\\")
            print(" |   / \\")
            print(" |___")

    def jugar(self):
        print("¿Jugamos AhorcadoGame?")
        print("Adivina la palabra oculta letra por letra. ¡Suerte UwU!")
        print(f"Pista: {self.pista}")
        print(self.mostrar_palabra())

        self.tiempo_inicio = time.time()  # Registra el tiempo de inicio

        while True:
            letra = input("Adivina una letra: ").lower()

            if letra in self.letras_adivinadas:
                print("Ya has intentado con esa letra. Prueba con otra.")
                continue

            if letra in self.letras_adivinadas or letra in self.letras_incorrectas:
                print("Ya has intentado esa letra. Intenta con otra.")
                continue

            if letra not in self.palabra_secreta:
                self.letras_incorrectas.append(letra)
                self.intentos += 1
                self.dibujar_ahorcado()
                print(f"Letra incorrecta. Letras incorrectas: {', '.join(self.letras_incorrectas)}")
                print("Intentos restantes:", self.intentos_maximos - self.intentos)
            else:
                self.letras_adivinadas.append(letra)
                print("¡Correcto! Esa letra está en la palabra.")

            palabra_mostrada = self.mostrar_palabra()
            print(palabra_mostrada)

            if palabra_mostrada.replace(" ", "") == self.palabra_secreta:
                tiempo_final = time.time()  # Registra el tiempo final
                tiempo_total = tiempo_final - self.tiempo_inicio
                
                print(f"¡Felicidades! Has ganado, la palabra era: {self.palabra_secreta}")
                print(f"Tiempo total: {tiempo_total:.2f} segundos")
                break

            if self.intentos == self.intentos_maximos:
                print(f"Este no era tu momento, has agotado los intentos. La palabra era: {self.palabra_secreta}")
                break
    
        print("Juego terminado. Cerrando en 5 segundos...")
        time.sleep(5)
        sys.exit()

if __name__ == "__main__":
    juego = AhorcadoGame()
    juego.jugar()