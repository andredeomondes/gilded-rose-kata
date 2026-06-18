Trabalho Prático
Modernização de Sistema Legado

Projeto Gilded Rose - Refatoração, Qualidade de Software e Documentação Inspirada no MPS.BR

Disciplina: Qualidade de Software e Testes

Professor: Leonardo Cardia

Entrega: pacote de modernização contendo documentação, código refatorado, testes e evidências

Resumo da atividade

Nesta atividade, a equipe deverá atuar como uma consultoria técnica contratada para modernizar um sistema legado. O desafio é compreender o comportamento atual, documentar os requisitos, planejar a refatoração, implementar a nova regra de negócio, criar testes automatizados e apresentar evidências de qualidade.

Repositório/base do problema: GildedRoseRequirements_pt-BR.mdLinks to an external site.

1. Contexto do Desafio

A empresa Gilded Rose possui um sistema legado responsável por atualizar diariamente a qualidade dos itens de seu estoque. O sistema funciona, mas foi desenvolvido de forma pouco estruturada, dificultando manutenção, entendimento, testes e evolução.

Sua equipe foi contratada para realizar uma modernização incremental da solução, preservando o comportamento existente e adicionando suporte à nova categoria de itens Conjurados (Conjured).

Importante

O objetivo principal não é apenas fazer o código funcionar. O objetivo é demonstrar capacidade de análise, planejamento, documentação, refatoração segura e validação por testes.

2. Objetivos de Aprendizagem

   Compreender e interpretar um sistema legado com regras de negócio existentes.
   Identificar problemas de qualidade de código, code smells e riscos de manutenção.
   Planejar uma refatoração segura, preservando o comportamento atual do sistema.
   Aplicar boas práticas de Clean Code, SOLID, modularização e testes automatizados.
   Produzir documentação técnica simplificada inspirada em práticas de qualidade como o MPS.BR.
   Apresentar evidências objetivas de funcionamento antes e depois da refatoração.

3. Regras Gerais do Trabalho

O trabalho deverá ser realizado em grupo, conforme orientação do professor. Cada grupo deverá entregar um pacote completo de modernização do sistema legado.
3.1 Restrições obrigatórias

    Não alterar a classe Item.
    Não alterar a propriedade Items da classe GildedRose.
    Preservar o comportamento existente para os itens já definidos no problema.
    Adicionar corretamente a regra dos itens Conjurados (Conjured).
    Evitar refatorações arriscadas sem testes ou evidências.
    Documentar claramente as decisões tomadas.

4. Passo a Passo da Atividade
   Passo 1 - Leitura e compreensão do problema

A equipe deve ler integralmente a especificação de requisitos do Gilded Rose. Antes de alterar qualquer código, é necessário compreender as regras dos itens comuns, Aged Brie, Sulfuras, Backstage Passes e Conjured.
Passo 2 - Execução inicial do sistema

Executem o projeto original e observem o comportamento do sistema. Registrem como o sistema se comporta antes da refatoração. Essa etapa servirá como base para comparação posterior.
Passo 3 - Diagnóstico técnico do código legado

Analisem o código atual e identifiquem problemas de design, legibilidade, duplicação, excesso de condicionais, responsabilidades misturadas, baixa testabilidade e possíveis violações de boas práticas.
Passo 4 - Documentação dos requisitos

Organizem as regras de negócio em requisitos funcionais e não funcionais. O objetivo é transformar a descrição narrativa do problema em uma documentação técnica simples e rastreável.
Passo 5 - Plano de contingência e refatoração

Antes de modificar o código, definam uma estratégia de refatoração. Indiquem riscos, cuidados, ordem das mudanças, critérios de validação e como a equipe evitará quebrar funcionalidades existentes.
Passo 6 - Criação de testes de caracterização

Criem testes que capturem o comportamento atual do sistema. Esses testes funcionam como uma rede de segurança para garantir que a refatoração não altere comportamentos já existentes.
Passo 7 - Refatoração incremental

Refatorem o código em pequenas etapas. Melhorem nomes, removam duplicações, reduzam condicionais complexas e separem responsabilidades, sempre executando os testes ao longo do processo.
Passo 8 - Implementação dos itens Conjurados

