class AhorcadoGame:
    def __init__(self):
        # Se añadió un diccionario de palabras con pistas para seleccionar la palabra y su pista de forma aleatoria
        self.palabras = {
            "python": "Lenguaje de programación popular",
            "programacion": "Creación de algoritmos para resolver problemas",
            "computadora": "Dispositivo electrónico para procesar datos",
            "codigo": "Conjunto de instrucciones en un programa",
            "tecnologia": "Conjunto de conocimientos técnicos aplicados",
            "ahorcado": "Juego clásico de adivinar palabras"
        }
        self.palabra_secreta, self.pista = self.obtener_palabra()  # Modificado para usar el nuevo método que incluye pistas
        self.letras_adivinadas = []
        self.intentos_maximos = 6
        self.intentos = 0

    def obtener_palabra(self):
        # Modificado para seleccionar una palabra y su pista de forma aleatoria del diccionario añadido en __init__
        import random
        
        palabra = random.choice(list(self.palabras.keys()))  # Corregido para usar self.palabras
        pista = self.palabras[palabra]  # Corregido para usar self.palabras
        return palabra, pista
        
        #pista = palabras[palabra]

    def mostrar_palabra(self):
        resultado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado.strip()

    def dibujar_ahorcado(self):
        # Sin cambios significativos en la lógica, pero esencial para integrar con el nuevo sistema de intentos
        estados = [
            "  ____\n |    |\n |    O\n |   /|\\\n |   / \\\n |_________",
            "  ____\n |    |\n |    O\n |   /|\\\n |   /\n |_________",
            "  ____\n |    |\n |    O\n |   /|\\\n |\n |_________",
            "  ____\n |    |\n |    O\n |   /|\n |\n |_________",
            "  ____\n |    |\n |    O\n |    |\n |\n |_________",
            "  ____\n |    |\n |    O\n |\n |\n |_________",
            "  ____\n |    |\n |\n |\n |\n |_________",
        ]
        print(estados[self.intentos])

    def jugar(self):
        print("Bienvenido al AhorcadoGame. Intenta adivinar la palabra.")
        # Se añade la impresión de la pista al inicio del juego
        print(f"Pista: {self.pista}")
        print(self.mostrar_palabra())

        while True:
            letra = input("Adivina una letra: ").lower()

            if letra in self.letras_adivinadas:
                print("Ya has intentado con esa letra. Prueba con otra.")
                continue

            self.letras_adivinadas.append(letra)

            if letra not in self.palabra_secreta:
                self.intentos += 1
                print("Letra incorrecta. Intentos restantes:", self.intentos_maximos - self.intentos)
                self.dibujar_ahorcado()  # La llamada a dibujar_ahorcado se mantiene igual pero se integra con los intentos ajustados
            else:
                print("¡Correcto! Esa letra está en la palabra.")

            palabra_mostrada = self.mostrar_palabra()
            print(palabra_mostrada)

            if "_" not in palabra_mostrada:
                print("¡Felicidades! Has ganado, la palabra era:", self.palabra_secreta)
                break

            if self.intentos >= self.intentos_maximos:
                print("Lo siento, has perdido. La palabra era:", self.palabra_secreta)
                break

if __name__ == "__main__":
    juego = AhorcadoGame()
    juego.jugar()
