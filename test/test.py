import pytest
from src.main import *
from unittest.mock import patch

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Bem-vindo à Garagem de Carros!"}

@pytest.mark.asyncio
async def test_senha():
    with patch("random.randint", return_value=123456):
        result = await senha()
    assert result == {"senha": True, "num_aleatorio": 123456}

@pytest.mark.asyncio
async def test_criar_carro():
    carro_teste = Carro(marca="Toyota", modelo="Corolla XEi", ano=2021, disponivel=False)
    result = await criar_carro(carro_teste)
    assert carro_teste == result

@pytest.mark.asyncio
async def test_obter_carro_existente():
    carro_teste = Carro(marca="Honda", modelo="Civic", ano=2020, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = await obter_carro(carro_id)
    assert result == carro_teste

@pytest.mark.asyncio
async def test_listar_carros():
    result = await listar_carros()
    assert isinstance(result, dict)
    assert all(isinstance(v, Carro) for v in result.values())

@pytest.mark.asyncio
async def test_atualizar_carro_positivo():
    carro_teste = Carro(marca="Chevrolet", modelo="Onix", ano=2022, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = await atualizar_carro(carro_id, carro_teste)
    assert result == carro_teste

@pytest.mark.asyncio
async def test_deletar_carro_positivo():
    carro_teste = Carro(marca="Volkswagen", modelo="Golf", ano=2019, disponivel=True)
    carro_id = len(db) + 1
    db[carro_id] = carro_teste
    result = await deletar_carro(carro_id)
    assert result == {"message": f"Carro {carro_id} removido da garagem com sucesso"}
