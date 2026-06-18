# Documento de Requisitos

Este documento organiza, em formato rastreável, as regras de negócio descritas na especificação oficial do problema (`docs/GildedRoseRequirements_pt-BR.md`) e confirmadas por execução real do sistema legado (`docs/evidencias/execucao_legado_antes.txt`).

## Requisitos Funcionais

Os requisitos funcionais descrevem o comportamento esperado do sistema para cada tipo de item.

| Código | Descrição |
|--------|-----------|
| RF01 | O sistema deve diminuir em 1 unidade o número de dias restantes (`sell_in`) de todo item a cada dia, com exceção dos itens da categoria Sulfuras. |
| RF02 | Itens comuns devem perder 1 ponto de qualidade por dia enquanto a data de venda não tiver passado. |
| RF03 | Itens comuns devem perder 2 pontos de qualidade por dia após a data de venda ter passado. |
| RF04 | O item "Aged Brie" deve ganhar 1 ponto de qualidade por dia enquanto a data de venda não tiver passado. |
| RF05 | O item "Aged Brie" deve ganhar 2 pontos de qualidade por dia após a data de venda ter passado. |
| RF06 | O item "Sulfuras, Hand of Ragnaros" nunca deve ter sua qualidade ou seu número de dias restantes alterados. |
| RF07 | Os itens "Backstage passes" devem ganhar 1 ponto de qualidade por dia quando restarem mais de 10 dias para o evento. |
| RF08 | Os itens "Backstage passes" devem ganhar 2 pontos de qualidade por dia quando restarem entre 6 e 10 dias para o evento. |
| RF09 | Os itens "Backstage passes" devem ganhar 3 pontos de qualidade por dia quando restarem 5 dias ou menos para o evento. |
| RF10 | A qualidade dos itens "Backstage passes" deve ser reduzida a zero imediatamente após a data do evento. |
| RF11 | Os itens da categoria Conjurados devem perder qualidade duas vezes mais rápido que os itens comuns: 2 pontos por dia antes do vencimento e 4 pontos por dia após o vencimento. |
| RF12 | A qualidade de um item nunca pode ser inferior a zero, independentemente do seu tipo. |
| RF13 | A qualidade de um item nunca pode ser superior a 50, exceto para o item Sulfuras, cuja qualidade é fixa em 80. |

## Requisitos Não Funcionais

Os requisitos não funcionais descrevem atributos de qualidade exigidos da solução, e não regras de comportamento específicas de um item.

| Código | Descrição |
|--------|-----------|
| RNF01 | A classe `Item` não pode ser alterada, conforme restrição obrigatória estabelecida pelo enunciado do trabalho. |
| RNF02 | A propriedade `items` da classe `GildedRose` não pode ser alterada, conforme restrição obrigatória estabelecida pelo enunciado do trabalho. |
| RNF03 | O comportamento já existente para os itens comuns, Aged Brie, Sulfuras e Backstage Passes deve ser integralmente preservado após a refatoração, validado por meio de testes de caracterização e da comparação entre as evidências de execução anteriores e posteriores à refatoração. |
| RNF04 | O código deve permitir que a regra de cada tipo de item seja testada de forma isolada, sem exigir a execução completa da simulação do sistema. |
| RNF05 | O código deve permitir a inclusão de uma nova categoria de item sem exigir modificações na lógica das categorias já existentes. |
| RNF06 | O código não deve identificar o tipo de um item por meio de comparações repetidas de texto espalhadas pela lógica de negócio. |
| RNF07 | A solução deve seguir um padrão arquitetural reconhecido, com separação clara entre a regra de domínio e a orquestração do sistema (Clean Architecture). |
