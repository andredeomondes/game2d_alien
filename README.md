# Game 2D — Alien Invasion

Projeto desenvolvido ao longo de um curso de Python aplicando progressivamente boas
praticas de engenharia de software: analise estatica, principios SOLID e testes
automatizados.

---

## Estrutura do projeto

```
game2d_alien/
├── src/
│   ├── alien_invasion.py           # versao original
│   ├── alien_invasion_refactored.py # versao com SRP/OCP completo
│   ├── alien.py
│   ├── fast_alien.py               # OCP: alien mais rapido por heranca
│   ├── ship.py
│   ├── bullet.py
│   ├── settings.py
│   ├── bullet_manager.py           # SRP: gerencia projeteis
│   ├── fleet_manager.py            # SRP: gerencia frota
│   ├── game_events.py              # SRP: trata eventos de teclado
│   ├── game_renderer.py            # SRP: renderizacao grafica
│   ├── game_stats.py               # estado do jogo (score, vidas)
│   ├── scoreboard.py               # placar visual na tela
│   └── desconto.py                 # exemplo didatico de Strategy Pattern
├── tests/
│   ├── doubles.py                  # StubSemDesconto
│   ├── test_desconto.py            # assert, fixture, parametrize
│   ├── test_doubles.py             # stub e mock
│   └── test_game_alien.py          # stub e mock aplicados ao jogo
├── docs/                           # documentacao por commit
├── pytest.ini
└── .gitignore
```

---

## Branches e commits realizados

### Branch: main

| Hash | Commit |
|------|--------|
| `81ddde4` | feat: Criacao do arquivo alien_invasion.py |
| `117d32e` | Merge branch 'feature/analise-estatica' |
| `340ac6b` | Merge branch 'feature/applying-solid' |
| `9ab8e1b` | Merge branch 'feature/tests_units' |

---

### Branch: feature/analise-estatica

Aplicacao de ferramentas de analise estatica para verificar qualidade, estilo e tipos
sem executar o codigo.

| Hash | Commit | O que foi feito |
|------|--------|-----------------|
| `88fb72e` | Aplica analise estatica com ruff e mypy --strict | ruff format corrigiu formatacao; type hints `-> None` adicionados em todos os metodos; mypy --strict passou sem erros |

**Ferramentas usadas:** `ruff check .` / `ruff check . --fix` / `ruff format .` / `mypy --strict .`

**Total de commits proprios:** 1

---

### Branch: feature/applying-solid

Refatoracao progressiva aplicando os principios SOLID — principalmente SRP (Single
Responsibility Principle) e OCP (Open/Closed Principle).

| Hash | Commit | O que foi feito |
|------|--------|-----------------|
| `6ca73de` | refatoracao do codigo: aplicando SRP | Classe `AlienInvasion` dividida em metodos privados com responsabilidade unica |
| `8e7a89b` | refactor: adiciona type hints e extrai _create_alien | Type hints em todos os metodos; `_create_alien` extraido de `create_fleet` |
| `be19e21` | refactor: finalizacao da refatoracao para o principio SRP | Cada responsabilidade virou modulo separado: `BulletManager`, `FleetManager`, `GameEventHandler`, `GameRenderer` |
| `0764a8e` | refactor: aplicando principio O (OCP) | `FastAlien` criado por heranca; `FleetManager` aceita `alien_class` injetada — extensao sem modificar codigo existente |
| `34bcd7b` | refactor: aplicando principio SOLID — Scoreboard e GameStats | `GameStats` centraliza estado; `Scoreboard` renderiza pontuacao; `Clock` limita FPS a 60; score atualizado por colisao |
| `07d7a9c` | feat: adiciona exemplo de Strategy Pattern com descontos | `IDesconto` ABC, `Pedido(desconto).total(valor)`, `DescontoFixo`, `DescontoPercentual` |
| `64b285f` | fix: corrige desconto.py para estrutura coerente com spec | Atributos e assinaturas corrigidos para refletir a spec do curso |

