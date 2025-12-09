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
    
    codigo = input("Código do insumo: ").strip()
    
    if _buscar_produto(codigo) != -1:
        print("Código já cadastrado. Tente novamente.")
        return
    
    nome = input("Nome do insumo: ").strip()
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço por unidade: "))
    fabricacao = input("Data de fabricação (DD/MM/AAAA): ").strip()
    validade = input("Data de validade (DD/MM/AAAA): ").strip()
    fornecedor = input("Nome do fornecedor: ").strip()
    
    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "fabricacao": fabricacao,
        "validade": validade,
        "fornecedor": fornecedor
    }
    
    estoque.append(novo_produto)
    salvar_insumos()
    print("Insumo cadastrado com sucesso!")


def registrar_entrada() -> None:
    """Aumenta a quantidade de um insumo existente."""
    print("\n--- Registrar Entrada de Insumo ---")
    
    codigo = input("Código do insumo: ").strip()
    indice = _buscar_produto(codigo)
    
    if indice == -1:
        print("Código não encontrado. Tente novamente.")
        return
    
    quantidade = int(input("Quantidade a adicionar: "))
    estoque[indice]["quantidade"] += quantidade
    salvar_insumos()
    print("Entrada registrada com sucesso!")


def registrar_saida() -> None:
    """Diminui a quantidade de um insumo existente."""
    print("\n--- Registrar Saída de Insumo ---")
    
    codigo = input("Código do insumo: ").strip()
    indice = _buscar_produto(codigo)
    
    if indice == -1:
        print("Código não encontrado. Tente novamente.")
        return
    
    quantidade = int(input("Quantidade a remover: "))
    if estoque[indice]["quantidade"] < quantidade:
        print("Quantidade insuficiente em estoque.")
        return
    
    estoque[indice]["quantidade"] -= quantidade
    salvar_insumos()
    print("Saída registrada com sucesso!")


def listar_insumos() -> None:
    """Lista todos os insumos cadastrados."""
    if not estoque:
        print("\nNenhum insumo cadastrado.")
        return
    
    print("\n--- Lista de Insumos ---")
    for i, produto in enumerate(estoque, 1):
        print(f"\n{i}. {produto['nome']} (Código: {produto['codigo']})")
        print(f"   Quantidade: {produto['quantidade']} unidades")
        print(f"   Preço unitário: R$ {produto['preco']:.2f}")
        print(f"   Fabricação: {produto['fabricacao']}")
        print(f"   Validade: {produto['validade']}")
        print(f"   Fornecedor: {produto['fornecedor']}")


def deletar_insumo() -> None:
    """Remove um insumo do estoque."""
    print("\n--- Deletar Insumo ---")
    
    codigo = input("Código do insumo a deletar: ").strip()
    indice = _buscar_produto(codigo)
    
    if indice == -1:
        print("Código não encontrado.")
        return
    
    confirmacao = input(f"Tem certeza que deseja deletar '{estoque[indice]['nome']}'? (s/n): ").lower()
    if confirmacao == 's':
        estoque.pop(indice)
        salvar_insumos()
        print("Insumo deletado com sucesso!")
    else:
        print("Operação cancelada.")


def custo_mensal() -> None:
    """Calcula o custo total mensal dos insumos em estoque."""
    if not estoque:
        print("\nNenhum insumo em estoque.")
        return
    
    total_custo = sum(p["quantidade"] * p["preco"] for p in estoque)
    print(f"\nCusto total mensal dos insumos em estoque: R$ {total_custo:.2f}")


def custo_semanal() -> None:
    """Calcula o custo total semanal dos insumos em estoque."""
    if not estoque:
        print("\nNenhum insumo em estoque.")
        return
    
    total_custo = sum((p["quantidade"] * p["preco"]) / 4 for p in estoque)
    print(f"\nCusto total semanal dos insumos em estoque: R$ {total_custo:.2f}")


def custo_anual() -> None:
    """Calcula o custo total anual dos insumos em estoque."""
    if not estoque:
        print("\nNenhum insumo em estoque.")
        return
    
    total_custo = sum(p["quantidade"] * p["preco"] * 12 for p in estoque)
    print(f"\nCusto total anual dos insumos em estoque: R$ {total_custo:.2f}")  