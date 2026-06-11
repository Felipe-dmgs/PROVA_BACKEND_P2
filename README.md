# 🚀 Projeto E-Commerce - API de Produtos (FastAPI & SQLAlchemy)

Projeto desenvolvido com FastAPI para o gerenciamento de produtos, utilizando PostgreSQL como banco de dados e Docker para conteinerização dos ambientes de desenvolvimento e teste.

---

## 1. Instruções para subir o banco de teste com Docker

O projeto utiliza o Docker Compose para gerenciar os serviços de banco de dados de forma isolada. Para subir o ambiente de testes, certifique-se de que o Docker Desktop esteja rodando em sua máquina e siga os passos abaixo:

1. No terminal, navegue até a raiz do projeto (`C:\Documents\PROVA_BACKEND_P2`).
2. Execute o comando para baixar as imagens e iniciar os contêineres em segundo plano:
   ```bash
   docker compose up -d
   docker compose down
   docker compose up -d

## 2. Comando para executar os testes
1. pytest --cov=main -v 
2. pytest --cov=main --cov-report=term-missing - para uma resposta mais detalhada

## 3. É esperado está sáida do pytes

============================================================= test session starts =============================================================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0 -- C:\ProjetoArduino\PROVA_BACKEND_P2\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\ProjetoArduino\PROVA_BACKEND_P2
configfile: pytest.ini
testpaths: .
plugins: anyio-4.13.0, cov-7.1.0
collected 15 items                                                                                                                             

tests/test_produtos.py::test_listar_produtos_banco_vazio PASSED                                                                          [  6%]
tests/test_produtos.py::test_criar_produto_e_persistencia PASSED                                                                         [ 13%]
tests/test_produtos.py::test_criar_produto_e_verificar_na_listagem PASSED                                                                [ 20%]
tests/test_produtos.py::test_buscar_produto_id PASSED                                                                                    [ 26%]
tests/test_produtos.py::test_buscar_produto_id_inexistente PASSED                                                                        [ 33%]
tests/test_produtos.py::test_deletar_produto PASSED                                                                                      [ 40%]
tests/test_produtos.py::test_deletar_produto_e_confirmar_com_get PASSED                                                                  [ 46%]
tests/test_produtos.py::test_deletar_produto_inexistente PASSED                                                                          [ 53%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido0] PASSED                                                    [ 60%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido1] PASSED                                                    [ 66%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido2] PASSED                                                    [ 73%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido3] PASSED                                                    [ 80%]
tests/test_produtos.py::test_criar_produto_payload_invalido[payload_invalido4] PASSED                                                    [ 86%]
tests/test_produtos.py::test_validar_banco_isolado_parte_1 PASSED                                                                        [ 93%]
tests/test_produtos.py::test_validar_banco_isolado_parte_2 PASSED                                                                        [100%]

=============================================================== tests coverage ================================================================
_______________________________________________ coverage: platform win32, python 3.14.5-final-0 _______________________________________________

Name      Stmts   Miss  Cover
-----------------------------
main.py      55      4    93%
-----------------------------
TOTAL        55      4    93%
============================================================= 15 passed in 0.20s ==============================================================
## 4. Isolamento entre Testes
- O isolamento do banco de dados ocorre devido a duas estratégias diferentes:
1. Isolamento de bancos, O banco de dados de desenvolvimento é separado do banco de testes, enquanto o de desenvolvimento roda na porta padrão 5432, o de testes roda em outro contêiner na porta 5433. Garantindo que um nunca se misture com o outro.
2. No arquivo conftest, usei fixtures do Pyytest configuradas com o escopo de função, onde antes de cada teste começar todas as tabelas antigas são apagadas e novas são criadas, Durante o teste sobescrevemos a dependência do banco de desenvolvimento pelo banco de testes, E após o fim do teste a sessão é fechada e o banco é resetado.