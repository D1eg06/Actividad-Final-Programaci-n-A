# 🏟️ Sistema de Gestión de Futbolistas Profesionales

Actividad Final Corte #1 — Programación Orientada a Objetos con Python  
**Facultad de Ingeniería de Sistemas — Universidad de La Guajira**

---

## 📖 Descripción de la analogía

Se modela un **sistema de gestión de futbolistas profesionales**. La analogía representa el mundo del fútbol, donde cada jugador tiene una identidad base (nombre, edad, nacionalidad), estadísticas de rendimiento (goles, asistencias, partidos jugados) y un contrato vigente con un club (equipo, salario, duración). A partir de estos tres pilares se construye el perfil completo de un futbolista profesional, incluyendo el cálculo estimado de su valor de mercado.

---

## 🗂️ Estructura del proyecto

```
nivelacion_python/
│
└── actividad_final_C1.py   # Script principal con toda la implementación
```

---

## 🧱 Arquitectura de clases

| Clase | Tipo | Descripción |
|---|---|---|
| `Futbolista` | Abstracta (ABC) | Clase padre. Define atributos base y declara `__str__` y `valorMercado` como métodos abstractos. |
| `Estadisticas` | Independiente | Gestiona goles, asistencias y partidos jugados. Calcula el promedio de contribuciones por partido. |
| `Contrato` | Independiente | Gestiona el equipo, la vigencia del contrato y el salario del jugador. |
| `FutbolistaProfesional` | Herencia múltiple | Hereda de `Futbolista`, `Estadisticas` y `Contrato`. Implementa los métodos abstractos y aplica encapsulamiento robusto con `@property`. |

---

## ▶️ Cómo ejecutar

### Requisitos

- Python **3.8** o superior
- No se requieren dependencias externas (solo librería estándar `abc`)

### Pasos

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/<tu-usuario>/nivelacion_python.git
   cd nivelacion_python
   ```

2. Ejecuta el script:
   ```bash
   python actividad_final_C1.py
   ```

### Salida esperada

El programa imprimirá en consola:

- La ficha completa de **3 jugadores** (Mbappé, Modric, Alisson), demostrando polimorfismo con `__str__` y `valorMercado()`.
- Una sección de **encapsulamiento** donde se lee y modifica la posición de un jugador a través de su setter, y se captura un error al intentar asignar una posición inválida (`"Arquero"`).
- Una demostración similar con el atributo `edad`, asignando un valor válido y luego intentando uno fuera del rango permitido (> 50).

---

## ✅ Conceptos de POO aplicados

- **Abstracción:** `Futbolista` es una clase abstracta que obliga a sus subclases a implementar `__str__` y `valorMercado`.
- **Herencia múltiple:** `FutbolistaProfesional` hereda de tres clases usando el orden MRO de Python.
- **Encapsulamiento:** Atributos privados (`__edad`, `__goles`, `__salario`, etc.) y protegidos (`_nombre`, `_posicion`, etc.) con acceso controlado por `@property` y validaciones en los setters.
- **Polimorfismo:** Los métodos `__str__` y `valorMercado()` se invocan uniformemente sobre objetos distintos iterando una lista.

---

## 🏷️ Convención de nombres

Se utiliza **camelCase** de forma consistente en todos los identificadores del proyecto (atributos, métodos, variables locales), siguiendo las indicaciones de la actividad.
