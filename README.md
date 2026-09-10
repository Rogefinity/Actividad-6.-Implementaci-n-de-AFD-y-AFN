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

-----------------------------------------
# Ejemplo de un AFD 
payload_afd = {
    "estados": ["q0", "q1"],
    "alfabeto": ["0", "1"],
    "estado_inicial": "q0",
    "estados_finales": ["q1"],
    "transiciones": {
        "q0": {"0": "q1", "1": "q0"},
        "q1": {"0": "q1", "1": "q0"}
    },
    "cadenas": ["10", "111", "000"]
}

# Ejemplo de un AFN
payload_afn = {
    "estados": ["q0", "q1", "q2"],
    "alfabeto": ["0", "1"],
    "estado_inicial": "q0",
    "estados_finales": ["q2"],
    "transiciones": {
        "q0": {"0": ["q0", "q1"], "1": ["q0"]},
        "q1": {"1": ["q2"]},
        "q2": {"0": ["q2"], "1": ["q2"]}
    },
    "cadenas": ["01", "000", "1010"]
}

