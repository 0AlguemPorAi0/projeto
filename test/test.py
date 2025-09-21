from src.main import *
from unittest.mock import patch


def test_root():
    result = root()
    assert result == {"message": "Bem-vindo à Garagem de Carros!"}


def test_senha():
    with patch("random.randint", return_value=123456):
        result = senha()
    assert result == {"senha": True, "num_aleatorio": 123456}


def test_criar_carro():
    carro_teste = Carro(marca="Toyota", modelo="Corolla XEi", ano=2021, disponivel=False)
    result = criar_carro(carro_teste)
    assert carro_teste == result


def test_atualizar_carro_negativo():
    result = atualizar_carro(-1)
    assert not result


def test_atualizar_carro_positivo():
    result = atualizar_carro(1)
    assert result


def test_deletar_carro_negativo():
    result = deletar_carro(-1)
    assert not result


def test_deletar_carro_positivo():
    result = deletar_carro(1)
    assert result


def test_obter_carro():
    result = obter_carro(1)
    assert isinstance(result, Carro)


def test_listar_carros():
    result = listar_carros()
    assert isinstance(result, list)
    assert all(isinstance(c, Carro) for c in result)
