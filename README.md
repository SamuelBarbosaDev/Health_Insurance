# Health Insurance
### Índice

- [Health Insurance](#health-insurance)
    - [Índice](#índice)
    - [Contextualização:](#contextualização)
    - [Metodologia Aplicada:](#metodologia-aplicada)
  - [Entendimento do Negócio:](#entendimento-do-negócio)
  - [Entendimento dos Dados:](#entendimento-dos-dados)
    - [Variáveis:](#variáveis)
    - [Verificando as Dimensões do DataFrame:](#verificando-as-dimensões-do-dataframe)
    - [Describe:](#describe)
    - [Verificando Valores Nulos:](#verificando-valores-nulos)
    - [Verificando Tipos:](#verificando-tipos)
    - [Gasto com saúde por idade:](#gasto-com-saúde-por-idade)
    - [Gasto com saúde por BMI:](#gasto-com-saúde-por-bmi)
    - [Filhos:](#filhos)
  - [Preparação dos Dados:](#preparação-dos-dados)
    - [Separando features:](#separando-features)
    - [Separando X e Y:](#separando-x-e-y)
    - [Train-test split:](#train-test-split)
    - [Tratando os nulos:](#tratando-os-nulos)
    - [Construção do pipeline de pré-processamento:](#construção-do-pipeline-de-pré-processamento)
  - [Modelagem:](#modelagem)
    - [Pipeline:](#pipeline)
    - [Modelos:](#modelos)
    - [Buscando os melhores modelos:](#buscando-os-melhores-modelos)
    - [Melhor modelo:](#melhor-modelo)
  - [Avaliação:](#avaliação)
  - [Implantação:](#implantação)
  - [Pré-requisitos para executar o projeto:](#pré-requisitos-para-executar-o-projeto)
    - [Ambiente virtual e Dependências:](#ambiente-virtual-e-dependências)


### Contextualização:
A previsão de seguro médico é crucial na área da saúde, pois prevê os custos médicos e ajuda as organizações de saúde a se prepararem para as despesas. Ao analisar fatores como demografia, histórico médico e estilo de vida, as seguradoras podem definir taxas de prêmio precisas e alocar recursos de forma eficiente. Isso também ajuda indivíduos de alto risco a receberem os recursos e apoio necessários. No geral, a previsão de seguro médico é uma ferramenta valiosa tanto para os pacientes quanto para os provedores em um sistema de saúde sustentável.

### Metodologia Aplicada:
A análise foi realizada utilizando o modelo CRISP-DM, o CRISP-DM (Cross Industry Standard Process for Data Mining) é um modelo padrão de processo para projetos de mineração de dados que define um conjunto de fases e tarefas que devem ser executadas para desenvolver soluções de mineração de dados efetivas.

![CRISP-DM](/core/img/CRISP-DM.png)

O modelo CRISP-DM é uma abordagem sistemática e estruturada para a mineração de dados que ajuda as empresas a desenvolver soluções de mineração de dados de maneira eficiente e eficaz, reduzindo o tempo e os custos do projeto.

## Entendimento do Negócio:
Este projeto tem como objetivo prever o custo do seguro de saúde.

## Entendimento dos Dados:
### Variáveis:
| Coluna           | Descrição                                             |
| ---------------- | ----------------------------------------------------- |
| age              | Idade                                                 |
| sex              | Sexo do cliente                                       |
| bmi              | BMI (body mass index) ou indice de masa corporal      |
| children         | Número de filhos                                      |
| smoker           | Se o cliente fuma ou não                              |
| region           | Região onde o cliente reside                          |
| charges          | Custo do cliente                                      |


### Verificando as Dimensões do DataFrame:
![Data Frame](/core/img/shape.png)

### Describe:
![Data Frame](/core/img/describe.png)

### Verificando Valores Nulos:
![Data Frame](/core/img/nulos.png)

### Verificando Tipos:
![Data Frame](/core/img/tipos.png)

### Gasto com saúde por idade:
![Data Frame](/core/img/gasto_com_saude_por_idade.png)

### Gasto com saúde por BMI:
![Data Frame](/core/img/gasto_com_saude_por_bmi.png)

### Filhos:
![Data Frame](/core/img/filhos.png)

## Preparação dos Dados:

### Separando features:
![Data Frame](/core/img/separando_features.png)

### Separando X e Y:
![Data Frame](/core/img/separando_x_e_y.png)

### Train-test split:
![Data Frame](/core/img/train_test_split.png)

### Tratando os nulos:
![Data Frame](/core/img/tratando_os_nulos.png)

### Construção do pipeline de pré-processamento:
![Data Frame](/core/img/pre_processamento.png)


## Modelagem:
### Pipeline:
![Data Frame](/core/img/pipeline.png)

### Modelos:
![Data Frame](/core/img/Modelos.png)

### Buscando os melhores modelos:
![Data Frame](/core/img/the_best_models.png)

### Melhor modelo:
![Data Frame](/core/img/the_best_model.png)

## Avaliação:
Nosso objetivo é prever o custo dos clientes para uma seguradora de saúde com base em algumas características (features), ou seja, prever o custo daquele cliente para a seguradora. Nosso modelo tem como propósito auxiliar na tomada de decisões e contribuir para uma melhor previsibilidade de custos futuros, o que beneficia a saúde financeira da empresa. As características que mais influenciaram nosso modelo foram idade, IMC (Índice de Massa Corporal), quantidade de filhos e se a pessoa fuma ou não.

O modelo que obteve melhor desempenho foi o Gradient Boosting Regressor, com um R2 de 0.84.

Como próximos objetivos em versões futuras para a melhoria contínua do projeto, planejamos fazer o seguinte:

- **Mais features relevantes:** Vamos considerar adicionar mais características relevantes ao modelo de previsão. Por exemplo, informações sobre histórico médico, hábitos de exercício, histórico familiar de doenças, entre outros, podem aumentar a precisão das previsões.

- **Validação externa:** Se possível, iremos validar o modelo em um conjunto de dados externo ou em uma situação real de aplicação. Isso ajudará a verificar a eficácia do modelo em condições reais.

## Implantação:
Iniciando a etapa de implementação do modelo em produção.

## Pré-requisitos para executar o projeto:
Abaixo, listarei os requisitos necessários para que o projeto funcione corretamente.

### Ambiente virtual e Dependências:
Criando ambiente virtual:
```
python3 -m venv core/.venv python=3.10.6
```

Entrando no ambiente virtual:
```
source core/.venv/bin/activate
```

Instale as dependências:
```
pip install -r core/requirements.txt
```

---
Linkedin: <https://www.linkedin.com/in/samuel-barbosa-dev/> 

E-mail: <samueloficial@protonmail.com>