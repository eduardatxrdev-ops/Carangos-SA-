import os 
os.system("cls" if os.name == "nt" else "clear")
import json
from typing import List, Dict, Any

FILE_NAME = "insumos.json"
FILE_PATH = os.path.join(os.path.dirname(__file__), FILE_NAME)


def carregar_insumos() -> List[Dict[str, Any]]:
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except Exception:
        return []

estoque = {}

def cadastrar_insumo():
    print("\n--- Cadastrar Insumo ---")
    
    codigo = input("Código do insumo: ")
    
    if codigo in estoque:
        print("Código já cadastrado. Tente novamente.")
        return
    
    nome = input("Nome do insumo: ")
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço por unidade: "))
    fabricação = input("Data de fabricação (DD/MM/AAAA): ")
    validade = input("Data de validade (DD/MM/AAAA): ")
    fornecedor = input("Nome do fornecedor: ")
    
    estoque[codigo] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "fabricação": fabricação,
        "validade": validade,
        "fornecedor": fornecedor
    }
    
    print("Insumo cadastrado com sucesso!")
    
def registrar_entrada ():
    print ("\n --- Registrar Entrada de Insumo ---")
    
    codigo = input("Código do insumo: ")
    
    if codigo not in estoque:
            print("Código não encontrado. Tente novamente.")
        
            return
    else:
        quantidade = int(input("Quantidade a adicionar: "))
        estoque[codigo]["quantidade"] += quantidade
        print("Entrada registrada com sucesso!")