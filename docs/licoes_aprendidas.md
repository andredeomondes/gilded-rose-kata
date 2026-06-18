# Lições Aprendidas

Este documento apresenta uma reflexão sobre o processo de modernização do sistema Gilded Rose, incluindo as principais dificuldades enfrentadas pela equipe e as limitações reconhecidas na solução entregue.

## Dificuldades enfrentadas

**Compreender o comportamento real antes de confiar apenas na leitura do código.** O sistema legado contém regras corretas, mas de difícil identificação apenas pela leitura do código-fonte. Um exemplo é a ordem exata entre a atualização da qualidade e a redução do número de dias restantes, que influencia diretamente o resultado da regra dos itens Backstage Passes no dia exato do evento. Por esse motivo, foi necessário executar o sistema legado e observar diretamente sua saída, em vez de confiar apenas na interpretação do código, antes de migrar a lógica para a nova estrutura.

**Identificar falhas de configuração de ambiente que pareciam falhas de lógica.** O teste de aprovação que já acompanhava o projeto original falhava devido à ausência de configuração de uma ferramenta de comparação de diferenças, e não devido a um erro na regra de negócio. Essa situação reforçou a importância de investigar a causa real de uma falha de teste antes de tirar qualquer conclusão sobre o comportamento do sistema.

**Resistir à tentação de reescrever todo o sistema de uma só vez.** Desde a etapa de diagnóstico, já era possível antever o desenho final da solução, baseado em uma estratégia específica para cada tipo de item. Ainda assim, a equipe optou por realizar a refatoração em etapas pequenas e sequenciais, sempre com os testes em execução a cada passo, conforme definido no Plano de Contingência. Essa abordagem exigiu mais tempo, mas eliminou o risco de uma alteração extensa mascarar uma regressão no comportamento do sistema.

## Aprendizados obtidos

Os testes de caracterização não substituem a compreensão da regra de negócio: eles documentam apenas o que o sistema faz atualmente, mas a decisão sobre o que o sistema deveria fazer, como por exemplo a regra correta dos itens Conjurados, ainda depende da leitura cuidadosa da especificação do problema.

A identificação de tipo de item por comparação repetida de texto é um problema relativamente simples de diagnosticar e de corrigir: centralizar os nomes em constantes nomeadas e concentrar a escolha da estratégia em um único ponto do código elimina a maior parte da duplicação presente no sistema original, sem que seja necessário alterar a regra de negócio em si.

Separar claramente "o que muda", ou seja, a regra específica de cada tipo de item, de "quem orquestra", ou seja, a classe responsável apenas por identificar o tipo do item e delegar a atualização correspondente, facilita a inclusão de novas categorias de item no futuro, sem exigir alterações nas categorias já existentes, atendendo ao critério de extensibilidade definido no requisito não funcional RNF05.

## Limitações reconhecidas na solução entregue

A identificação dos itens Conjurados é realizada por meio do prefixo do seu nome. Essa abordagem é suficiente para o cenário proposto pelo trabalho, mas representa uma heurística baseada em texto: uma solução voltada à produção real provavelmente utilizaria um campo explícito de categoria no item, em vez de depender do nome. Essa limitação existe porque a classe `Item` não pode ser alterada, conforme restrição obrigatória do trabalho.

A cobertura de testes de 97% não inclui o script de demonstração do sistema (`src/texttest_fixture.py`), pois trata-se de um script de exibição de resultados, e não de uma regra de negócio. A decisão de não testá-lo unitariamente foi consciente e deliberada.
