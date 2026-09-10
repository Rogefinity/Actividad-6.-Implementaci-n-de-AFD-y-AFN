from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Union

app = FastAPI(title="Evaluador de Autómatas (AFD y AFN)")

class AutomataRequest(BaseModel):
    estados: List[str]
    alfabeto: List[str]
    estado_inicial: str
    estados_finales: List[str]
    transiciones: Dict[str, Dict[str, Union[str, List[str]]]]
    cadenas: List[str]

#AFD
@app.post("/afd")
def evaluar_afd(req: AutomataRequest):
    resultados = []
    
    for cadena in req.cadenas:
        estado_actual = req.estado_inicial
        camino = [estado_actual]
        valida = True
        
        for char in cadena:
            #validar que el caracter pertenezca al alfabeto
            if char not in req.alfabeto:
                valida = False
                break
            
            #buscar la transicion
            if estado_actual in req.transiciones and char in req.transiciones[estado_actual]:
                estado_actual = req.transiciones[estado_actual][char]
                camino.append(estado_actual)
            else:
                valida = False
                break #atasco
        
        #es aceptada si no se atascó y terminó en un estado de aceptación
        es_aceptada = valida and (estado_actual in req.estados_finales)
        notacion = " -> ".join(camino) if valida else f"{' -> '.join(camino)} -> [Error/Atasco]"
        
        resultados.append({
            "cadena": cadena,
            "aceptada": es_aceptada,
            "camino_transicion": notacion
        })

    return {
        "estados_totales": req.estados,
        "alfabeto": req.alfabeto,
        "estado_inicial": req.estado_inicial,
        "estados_finales": req.estados_finales,
        "resultados": resultados
    }

#AFN
@app.post("/afn")
def evaluar_afn(req: AutomataRequest):
    resultados = []
    
    for cadena in req.cadenas:
        #en un AFN, podemos estar a la vez
        estados_actuales = {req.estado_inicial}
        camino = [f"{{{', '.join(estados_actuales)}}}"]
        valida = True

        for char in cadena:
            if char not in req.alfabeto:
                valida = False
                break
            
            siguientes_estados = set()
            for estado in estados_actuales:
                if estado in req.transiciones and char in req.transiciones[estado]:
                    destinos = req.transiciones[estado][char]
                    if isinstance(destinos, list):
                        siguientes_estados.update(destinos)
                    else:
                        siguientes_estados.add(destinos)
            
            if not siguientes_estados:
                valida = False
                break #atasco masivo 
                
            estados_actuales = siguientes_estados
            camino.append(f"{{{', '.join(estados_actuales)}}}")
        
        #es aceptada si la interseccion entre los estados actuales y los finales no esta vacia
        es_aceptada = valida and bool(estados_actuales.intersection(set(req.estados_finales)))
        notacion = " -> ".join(camino) if valida else f"{' -> '.join(camino)} -> [Conjunto Vacío]"

        resultados.append({
            "cadena": cadena,
            "aceptada": es_aceptada,
            "camino_transicion": notacion
        })

    return {
        "estados_totales": req.estados,
        "alfabeto": req.alfabeto,
        "estado_inicial": req.estado_inicial,
        "estados_finales": req.estados_finales,
        "resultados": resultados
    }
