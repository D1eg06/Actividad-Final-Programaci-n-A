from abc import ABC, abstractmethod
def main():
    
    class Futbolista(ABC):
        def __init__(self, nombre, edad, nacionalidad, equipo,goles, asistencias):
            self.nombre = nombre
            self._edad = edad
            self.nacionalidad = nacionalidad
            self.equipo = equipo
            self.goles = goles
            self.asistencias = asistencias
            
        @property
        def edad(self):
            return self._edad
        
        @edad.setter
        def edad(self, nuevaEdad):
            if nuevaEdad < 15 or nuevaEdad > 50:
                print("La edad debe estar entre 15 y 50 años.")
            else:
                self._edad = nuevaEdad

        @abstractmethod
        def __str__(self):
            pass

        @abstractmethod
        def valorMercado(self):
            pass
        
    class Jugar:
        def jugarPartido(self):
            return("Jugando un partido...")
            
    class Entrenar:
        def entrenar(self):
            return("Entrenando para el próximo partido...")
            
    class Delantero(Futbolista, Entrenar, Jugar):
        def __init__(self, nombre, edad, nacionalidad, equipo, goles, asistencias, promedioGoles):
            super().__init__(nombre, edad, nacionalidad, equipo, goles, asistencias)
            self.promedioGoles = promedioGoles

        def __str__(self):
            return (
                f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad} años\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Equipo: {self.equipo}\n"
                f"Goles: {self.goles}\n"
                f"Asistencias: {self.asistencias}\n"
                f"Promedio de Goles: {self.promedioGoles}\n"
                f"{self.entrenar()}\n"
                f"{self.jugarPartido()}\n"        
            )

        def valorMercado(self):
            valor = (self.goles * 1000000) + (self.asistencias * 500000)
            return valor
        
    jugador1 = Delantero("Lionel Messi", 36, "Argentina", "Paris Saint-Germain", 30, 20, 0.75)
    jugador2 = Delantero("Cristiano Ronaldo", 38, "Portugal", "Manchester United", 25, 15, 0.65)
    jugador3 = Delantero("Kylian Mbappé", 25, "Francia", "Paris Saint-Germain", 28, 18, 0.80)
        
    futbolistas = [jugador1, jugador2, jugador3]
      
    print("POLIMORFISMO EN ACCIÓN")  
    for jugador in futbolistas:
        print("-" * 40)
        print(jugador)
        print(f"Valor de Mercado para {jugador.nombre}: ${jugador.valorMercado():,.2f}")
        print("-" * 40)
        
    print("\nENCAPSULAMIENTO")
    print("-" * 40)
    print(f"Edad original de {jugador1.nombre}: {jugador1.edad} años")
    jugador1.edad = 40
    print("\nIntento de edad inválida (60 años):")
    jugador1.edad = 60
    print(f"Edad después de intento inválido: {jugador1.edad} años")
    
if __name__ == "__main__":
    main()