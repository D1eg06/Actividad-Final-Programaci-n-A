## Descripción de la Analogía

Este proyecto modela un sistema de **gestión de futbolistas** usando los principios de la Programación Orientada a Objetos (POO) en Python. La analogía principal es el mundo del fútbol profesional, donde un **Delantero** es un tipo especializado de futbolista que combina habilidades de juego y entrenamiento.

La jerarquía de clases es la siguiente:

```
Futbolista (ABC - clase abstracta)
Jugar      (clase independiente: representa la capacidad de jugar partidos)
Entrenar   (clase independiente: representa la capacidad de entrenamiento)
    └── Delantero (herencia múltiple de las tres anteriores)
```

---

## Estructura del Proyecto

```
nivelacion_python/
├── futbolista.py   # Contiene todas las clases y el bloque de prueba principal
└── README.md       # Este archivo
```

---

## Requisitos

- Python 3.8 o superior
- No se requieren dependencias externas (solo módulos estándar de Python: `abc`)

---

## Cómo Ejecutar

1. Clona el repositorio y navega a la carpeta del proyecto:

```bash
git clone <url-del-repositorio>
cd nivelacion_python
```

2. Ejecuta el script principal:

```bash
python futbolista.py
```

El bloque `if __name__ == "__main__":` al final del archivo activa automáticamente las pruebas, las cuales demuestran:

- **Polimorfismo:** se itera sobre una lista de objetos `Delantero` y se invocan los métodos `__str__` y `valorMercado()` heredados de la clase abstracta.
- **Encapsulamiento:** se lee y modifica el atributo protegido `_edad` a través de su `@property` y `@edad.setter`, incluyendo la validación que rechaza edades fuera del rango permitido (15–50 años).

---

## Ejemplo de Salida Esperada

```
POLIMORFISMO EN ACCIÓN
----------------------------------------
Nombre: Lionel Messi
Edad: 36 años
...
Valor de Mercado para Lionel Messi: $40,000,000.00
----------------------------------------

ENCAPSULAMIENTO
----------------------------------------
Edad original de Lionel Messi: 36 años
Intento de edad inválida (60 años):
La edad debe estar entre 15 y 50 años.
Edad después de intento inválido: 40 años
```

---

## Convención de Nombres

Se utilizó **camelCase** de forma consistente en todos los atributos y métodos del proyecto (por ejemplo: `valorMercado`, `promedioGoles`, `nuevaEdad`).

---

## Conceptos de POO Aplicados

| Concepto | Implementación |
|---|---|
| Clase abstracta | `Futbolista` con `ABC` y `@abstractmethod` |
| Herencia múltiple | `Delantero(Futbolista, Entrenar, Jugar)` |
| Encapsulamiento | Atributo `_edad` con `@property` y `@edad.setter` |
| Polimorfismo | Iteración sobre lista de objetos llamando métodos heredados |
| Validación | El setter de `edad` rechaza valores fuera del rango 15–50 |