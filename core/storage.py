import json
import os

DATA_PATH = "data/gastos.json"

def loadData():
    if not os.path.exists(DATA_PATH):
        return {"gastos": [], "categorias": []}

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def saveData(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def nextId(data):
    if not data["gastos"]:
        return "00001"

    ultimo = int(data["gastos"][-1]["id"])
    nuevo = ultimo + 1
    return str(nuevo).zfill(5)
