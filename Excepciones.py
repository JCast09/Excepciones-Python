#Se define la clase para calcular divisores
class CalculadoraDivisores:
    #Se define el metodo para ingresar el numero utilizando excepciones
    def ingresarNumero(self):
        while True:
            try:
                num = int(input("Ingrese un número natural: "))
                if num < 1:
                    raise ValueError("El número debe ser natural (mayor que 0).")
                return num
            except ValueError as e:
                print(f"Entrada inválida: {e}. Intente de nuevo.")

    #Se define el metodo para calcular los divisores
    def calcular_divisores(self, numero):
        return [i for i in range(1, numero + 1) if numero % i == 0]

    #Se muestran los divisores
    def mostrar_divisores(self):
        numero = self.ingresarNumero()
        divisores = self.calcular_divisores(numero)
        print(f"Los divisores de {numero} son: {divisores}")

def main():
    calculadora = CalculadoraDivisores()
    calculadora.mostrar_divisores()

if __name__ == "__main__":
    main()
