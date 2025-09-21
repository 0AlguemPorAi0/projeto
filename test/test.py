from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Bem-vindo à Garagem de Carros!"}

def test_senha():
    with patch("random.randint", return_value=123456):
        result = senha()
    assert result == {"senha": True, "num_aleatorio": 123456}

def test_criar_carro():
    carro_teste = Carro(marca="Toyota", modelo="Corolla XEi", ano=2021, disponivel=False)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    assert db[carro_id] == carro_teste

def test_obter_carro_existente():
    carro_teste = Carro(marca="Honda", modelo="Civic", ano=2020, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    assert obter_carro(carro_id) == carro_teste

def test_obter_carro_inexistente():
    try:
        obter_carro(9999)
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Carro não encontrado"

def test_listar_carros():
    result = listar_carros()
    assert isinstance(result, dict)
    assert all(isinstance(v, Carro) for v in result.values())

def test_atualizar_carro_negativo():
    try:
        atualizar_carro(-1, Carro(marca="Ford", modelo="Ka", ano=2018, disponivel=True))
    except HTTPException as e:
        assert e.status_code == 404

def test_atualizar_carro_positivo():
    carro_teste = Carro(marca="Chevrolet", modelo="Onix", ano=2022, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    atualizado = atualizar_carro(carro_id, carro_teste)
    assert atualizado == carro_teste

def test_deletar_carro_negativo():
    try:
        deletar_carro(-1)
    except HTTPException as e:
        assert e.status_code == 404

def test_deletar_carro_positivo():
    carro_teste = Carro(marca="Volkswagen", modelo="Golf", ano=2019, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = deletar_carro(carro_id)
    assert result == {"message": f"Carro {carro_id} removido da garagem com sucesso"}
