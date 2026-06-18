# Plano de Execução — Gilded Rose Modernização

Mapeia as 10 etapas do `plan.md` em branches git e commits sequenciais, alinhados ao barema (item 9).

## Estrutura final do repositório

```
gilded-rose-modernizacao/
├── README.md
├── src/
│   └── (clean architecture: domain/, application/, infra ou cli/)
├── tests/
│   └── test_gilded_rose.py
├── docs/
│   ├── diagnostico_tecnico.md
│   ├── requisitos.md
│   ├── plano_contingencia.md
│   └── evidencias_testes.md
└── apresentacao/
    └── slides.pdf
```

## Convenção de branches

`main` protegida — só recebe merge depois que cada etapa estiver completa e testada.

| # | Branch | Etapa do plan.md | Entregável (barema) |
|---|--------|-------------------|----------------------|
| 1 | `docs/contexto-e-diagnostico` | Passo 1-3 | 5.1 Diagnóstico técnico (1,0 pt) |
| 2 | `docs/requisitos` | Passo 4 | 5.2 Documento de requisitos (1,0 pt) |
| 3 | `docs/plano-contingencia` | Passo 5 | 5.3 Plano de contingência (1,0 pt) |
| 4 | `legacy/codigo-original` | Passo 2 | base de comparação (sem nota direta, mas exigido p/ evidências) |
| 5 | `test/caracterizacao` | Passo 6 | base para 5.5 (testes) |
| 6 | `refactor/clean-architecture` | Passo 7 | 5.4 Código refatorado (1,0 pt) |
| 7 | `feat/conjured` | Passo 8 | Implementação Conjured (0,5 pt) |
| 8 | `test/cobertura-final` | Passo 9 | 5.5 Testes automatizados (1,0 pt) + 5.6 Evidências (0,5 pt) |
| 9 | `docs/readme-e-entrega` | Passo 10 | 5.7 README (1,0 pt) |
| 10 | `docs/apresentacao` | Passo 10 | 5.8 Apresentação (3,0 pt — feito fora do git) |

Cada branch nasce de `main` atualizada, e só faz merge (`git merge --no-ff`) depois de revisão do grupo.

## Sequência de commits por branch

### 1. `docs/contexto-e-diagnostico`
1. `docs: adiciona descricao do problema e contexto do sistema legado`
2. `docs: registra evidencias de execucao do sistema original (antes da refatoracao)`
3. `docs: diagnostico tecnico - code smells e riscos identificados`

→ merge em `main`: `Merge docs/contexto-e-diagnostico: diagnostico tecnico completo`

### 2. `docs/requisitos`
1. `docs: adiciona requisitos funcionais RF01-RF0n (itens comuns, Aged Brie, Sulfuras, Backstage, Conjured)`
2. `docs: adiciona requisitos nao funcionais RNF01-RNF0n`

→ merge: `Merge docs/requisitos: documento de requisitos rastreavel`

### 3. `docs/plano-contingencia`
1. `docs: define estrategia de refatoracao segura e ordem de mudancas`
2. `docs: lista riscos e acoes preventivas da refatoracao`

→ merge: `Merge docs/plano-contingencia: plano de riscos e validacao`

### 4. `legacy/codigo-original`
1. `chore: importa codigo legado original (Item, GildedRose, update_quality)`
2. `chore: adiciona script de execucao manual para gerar evidencias antes/depois`

→ merge: `Merge legacy/codigo-original: baseline do sistema legado`

### 5. `test/caracterizacao`
1. `test: adiciona testes de caracterizacao para itens comuns`
2. `test: adiciona testes de caracterizacao para Aged Brie e Sulfuras`
3. `test: adiciona testes de caracterizacao para Backstage Passes (casos de borda)`

→ merge: `Merge test/caracterizacao: rede de seguranca antes da refatoracao`

### 6. `refactor/clean-architecture`
(pequenos passos, testes rodando a cada commit)
1. `refactor: extrai logica de update_quality para camada domain (sem mudar comportamento)`
2. `refactor: cria estrategia por tipo de item (Strategy/polimorfismo) preservando regras`
3. `refactor: isola GildedRose como camada application, mantendo Item e Items intactos`
4. `refactor: remove duplicacao e condicionais aninhadas`

→ merge: `Merge refactor/clean-architecture: codigo refatorado com testes verdes`

### 7. `feat/conjured`
1. `feat: adiciona regra Conjured com degradacao dobrada respeitando limites`
2. `test: cobre Conjured com testes de qualidade minima/maxima e degradacao`

→ merge: `Merge feat/conjured: suporte a itens Conjured implementado e testado`

### 8. `test/cobertura-final`
1. `test: completa cobertura de casos de borda em todos os tipos de item`
2. `chore: gera relatorio de cobertura (pytest-cov)`
3. `docs: registra evidencias de execucao pos-refatoracao (prints/logs)`

→ merge: `Merge test/cobertura-final: evidencias e cobertura completas`

### 9. `docs/readme-e-entrega`
1. `docs: escreve README com instalacao, execucao e estrutura de pastas`
2. `docs: resume decisoes de refatoracao no README`
3. `chore: organiza estrutura final de pastas do repositorio`

→ merge: `Merge docs/readme-e-entrega: documentacao final pronta para entrega`

### 10. `docs/apresentacao`
1. `docs: adiciona slides da apresentacao final`

→ merge: `Merge docs/apresentacao: material de apresentacao incluido`

## Regras de ouro durante todo o processo

- Nunca alterar `Item` nem `GildedRose.items` — qualquer commit que toque nisso é revertido.
- Rodar testes antes de cada commit em `refactor/*` e `feat/*`.
- Commits pequenos e atômicos — 1 intenção por commit, mensagens no padrão `tipo: descrição` (conventional commits leve).
- `main` só recebe merge de branch com testes verdes.

## Próximo passo sugerido

Inicializar o repositório git e criar a branch 1 (`docs/contexto-e-diagnostico`) para começar o diagnóstico técnico.
