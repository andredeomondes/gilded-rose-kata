# Problema e Contexto

## O sistema

A Gilded Rose é uma estalagem que mantém um inventário de itens cuja `quality` (qualidade) e `sell_in` (dias restantes para venda) são atualizados diariamente por um único método, `update_quality`, em `legacy/gilded_rose.py`.

Regras de negócio vigentes (capturadas a partir da especificação oficial, `docs/GildedRoseRequirements_pt-BR.md`, e confirmadas por execução em `docs/evidencias/execucao_legado_antes.txt`):

- Itens comuns perdem 1 de qualidade por dia, 2 por dia após a data de venda (`sell_in < 0`).
- `Aged Brie` ganha qualidade com o tempo (1/dia, 2/dia após vencer).
- `Sulfuras, Hand of Ragnaros` é um item legendário: nunca muda `quality` (fixo em 80) nem `sell_in`.
- `Backstage passes` ganham qualidade conforme a data se aproxima (1/dia, 2/dia com `sell_in < 11`, 3/dia com `sell_in < 6`), caindo a 0 abruptamente após o show (`sell_in < 0`).
- `quality` nunca é negativa nem passa de 50 (exceto Sulfuras).
- Itens `Conjured` deveriam perder qualidade 2x mais rápido que itens comuns — regra ainda **não implementada** no legado (ver Diagnóstico Técnico).

## Dificuldades de manutenção do sistema atual

O código funciona, mas toda a lógica está concentrada em um único método com condicionais profundamente aninhados e identificação de tipo de item por comparação de string repetida. Isso dificulta:

- Adicionar uma nova categoria de item (como Conjured) sem revisar manualmente todo o método em busca de pontos de impacto.
- Escrever testes unitários direcionados a uma única regra (a única forma de testar é rodar a simulação completa).
- Garantir, ao alterar uma regra, que regras de outros itens não foram afetadas por engano.

## Restrições obrigatórias do trabalho

- Não alterar a classe `Item`.
- Não alterar a propriedade `items` da classe `GildedRose`.
- Preservar comportamento existente para os itens já definidos.
- Implementar corretamente a regra dos itens Conjurados.
- Evitar refatoração arriscada sem rede de testes.
