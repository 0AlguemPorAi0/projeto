from src.main import *
from unittest.mock import patch


def test_root():
    result = root()
    yield result
    assert result == {"message": "Bem-vindo à Garagem de Carros!"}


def test_senha():
    with patch("random.randint", return_value=123456):
        result = senha()
        yield result
    assert result == {"senha": True, "num_aleatorio": 123456}


def test_criar_carro():
    carro_teste = Carro(marca="Toyota", modelo="Corolla XEi", ano=2021, disponivel=False)
    result = criar_carro(carro_teste)
    yield result
    assert carro_teste == result


def test_obter_carro_existente():
    carro_teste = Carro(marca="Honda", modelo="Civic", ano=2020, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = obter_carro(carro_id)
    yield result
    assert result == carro_teste


def test_obter_carro_inexistente():
    try:
        result = obter_carro(9999)
        yield result
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Carro não encontrado"


def test_listar_carros():
    result = listar_carros()
    yield result
    assert isinstance(result, dict)
    assert all(isinstance(v, Carro) for v in result.values())


def test_atualizar_carro_negativo():
    try:
        result = atualizar_carro(-1, Carro(marca="Ford", modelo="Ka", ano=2018, disponivel=True))
        yield result
    except HTTPException as e:
        assert e.status_code == 404


def test_atualizar_carro_positivo():
    carro_teste = Carro(marca="Chevrolet", modelo="Onix", ano=2022, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = atualizar_carro(carro_id, carro_teste)
    yield result
    assert result == carro_teste


def test_deletar_carro_negativo():
    try:
        result = deletar_carro(-1)
        yield result
    except HTTPException as e:
        assert e.status_code == 404


def test_deletar_carro_positivo():
    carro_teste = Carro(marca="Volkswagen", modelo="Golf", ano=2019, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = deletar_carro(carro_id)
    yield result
    assert result == {"message": f"Carro {carro_id} removido da garagem com sucesso"}
