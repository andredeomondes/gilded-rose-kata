# Melhoria Realizada

Este documento descreve as alterações realizadas no sistema Gilded Rose e a justificativa técnica de cada uma, em complemento ao Diagnóstico Técnico (`docs/diagnostico_tecnico.md`) e ao Plano de Contingência (`docs/plano_contingencia.md`).

## 1. Extração da classe `Item` e da classe `GildedRose` para a nova estrutura de pastas

O código foi movido do arquivo `legacy/gilded_rose.py` para os arquivos `src/domain/item.py`, contendo a classe `Item` sem qualquer alteração, e `src/application/gilded_rose.py`, contendo a classe `GildedRose` com a lógica ainda idêntica à original nesta primeira etapa.

Essa primeira movimentação teve como objetivo estabelecer a estrutura de pastas da arquitetura limpa antes de qualquer alteração de comportamento, permitindo confirmar, por meio dos testes de caracterização, que a simples mudança de localização do código não alterou o seu funcionamento.

## 2. Substituição dos condicionais aninhados por estratégias específicas

Cada tipo de item — comum, Aged Brie, Sulfuras e Backstage Passes — passou a ter sua própria classe de atualização, com um único método responsável por aplicar a regra correspondente. A classe `GildedRose` foi simplificada para apenas identificar o tipo de cada item e delegar a atualização à classe responsável.

Essa mudança resolve diretamente os problemas identificados no Diagnóstico Técnico relacionados a condicionais aninhados, duplicação de comparação de texto, mistura de responsabilidades e acoplamento indevido entre regras distintas. Cada regra de negócio passou a poder ser lida, compreendida e testada de forma isolada, sem necessidade de instanciar o sistema completo.

## 3. Centralização dos limites de qualidade

Os valores mínimo (zero) e máximo (cinquenta), antes repetidos como números fixos em diversos pontos do código legado, foram centralizados em constantes nomeadas e aplicados de forma consistente em toda a lógica de domínio.

Essa centralização resolve o problema de duplicação da regra de limite identificado no Diagnóstico Técnico: qualquer alteração futura desses valores passa a exigir uma única modificação no código.

## 4. Centralização dos nomes de item

Os textos "Aged Brie", "Sulfuras, Hand of Ragnaros" e "Backstage passes to a TAFKAL80ETC concert", antes repetidos como literais em diversos pontos do código, passaram a ser constantes nomeadas, reutilizadas tanto pela lógica de domínio quanto pelos testes automatizados.

Essa centralização elimina o risco de divergência entre o nome utilizado na lógica do sistema e o nome utilizado nos testes, além de tornar explícita a intenção de cada constante.

## 5. Implementação da regra dos itens Conjurados

Foi criada uma nova estratégia responsável por aplicar a degradação de 2 pontos de qualidade por dia antes do vencimento e 4 pontos por dia após o vencimento, sempre respeitando o limite mínimo de qualidade igual a zero. A identificação desse tipo de item é feita por meio do prefixo do nome, e não por correspondência exata, de modo a cobrir toda a categoria de itens Conjurados, e não apenas o item "Conjured Mana Cake" citado na especificação.

Essa implementação corrige o problema confirmado no sistema legado, em que o item Conjurado já estava presente no cenário de demonstração, mas era tratado incorretamente como um item comum.

## 6. Criação de testes em duas camadas

Foram criados testes de ponta a ponta, que avaliam o comportamento completo do sistema por meio da classe `GildedRose`, e testes unitários, que avaliam cada estratégia de atualização de forma isolada, sem depender da instância completa do sistema.

Essa divisão demonstra, na prática, a melhoria de testabilidade exigida pelo requisito não funcional RNF04 (`docs/requisitos.md`) — algo que não era possível realizar no sistema legado.

## Evidência de que o comportamento foi preservado

O arquivo `docs/evidencias/diff_antes_depois.txt` apresenta a comparação completa entre a execução do sistema legado e a execução do sistema refatorado ao longo de 30 dias de simulação. A única diferença encontrada está relacionada ao item Conjurado, que teve seu comportamento corrigido intencionalmente. Todos os demais itens — comum, Aged Brie, Sulfuras e Backstage Passes — produziram exatamente a mesma saída em ambas as versões.
