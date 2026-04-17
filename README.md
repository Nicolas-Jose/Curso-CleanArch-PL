# CleanArch (Estudo de Clean Architecture em Python)

Projeto de estudo com foco em separação de camadas (`main`, `presentation`, `data`, `domain`, `infra`) e fluxo HTTP com Flask.

## Objetivo

Demonstrar, na prática, conceitos de Clean Architecture:
- separação de responsabilidades
- inversão de dependência
- uso de interfaces/contratos
- isolamento de detalhes de framework e banco

## Tecnologias

- Python
- Flask
- SQLAlchemy
- MySQL (PyMySQL)
- Cerberus
- Pytest

## Estrutura

- `src/main`: rotas, adapters, composers, bootstrap
- `src/presentation`: controllers e tipos HTTP
- `src/data`: implementação dos casos de uso e interfaces
- `src/domain`: contratos de casos de uso e modelos de domínio
- `src/infra`: acesso a banco, entidades e conexão

## Fluxos implementados

- `POST /user` → registro de usuário
- `GET /user/find?first_name=...` → busca de usuário

## Como executar

```bash
pip install -r requirements.txt
python run.py