**Total de commits proprios:** 7

---

### Branch: feature/tests_units

Implementacao de testes automatizados com pytest cobrindo os tres padroes principais
(assert, fixture, parametrize) e test doubles (stub e mock).

| Hash | Commit | O que foi feito |
|------|--------|-----------------|
| `a372c1a` | test: codigos exemplo de teste para o projeto | `pytest.ini`, `test_desconto.py` com assert / fixture / parametrize, 5 testes passando |
| `d4e5283` | test: codigos exemplo de teste para o projeto | `doubles.py` com `StubSemDesconto`; `test_doubles.py` com stub e mock; `test_game_alien.py` com stub de Settings e mock de `reset_stats`; `pytest-mock`, `pytest-html`, `coverage` instalados; `.gitignore` criado |
| `baccb72` | docs: atualiza documentacao com Strategy Pattern e testes | Docs 07, 08 e 09 adicionados |

**Total de commits proprios:** 3

---

## Resumo geral

| Metrica | Valor |
|---------|-------|
| Total de commits | 15 |
| Branches criadas | 3 |
| Branches mergeadas na main | 3 |
| Arquivos Python criados | 14 |
| Testes escritos | 10 |
| Cobertura de testes | 97% |

---

## Conceitos aplicados

| Conceito | Branch | Arquivo(s) |
|----------|--------|------------|
| Analise estatica (ruff + mypy) | feature/analise-estatica | `alien_invasion.py` |
| SRP — metodos | feature/applying-solid | `alien_invasion.py` |
| SRP — modulos | feature/applying-solid | `bullet_manager.py`, `fleet_manager.py`, `game_events.py`, `game_renderer.py` |
| OCP — heranca | feature/applying-solid | `fast_alien.py` |
| OCP — injecao de dependencia | feature/applying-solid | `fleet_manager.py` |
| Strategy Pattern | feature/applying-solid | `desconto.py` |
| Testes: assert | feature/tests_units | `test_desconto.py` |
| Testes: fixture | feature/tests_units | `test_desconto.py` |
| Testes: parametrize | feature/tests_units | `test_desconto.py` |
| Test double: Stub | feature/tests_units | `doubles.py`, `test_doubles.py`, `test_game_alien.py` |
| Test double: Mock | feature/tests_units | `test_doubles.py`, `test_game_alien.py` |
| Coverage + HTML report | feature/tests_units | `pytest.ini`, `.gitignore` |

---

## Como executar os testes

```bash
# Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install pytest pytest-mock pytest-html coverage pygame

# Rodar os testes
pytest -v

# Gerar relatorio HTML
pytest --html=relatorio.html

# Verificar cobertura
coverage run -m pytest
coverage report
```

---

## Documentacao

Cada etapa do projeto tem um arquivo `.md` explicando o que foi feito e por que:

| Arquivo | Conteudo |
|---------|----------|
| [docs/01-criacao-inicial.md](docs/01-criacao-inicial.md) | Game loop, estrutura inicial |
| [docs/02-analise-estatica.md](docs/02-analise-estatica.md) | ruff, mypy, type hints |
| [docs/03-aplicando-srp.md](docs/03-aplicando-srp.md) | SRP em metodos |
| [docs/04-srp-em-modulos.md](docs/04-srp-em-modulos.md) | SRP em arquivos separados |
| [docs/05-aplicando-ocp.md](docs/05-aplicando-ocp.md) | OCP, FastAlien, injecao de dependencia |
| [docs/06-scoreboard-gamestats.md](docs/06-scoreboard-gamestats.md) | GameStats, Scoreboard, Clock |
| [docs/07-strategy-pattern-desconto.md](docs/07-strategy-pattern-desconto.md) | Strategy Pattern, IDesconto |
| [docs/08-testes-unitarios.md](docs/08-testes-unitarios.md) | assert, fixture, parametrize |
| [docs/09-test-doubles-stub-mock.md](docs/09-test-doubles-stub-mock.md) | Stub, Mock, coverage |
