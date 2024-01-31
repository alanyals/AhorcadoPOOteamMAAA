class AhorcadoGame:
    def __init__(self):
        self.palabra_secreta = self.obtener_palabra()
        self.letras_adivinadas = []
        self.intentos_maximos = 6
        self.intentos = 0

    def obtener_palabra(self):
        palabras = ["python", "programacion", "computadora", "codigo", "tecnologia", "ahorcado"]
        return palabras[5]

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
        print(self.mostrar_palabra())

        while True:
            letra = input("Adivina una letra: ")

            self.letras_adivinadas.append(letra)

            if letra not in self.palabra_secreta:
                self.intentos += 1
                self.dibujar_ahorcado()
                print("Letra incorrecta,. Intentos restantes:", self.intentos_maximos - self.intentos)
            else:
                print("¡whoosh, letra correcta!")

            palabra_mostrada = self.mostrar_palabra()
            print(palabra_mostrada)

            if palabra_mostrada.replace(" ", "") == self.palabra_secreta:
                print("¡Que pro!, le has dado a la palabra.")
                break

            if self.intentos == self.intentos_maximos:
                print("Este no era tu momento, has agotado los intentos. Tu palabra secreta era:", self.palabra_secreta)
                break

if __name__ == "__main__":
    juego = AhorcadoGame()
    juego.jugar()
