# Gilded Rose — Modernização

Modernização do sistema legado Gilded Rose: diagnóstico técnico, refatoração segura para Clean Architecture e implementação da regra de itens Conjurados, com testes automatizados e evidências de validação.

## Estrutura do projeto

```
.
├── README.md
├── pytest.ini
├── .coveragerc
├── legacy/                  # código original do kata, intocado (baseline de comparação)
│   ├── gilded_rose.py
│   ├── texttest_fixture.py
│   └── tests/
├── src/                      # código refatorado (Clean Architecture)
│   ├── domain/
│   │   ├── item.py           # classe Item — não alterada (restrição obrigatória)
│   │   ├── item_names.py     # nomes de item centralizados
│   │   └── item_updaters.py  # uma estratégia (Strategy) por tipo de item
│   ├── application/
│   │   └── gilded_rose.py    # orquestração — delega para a estratégia correta
│   └── texttest_fixture.py   # mesma simulação do legado, sobre o código novo
├── tests/                    # testes contra o código refatorado
│   ├── test_caracterizacao.py
│   └── test_item_updaters.py
└── docs/
    ├── GildedRoseRequirements_pt-BR.md
    ├── contexto.md
    ├── diagnostico_tecnico.md
    ├── requisitos.md
    ├── plano_contingencia.md
    └── evidencias/
        ├── execucao_legado_antes.txt
        ├── testes_legado_antes.txt
        ├── execucao_refatorado_depois.txt
        ├── diff_antes_depois.txt
        └── cobertura_final.txt
```

## Instalação

```bash
python3 -m venv .venv
.venv/bin/pip install -r legacy/requirements.txt pytest-cov
```

## Executar o sistema

Simulação de N dias sobre o código refatorado:

```bash
.venv/bin/python -m src.texttest_fixture 30
```

Simulação sobre o código legado original (comparação):

```bash
cd legacy && ../.venv/bin/python texttest_fixture.py 30
```

## Rodar os testes

```bash
.venv/bin/python -m pytest tests/ -v
```

Com relatório de cobertura:

```bash
.venv/bin/python -m pytest tests/ --cov=src --cov-report=term-missing
```

## Resumo da solução

O sistema legado concentrava toda a regra de negócio em um único método (`legacy/gilded_rose.py:update_quality`), com condicionais aninhados em até 4 níveis e identificação de tipo de item por comparação de string repetida em vários pontos. Isso tornava o código difícil de testar isoladamente e arriscado de estender (detalhes em `docs/diagnostico_tecnico.md`).

A refatoração (`docs/plano_contingencia.md`) seguiu 3 passos, sempre com testes de caracterização passando:

1. Mover `Item` e `GildedRose` para `src/`, sem alterar lógica — prova que a estrutura nova não quebra nada.
2. Substituir os condicionais por uma estratégia (Strategy/polimorfismo) isolada por tipo de item, em `src/domain/item_updaters.py`.
3. Adicionar a estratégia de itens Conjurados (`ConjuredItemUpdater`), corrigindo um bug confirmado no legado: o item já existia no cenário de demonstração, mas degradava como item comum em vez de 2x mais rápido.

`Item` e a propriedade `items` de `GildedRose` nunca foram alterados, conforme restrição obrigatória do trabalho.

## Validação

- 24 testes automatizados (pytest), cobrindo itens comuns, Aged Brie, Sulfuras, Backstage Passes e Conjured, incluindo casos de borda (limites de quality 0 e 50).
- 97% de cobertura de código na camada `domain`/`application` (`docs/evidencias/cobertura_final.txt`).
- Evidência de execução antes e depois da refatoração, com diff linha a linha: a única diferença é o comportamento do item Conjured, que passou a degradar corretamente (`docs/evidencias/diff_antes_depois.txt`).