Após a refatoração inicial, implementem a regra dos itens Conjurados: eles devem perder qualidade duas vezes mais rápido que os itens comuns, respeitando os limites de qualidade.
Passo 9 - Testes finais e evidências

Executem todos os testes, registrem evidências e comparem o comportamento antes e depois. Incluam prints, logs, relatório de cobertura se houver e explicações sobre os resultados.
Passo 10 - Preparação da entrega

Organizem o repositório, finalizem a documentação, revisem o README e preparem uma apresentação curta com os principais achados, decisões e aprendizados. 5. Entregáveis Obrigatórios

Todas as entregas devem estar bem organizadas no repositório ou em uma pasta compactada. Recomenda-se separar a documentação em uma pasta chamada docs e os testes em uma pasta chamada tests.
5.1 Relatório de diagnóstico técnico

    O relatório deve descrever os principais problemas encontrados no código legado.
    Identifique code smells, duplicações, nomes pouco claros, funções ou métodos com muitas responsabilidades, excesso de condicionais e baixa testabilidade.
    Explique por que esses problemas dificultam manutenção, evolução e confiabilidade do sistema.
    Sempre que possível, cite trechos ou arquivos do código onde o problema ocorre.

5.2 Documento de requisitos

    Documente as regras do sistema em formato claro e organizado.
    Inclua requisitos funcionais, como atualização de qualidade dos itens comuns, Aged Brie, Sulfuras, Backstage Passes e Conjured.
    Inclua requisitos não funcionais, como manutenibilidade, testabilidade, legibilidade, preservação de comportamento e respeito aos limites de qualidade.
    Use uma numeração simples, por exemplo: RF01, RF02, RNF01, RNF02.

5.3 Plano de contingência e refatoração

    Descreva a estratégia que a equipe usará para modificar o sistema com segurança.
    Informe quais partes do código serão alteradas e quais não podem ser alteradas.
    Liste riscos, como quebra de regra de negócio, alteração indevida da classe Item ou perda de comportamento existente.
    Explique como os testes serão usados para reduzir riscos durante a refatoração.

5.4 Código refatorado

    Entregue o código final com melhoria de organização, legibilidade e manutenção.
    O código deve respeitar a restrição de não alterar a classe Item nem a propriedade Items da classe GildedRose.
    A solução deve reduzir complexidade e facilitar a inclusão de novas regras no futuro.
    A regra dos itens Conjurados deve estar implementada corretamente.
    Obrigatória utilização de um padrão arquitetural como arquitetura limpa ou hexagonal.

5.5 Testes automatizados

    Crie testes automatizados, preferencialmente com pytest.
    Os testes devem cobrir itens comuns, Aged Brie, Sulfuras, Backstage Passes e Conjured.
    Os testes devem demonstrar que o comportamento existente foi preservado após a refatoração.

5.6 Evidências de execução

    Inclua prints ou logs da execução dos testes.
    Apresente evidências do comportamento antes e depois da refatoração.
    Se possível, inclua relatório de cobertura de testes.
    As evidências devem ser suficientes para demonstrar que a solução foi validada.

5.7 README técnico

    O README deve explicar como instalar dependências, executar o sistema e rodar os testes.
    Deve conter um resumo da solução adotada e das principais decisões de refatoração.
    Também deve indicar a estrutura de pastas do projeto.
    O README deve permitir que outra pessoa consiga executar o projeto sem depender de explicações externas.

5.8 Apresentação curta

    Cada grupo deverá realizar uma apresentação objetiva, com duração de 10 a 15 minutos.
    A apresentação deve destacar os principais problemas encontrados, a estratégia adotada, as melhorias realizadas e os resultados dos testes.
    O foco deve estar na justificativa técnica das decisões, não apenas na demonstração do código.

6. Documentação Simplificada Inspirada no MPS.BR

A documentação solicitada nesta atividade não corresponde a uma implantação completa do MPS.BR. Ela é uma versão simplificada, usada com finalidade didática, para estimular práticas de processo, qualidade, rastreabilidade e melhoria de software.

Elemento da documentação

O que deve conter

Finalidade na atividade

Problema e contexto

Descrição do sistema legado e das dificuldades encontradas.

Compreender o cenário de manutenção.

