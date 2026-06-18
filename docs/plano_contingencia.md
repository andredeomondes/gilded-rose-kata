# Plano de Contingência e Refatoração

## Estratégia geral

A refatoração do sistema foi planejada de forma incremental, sempre apoiada por uma rede de testes de caracterização. Nenhuma alteração estrutural no código foi realizada antes da existência de testes automatizados que comprovassem o comportamento atual do sistema, conforme descrito no documento de requisitos (`docs/requisitos.md`).

## O que foi alterado

- O método `update_quality` foi decomposto em estratégias independentes, uma para cada tipo de item, organizadas na camada de domínio da arquitetura limpa adotada.
- A classe `GildedRose` passou a delegar a atualização de cada item à estratégia correspondente, em vez de concentrar toda a lógica em condicionais internos.
- Foi adicionada a estratégia para os itens da categoria Conjurados, ausente no sistema legado, conforme apontado no item 7 do Diagnóstico Técnico (`docs/diagnostico_tecnico.md`).
- Foi criada uma suíte de testes automatizados que cobre individualmente cada tipo de item, além da correção da configuração do mecanismo de teste de aprovação que, no sistema legado, falhava por ausência de configuração, e não por erro de lógica.

## O que não foi alterado

Por se tratar de uma restrição obrigatória do trabalho, os seguintes elementos permaneceram exatamente como estavam no sistema legado:

- A classe `Item`, definida originalmente em `legacy/gilded_rose.py` (linhas 39 a 46): sua assinatura, seus atributos e seu método `__repr__` permanecem idênticos.
- A propriedade `items` da classe `GildedRose`: continua sendo uma lista simples de objetos `Item`, atribuída diretamente no método construtor, sem qualquer encapsulamento adicional.
- O comportamento observável do sistema para os itens comuns, Aged Brie, Sulfuras e Backstage Passes, validado por comparação direta com a execução do sistema legado (`docs/evidencias/execucao_legado_antes.txt`).

## Riscos identificados e ações preventivas

| Risco | Ação preventiva adotada |
|-------|--------------------------|
| Quebrar uma regra de negócio já existente ao mover a lógica para estratégias separadas | Os testes de caracterização foram escritos e validados antes de qualquer alteração estrutural no código; a saída da simulação de 30 dias foi comparada, linha a linha, entre a versão anterior e a versão posterior à refatoração. |
| Alterar a classe `Item` ou a propriedade `items` por descuido, o que acarretaria penalidade de 2,0 pontos conforme o critério de avaliação | Cada etapa da refatoração foi revisada individualmente para confirmar que a classe `Item` permaneceu intocada; os testes automatizados também verificam que a referência à lista de itens não foi substituída. |
| Implementar a regra dos itens Conjurados de forma incorreta, o que acarretaria penalidade de 2,0 pontos | Foram criados testes dedicados exclusivamente à regra dos itens Conjurados, cobrindo a degradação de 2 pontos por dia antes do vencimento, 4 pontos por dia após o vencimento, e o respeito ao limite mínimo de qualidade igual a zero. |
| Perder a cobertura de algum caso de borda já existente, como a qualidade exatamente em zero ou em cinquenta, ou o comportamento dos itens Backstage Passes no dia exato do evento | Os testes de caracterização, escritos antes da refatoração, já cobrem esses casos; os mesmos casos foram preservados na suíte de testes final. |
| Realizar uma refatoração de grande porte de uma só vez, dificultando a revisão do código e a reversão de eventuais erros | A refatoração foi dividida em comissões pequenas e sequenciais (extrair a lógica para a nova estrutura, introduzir as estratégias por tipo de item e, por fim, remover os condicionais antigos), sempre com os testes em execução a cada etapa. |

## Ordem de execução adotada

1. Criação de testes de caracterização cobrindo todos os tipos de item já existentes, executados contra o código legado, sem qualquer alteração.
2. Extração da lógica do método `update_quality` para a camada de domínio da nova arquitetura, mantendo os testes em execução a cada etapa.
3. Implementação da estratégia para os itens Conjurados, acompanhada de testes específicos.
4. Execução da suíte completa de testes, geração de evidências posteriores à refatoração e comparação com as evidências anteriores.

## Critérios de validação adotados

- Toda a suíte de testes, incluindo os testes de caracterização e os novos testes unitários, deve ser executada com sucesso antes de qualquer integração à branch principal do repositório.
- A saída da simulação de 30 dias deve ser idêntica, item por item, entre a versão legada e a versão final, com exceção do item Conjurado, cujo comportamento foi corrigido intencionalmente.
- A comparação entre a classe `Item` do sistema legado e a classe `Item` da versão final deve resultar em nenhuma diferença.
