# Documento de Requisitos

Requisitos extraídos de `docs/GildedRoseRequirements_pt-BR.md` e confirmados por execução em `docs/evidencias/execucao_legado_antes.txt`.

## Requisitos Funcionais

| ID | Descrição |
|----|-----------|
| RF01 | O sistema deve diminuir `sell_in` de todo item em 1 a cada dia, exceto itens `Sulfuras`. |
| RF02 | Itens comuns devem perder 1 de `quality` por dia enquanto `sell_in >= 0`. |
| RF03 | Itens comuns devem perder 2 de `quality` por dia depois que `sell_in < 0`. |
| RF04 | `Aged Brie` deve ganhar 1 de `quality` por dia enquanto `sell_in >= 0`. |
| RF05 | `Aged Brie` deve ganhar 2 de `quality` por dia depois que `sell_in < 0`. |
| RF06 | `Sulfuras, Hand of Ragnaros` nunca deve ter `sell_in` ou `quality` alterados. |
| RF07 | `Backstage passes` devem ganhar 1 de `quality` por dia quando `sell_in > 10`. |
| RF08 | `Backstage passes` devem ganhar 2 de `quality` por dia quando `sell_in <= 10` e `sell_in > 5`. |
| RF09 | `Backstage passes` devem ganhar 3 de `quality` por dia quando `sell_in <= 5` e `sell_in >= 0`. |
| RF10 | `Backstage passes` devem ter `quality` zerada imediatamente após o show (`sell_in < 0`). |
| RF11 | Itens `Conjured` devem perder `quality` 2x mais rápido que itens comuns: 2/dia enquanto `sell_in >= 0`, 4/dia depois que `sell_in < 0`. |
| RF12 | `quality` nunca deve ser negativa, para nenhum tipo de item. |
| RF13 | `quality` nunca deve exceder 50, exceto para `Sulfuras` (fixo em 80). |

## Requisitos Não Funcionais

| ID | Descrição |
|----|-----------|
| RNF01 | A classe `Item` não pode ser alterada (restrição obrigatória do trabalho). |
| RNF02 | A propriedade `items` da classe `GildedRose` não pode ser alterada (restrição obrigatória). |
| RNF03 | O comportamento existente para itens já definidos (comum, Aged Brie, Sulfuras, Backstage) deve ser preservado integralmente após a refatoração — validado por testes de caracterização (`docs/evidencias/execucao_legado_antes.txt` vs. evidência pós-refatoração). |
| RNF04 | O código deve permitir testar a regra de cada tipo de item de forma isolada (testabilidade), sem exigir execução da simulação completa. |
| RNF05 | O código deve permitir adicionar uma nova categoria de item sem modificar a lógica de categorias existentes (manutenibilidade/extensibilidade), seguindo princípio aberto/fechado. |
| RNF06 | O código deve eliminar identificação de tipo de item por comparação de string duplicada (legibilidade, ver `docs/diagnostico_tecnico.md` item 2). |
| RNF07 | A solução deve seguir um padrão arquitetural reconhecido (Clean Architecture), com separação entre regra de domínio e orquestração (`GildedRose`). |
