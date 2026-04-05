#Diego Quintero y Juan Arenas

from abc import ABC, abstractmethod

def main():

    class Futbolista(ABC):
        def __init__(self, nombre, edad, nacionalidad):
            self._nombre = nombre
            self.__edad = edad
            self._nacionalidad = nacionalidad
        
        @property
        def nombre(self):
            return self._nombre
        
        @nombre.setter
        def nombre(self, nuevoNombre):
            self._nombre = nuevoNombre

        @property
        def edad(self):
            return self.__edad
        
        @edad.setter
        def edad(self, nuevaEdad):
            if nuevaEdad < 15 or nuevaEdad > 50:
                raise ValueError("La edad debe estar entre 15 y 50 años.")
            self.__edad = nuevaEdad
            
        @property 
        def nacionalidad(self):
            return self._nacionalidad
        
        @nacionalidad.setter
        def nacionalidad(self, nuevaNacionalidad):
            self._nacionalidad = nuevaNacionalidad

        @abstractmethod
        def __str__(self):
            pass
            
        @abstractmethod
        def valorMercado(self):
            pass

        
    class Estadisticas:
        def __init__(self, goles, asistencias, partidosJugados):
            self.__goles = goles
            self.__asistencias = asistencias
            self._partidosJugados = partidosJugados
            
        @property
        def goles(self):
            return self.__goles
        
        @goles.setter
        def goles(self, nuevosGoles):
            if nuevosGoles < 0:
                raise ValueError("Los goles deben ser un número entero no negativo.")
            self.__goles = nuevosGoles
        
        @property
        def asistencias(self):
            return self.__asistencias
        
        @asistencias.setter
        def asistencias(self, nuevasAsistencias):
            if nuevasAsistencias < 0:
                raise ValueError("Las asistencias deben ser un número entero no negativo.")
            self.__asistencias = nuevasAsistencias
        
        @property
        def partidosJugados(self):
            return self._partidosJugados
        
        @partidosJugados.setter
        def partidosJugados(self, nuevosPartidos):
            if nuevosPartidos < 0:
                raise ValueError("Los partidos jugados deben ser un número entero no negativo.")
            self._partidosJugados = nuevosPartidos
            
        def promedioGolesYAsistencias(self):
            if self._partidosJugados == 0:
                return 0
            return (self.__goles + self.__asistencias) / self._partidosJugados

        def estadisticasCompletas(self):
            return (
                f"Goles: {self.__goles}\n"
                f"Asistencias: {self.__asistencias}\n"
                f"Partidos Jugados: {self._partidosJugados}\n"
                f"Promedio Goles y Asistencias por Partido: {self.promedioGolesYAsistencias():.2f}\n"
            )
            
            
    class Contrato:
        def __init__(self, equipo, vigenciaDeContrato, salario):
            self._equipo = equipo
            self.__vigenciaDeContrato = vigenciaDeContrato
            self.__salario = salario
        
        @property
        def equipo(self):
            return self._equipo
        
        @equipo.setter
        def equipo(self, nuevoEquipo):
            self._equipo = nuevoEquipo
        
        @property
        def vigenciaDeContrato(self):
            return self.__vigenciaDeContrato
        
        @vigenciaDeContrato.setter
        def vigenciaDeContrato(self, nuevaVigenciaDeContrato):
            if nuevaVigenciaDeContrato <= 0:
                raise ValueError("La duración del contrato debe ser un número entero positivo.")
            self.__vigenciaDeContrato = nuevaVigenciaDeContrato
        
        @property
        def salario(self):  
            return self.__salario
            
        @salario.setter
        def salario(self, nuevoSalario):
            if nuevoSalario < 0:
                raise ValueError("El salario debe ser un número no negativo.")
            self.__salario = nuevoSalario

            
        def contratoCompleto(self):
            return (
                f"Equipo: {self._equipo}\n"
                f"Vigencia de Contrato: {self.__vigenciaDeContrato} años\n"
                f"Salario: ${self.__salario:,.2f}\n"
            )
            
    class FutbolistaProfesional(Futbolista, Estadisticas, Contrato):
        def __init__(self, nombre, edad, nacionalidad,
                     goles, asistencias, partidosJugados, 
                     equipo, vigenciaDeContrato, salario, posicion):
            Futbolista.__init__(self, nombre, edad, nacionalidad)
            Estadisticas.__init__(self, goles, asistencias, partidosJugados)
            Contrato.__init__(self, equipo, vigenciaDeContrato, salario)
            self._posicion = posicion
            
        @property   
        def posicion(self):
            return self._posicion
        
        @posicion.setter    
        def posicion(self, nuevaPosicion):
            if nuevaPosicion.lower() not in ["portero", "defensa", "centrocampista", "delantero"]:
                raise ValueError("La posición debe ser una de las siguientes: Portero, Defensa, Centrocampista, Delantero.")
            self._posicion = nuevaPosicion
            
        def __str__(self):
            return (
                f"Nombre: {self.nombre}\n"
                f"Edad: {self.edad} años\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Posición: {self._posicion}\n"
                f"{self.estadisticasCompletas()}"
                f"{self.contratoCompleto()}"
            )
            
        def valorMercado(self):
            valorBase = 1000000
            valorGoles = self.goles * 50000
            valorAsistencias = self.asistencias * 30000
            valorExperiencia = self.partidosJugados * 20000
 
            if self.edad < 23:
                valorEdad = 500000   
            elif self.edad <= 29:
                valorEdad = 300000   
            elif self.edad <= 33:
                valorEdad = 100000   
            else:
                valorEdad = -200000  
 
            valorTotal = valorBase + valorGoles + valorAsistencias + valorExperiencia + valorEdad
 
            if self._posicion.lower() == "delantero":
                valorTotal *= 1.2
            elif self._posicion.lower() == "centrocampista":
                valorTotal *= 1.1
            elif self._posicion.lower() == "defensa":
                valorTotal *= 0.9
            elif self._posicion.lower() == "portero":
                valorTotal *= 0.8
 
            return f"Valor de Mercado Estimado: ${valorTotal:,.2f}"
        
    jugador1 = FutbolistaProfesional(
        nombre="kylian Mbappe",
        edad=25,
        nacionalidad="Francia",
        goles=30,
        asistencias=20,
        partidosJugados=50,
        equipo="Real Madrid",
        vigenciaDeContrato=2,
        salario=41000000,
        posicion="Delantero"
    )
    
    jugador2 = FutbolistaProfesional(
        nombre="Luka Modric",
        edad=39,
        nacionalidad="Croacia",
        goles=15,
        asistencias=10,
        partidosJugados=45,
        equipo="Milan",
        vigenciaDeContrato=1,
        salario=25000000,
        posicion="Centrocampista"
    )
    
    jugador3 = FutbolistaProfesional(
        nombre="Alisson Becker",
        edad=31,
        nacionalidad="Brasil",
        goles=1,
        asistencias=2,
        partidosJugados=40,
        equipo="Liverpool",
        vigenciaDeContrato=3,
        salario=18000000,
        posicion="Portero"
    )
    
    jugadores = [jugador1, jugador2, jugador3]
    
    for jugador in jugadores:
        print("-" * 40)
        print("Polimorfismo en acción: __str__ y valorMercado()")
        print(jugador)
        print(jugador.valorMercado())
        print("-" * 40)
        
    print("-"*40)
    print("  ENCAPSULAMIENTO")
    print("-"*40)
    print(f"Posición actual de {jugador1.nombre}: {jugador1.posicion}")
    
    jugador1.posicion = "Centrocampista"
    print(f"Posición actualizada     : {jugador1.posicion}")
    
    print("\nIntento de asignar posición inválida ('Arquero'):")
    try:
        jugador1.posicion = "Arquero"
    except ValueError as e:
        print(f"  Error capturado → {e}")
 
    print(f"\nEdad actual de {jugador3.nombre}: {jugador3.edad}")
    jugador3.edad = 39
    print(f"Edad actualizada: {jugador3.edad}")
 
    print("\nIntento de asignar edad inválida (60):")
    try:
        jugador3.edad = 60
    except ValueError as e:
        print(f"  Error capturado → {e}")
    
if __name__ == "__main__":
    main()