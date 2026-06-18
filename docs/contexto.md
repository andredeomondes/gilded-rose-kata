# Problema e Contexto

## O sistema

A Gilded Rose é uma estalagem fictícia que mantém um inventário de itens. Cada item possui dois atributos principais: a qualidade (`quality`), que representa o seu valor, e o número de dias restantes até a data de venda (`sell_in`). Esses dois atributos são atualizados automaticamente todos os dias por um único método do sistema, chamado `update_quality`, localizado no arquivo `legacy/gilded_rose.py`.

As regras de negócio vigentes foram extraídas da especificação oficial do problema (documento `docs/GildedRoseRequirements_pt-BR.md`) e confirmadas por meio da execução real do sistema, cuja saída está registrada em `docs/evidencias/execucao_legado_antes.txt`:

- Itens comuns perdem 1 ponto de qualidade por dia. Após a data de venda, essa perda passa a ser de 2 pontos por dia.
- O item "Aged Brie" ganha qualidade com o passar do tempo: 1 ponto por dia antes do vencimento e 2 pontos por dia após o vencimento.
- O item "Sulfuras, Hand of Ragnaros" é um item legendário e, por isso, nunca tem sua qualidade ou seu prazo de validade alterados.
- Os itens "Backstage passes" ganham qualidade conforme a data do evento se aproxima: 1 ponto por dia quando faltam mais de 10 dias, 2 pontos por dia quando faltam entre 6 e 10 dias, e 3 pontos por dia quando faltam 5 dias ou menos. Após a data do evento, a qualidade desses itens cai imediatamente a zero.
- A qualidade de qualquer item nunca pode ser negativa, nem pode superar o valor máximo de 50, com exceção do item Sulfuras, cuja qualidade é fixa em 80.
- Os itens da categoria "Conjurados" (Conjured) deveriam perder qualidade duas vezes mais rápido que os itens comuns. Essa regra, no entanto, ainda não está implementada corretamente no sistema legado, conforme detalhado no Diagnóstico Técnico (`docs/diagnostico_tecnico.md`).

## Dificuldades de manutenção do sistema atual

Embora o sistema funcione corretamente para os itens já existentes, toda a sua lógica de negócio está concentrada em um único método, organizado por meio de condicionais aninhados e identificação de tipo de item por comparação direta de texto. Essa estrutura traz três dificuldades principais:

1. Adicionar uma nova categoria de item, como o Conjurado, exige revisar manualmente todo o método em busca de pontos que possam ser afetados pela mudança.
2. Não é possível escrever um teste automatizado que valide isoladamente a regra de um único tipo de item — a única forma de testar qualquer regra é executar a simulação completa do sistema.
3. Ao alterar uma regra específica, não há garantia de que regras de outros itens, sem relação alguma com a mudança, não tenham sido afetadas por engano.

## Restrições obrigatórias do trabalho

A modernização do sistema deve respeitar as seguintes restrições, definidas pelo enunciado da atividade:

- A classe `Item` não pode ser alterada.
- A propriedade `items` da classe `GildedRose` não pode ser alterada.
- O comportamento já existente para os itens previstos na especificação original deve ser integralmente preservado.
- A regra dos itens Conjurados deve ser implementada corretamente.
- Toda refatoração deve ser acompanhada de testes automatizados que comprovem a preservação do comportamento.
