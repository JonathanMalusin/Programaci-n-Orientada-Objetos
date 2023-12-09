#Programacion_(POO)
class RegistroClima:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas_diarias.append(temp)

    def calcular_promedio_semanal(self):
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

def main():
    registro_clima = RegistroClima()
    registro_clima.ingresar_temperaturas_diarias()
    promedio_semanal = registro_clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio_semanal}")

if __name__ == "__main__":
    main()