Requisitos

Regras funcionais e atributos de qualidade esperados.

Transformar narrativa em especificação.

Riscos e contingência

Riscos da refatoração e ações preventivas.

Planejar mudanças seguras.

Testes e validação

Casos de teste e evidências de execução.

Comprovar preservação de comportamento.

Melhoria realizada

Descrição das alterações e justificativas.

Demonstrar evolução da qualidade.

Lições aprendidas

Dificuldades, aprendizados e limitações.

Refletir sobre o processo de modernização. 7. Estrutura Recomendada da Entrega

A estrutura abaixo é uma sugestão para organização do repositório final:

gilded-rose-modernizacao/
├── README.md
├── src/
│ └── codigo_refatorado.py
├── tests/
│ └── test_gilded_rose.py
├── docs/
│ ├── diagnostico_tecnico.pdf ou .docx
│ ├── requisitos.pdf ou .docx
│ ├── plano_contingencia.pdf ou .docx
│ └── evidencias_testes.pdf ou .docx
└── apresentacao/
└── slides.pdf 8. Orientações de Qualidade

    Prefira refatorações pequenas e progressivas, evitando reescrever tudo de uma vez.
    Crie testes antes de grandes mudanças no código.
    Não modifique estruturas proibidas pela especificação.
    Explique as decisões técnicas no relatório, mesmo quando a solução parecer simples.
    Evite copiar soluções prontas sem compreensão. O relatório e a apresentação devem demonstrar domínio da equipe.
    Valorize clareza, organização e preservação do comportamento do sistema.

9. Barema de Avaliação

A nota final será atribuída com base nos critérios abaixo, totalizando 10,0 pontos.

Critério

Descrição esperada

Pontuação

Observações

Diagnóstico técnico

Identificação clara de code smells, problemas de design, riscos e dificuldades de manutenção.

1,0

Deve relacionar problemas ao código existente.

Documentação de requisitos

Requisitos funcionais e não funcionais organizados, coerentes e rastreáveis às regras do problema.

1,0

Usar numeração como RF01, RF02, RNF01.

Plano de contingência/refatoração

Estratégia de refatoração segura, com riscos, ações preventivas e ordem de execução.

1,0

Deve explicar como evitar quebrar o sistema.

Código refatorado

Melhoria real de legibilidade, organização, redução de duplicação e separação de responsabilidades.

1,0

Não alterar Item nem Items.

Implementação dos itens Conjured

Regra implementada corretamente, respeitando degradação dobrada e limites de qualidade.

0,5

Deve estar coberta por testes.

Testes automatizados

Testes para itens comuns, Aged Brie, Sulfuras, Backstage Passes, Conjured e casos de borda.

1,0

Preferencialmente com pytest.

Evidências de execução

Prints, logs, antes/depois e/ou cobertura comprovando funcionamento.

0,5

As evidências devem estar organizadas.

README técnico e organização

Instruções claras de execução, estrutura de pastas e resumo das decisões.

1,0

Permite reproduzir a solução.

Apresentação e defesa técnica

Comunicação objetiva dos problemas, decisões, resultados e aprendizados.

3,0

Apresentação de 10 a 15 minutos. 10. Resultado Esperado

Ao final da atividade, espera-se que cada equipe entregue uma versão modernizada do sistema Gilded Rose, acompanhada de documentação técnica, testes automatizados e evidências de validação. A avaliação considerará não apenas o código final, mas também a qualidade do processo de análise, planejamento, documentação e justificativa das decisões técnicas.

11. Regra de Dependência entre Entregáveis
    Critério Eliminatório Parcial

O processo de modernização de software deve seguir uma sequência lógica de engenharia e qualidade. Portanto, as etapas do projeto possuem dependência entre si.

Caso o grupo deixe de entregar qualquer um dos entregáveis obrigatórios das etapas iniciais, será aplicada penalidade na nota final do trabalho.
Penalidade
Problema Penalidade
Ausência do Diagnóstico Técnico -3,0
Ausência do Plano de Contingência -3,0
Ausência de Testes Automatizados -3,0
Código não executa Nota máxima limitada a 5,0
Alterar classe Item indevidamente -2,0
Não implementar Conjured corretamente -2,0
