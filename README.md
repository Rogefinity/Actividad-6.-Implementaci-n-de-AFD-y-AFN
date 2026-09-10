Actividad 6. Implementación de evaluador de cadenas para un AFD y AFN

# Actividad 6. Implementación de evaluador de cadenas para un AFD y AFN

## Identificación del Estudiante
* **Nombre:** Rogelio Sotomayor Carrasco
* **No. de Cuenta:** 195721
* **Materia:** Lenguajes de Programación
* **Actividad:** Actividad 6 - Evaluador AFD y AFN

## Desarrollo y Resultados
Este repositorio contiene una API desarrollada en FastAPI que evalúa cadenas sobre Autómatas Finitos Deterministas (AFD) y Autómatas Finitos No Deterministas (AFN).

### Endpoints Disponibles
* `POST /afd`: Recibe la definición formal del AFD y una lista de cadenas. Evalúa de forma lineal.
* `POST /afn`: Recibe la definición formal del AFN (con múltiples caminos posibles por símbolo) y evalúa generando conjuntos de estados activos.

