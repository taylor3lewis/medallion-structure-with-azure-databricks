# Medallion Structure with Azure Databricks

Projeto de portfólio de Data Engineering com arquitetura **Medallion / Lakehouse** usando **Azure ADLS Gen2**, **Azure Databricks**, **PySpark** e **Terraform**.

## Objetivo

Construir um pipeline end-to-end para dados de vagas de emprego sintéticas, cobrindo:

- geração de dados com ruído proposital
- ingestão para ADLS Gen2
- transformação Bronze → Silver → Gold
- provisionamento de infraestrutura com Terraform
- consultas analíticas na Gold via metastore do Databricks

## Arquitetura

### Bronze
Dados brutos em JSON, com múltiplos arquivos no Data Lake.

Características dos dados gerados:
- títulos de vaga com caixa inconsistente e espaços extras
- localizações com formatos variados
- salários em formatos diferentes
- skills duplicadas ou com sinônimos
- campos nulos
- duplicatas exatas e quase-duplicatas

### Silver
Camada de limpeza e padronização:
- trim e normalização textual
- tratamento de nulos
- normalização de skills
- deduplicação
- normalização de localização
- parsing de salário
- criação de `job_id`
- flags de qualidade e lineage por arquivo

### Gold
Camada analítica:
- `fact_jobs`
- `dim_skills`
- `fact_job_skills`
- agregações como top skills, salários e vagas por localização

## Stack

- **Azure**
  - ADLS Gen2
  - Databricks
- **Infra as Code**
  - Terraform
- **Linguagem**
  - Python
- **Processamento**
  - PySpark
- **CLI / utilitários**
  - Databricks CLI
  - dotenv

## Estrutura do repositório

```text
.
├── data/
│   ├── fake_data_gen.py
│   ├── skills.py
│   └── sample/
│       ├── jobs_raw_1.json
│       ├── jobs_raw_2.json
│       ├── jobs_raw_3.json
│       ├── jobs_raw_4.json
│       ├── jobs_raw_5.json
│       └── jobs_raw_6.json
├── ingestion/
│   ├── __init__.py
│   └── upload_to_lake.py
├── notebooks/
│   ├── 01_bronze_to_silver.ipynb
│   ├── 02_validate_silver.ipynb
│   ├── 03_silver_to_gold.ipynb
│   ├── 04_metastore_tables.ipynb
│   ├── 05_sql_queries.ipynb
│   └── 06_analytical_queries.ipynb
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
├── utils/
│   └── utils.py
├── .env.example
└── requirements.txt
```

## Fluxo do projeto

1. **Provisionamento**
   - cria Resource Group
   - cria Storage Account com HNS habilitado
   - cria filesystem no ADLS
   - cria diretórios Bronze / Silver / Gold
   - cria Databricks Workspace
   - cria Service Principal para acesso do Databricks ao ADLS

2. **Geração dos dados**
   - o script `data/fake_data_gen.py` gera arquivos JSON sintéticos com ruído controlado

3. **Ingestão**
   - o script `ingestion/upload_to_lake.py` envia os arquivos para o diretório Bronze no ADLS

4. **Transformações**
   - notebooks do Databricks limpam, padronizam e modelam os dados

5. **Consumo**
   - tabelas Gold são registradas no metastore
   - consultas SQL produzem insights analíticos

## Como executar

### 1. Clonar e criar ambiente

```bash
git clone <seu-repo>
cd <seu-repo>
python -m venv .venv
```

No Windows:

```bash
.venv\\Scripts\\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Copie `.env.example` para `.env` e ajuste os valores.

Exemplo:

```env
AZURE_STORAGE_ACCOUNT_NAME=stjobmarketdev001
AZURE_DATALAKE_FILESYSTEM=job-data
SAMPLE_FOLDER=data/sample/
TARGET_DIRECTORY=bronze
DB_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Observação: o código de ingestão usa `TARGET_DIRECTORY`, mas essa variável não aparece no `.env.example` atual. Adicione-a no seu `.env`.

### 4. Provisionar infraestrutura

Entre na pasta `terraform/` e execute:

```bash
terraform init
terraform plan
terraform apply
```

## Autenticação no Databricks

O projeto usa **OAuth com Service Principal** para acessar o ADLS a partir do Databricks.

Fluxo adotado:
- Service Principal provisionado via Terraform
- secret salvo em **Databricks Secret Scope**
- Spark config do cluster apontando para `{{secrets/<scope>/<key>}}`

Assim, os notebooks não precisam repetir célula de autenticação em toda execução.

## Notebooks

### `01_bronze_to_silver.ipynb`
Leitura da Bronze e construção da Silver:
- leitura de múltiplos JSONs com `multiline=true`
- limpeza textual
- normalização de arrays de skills
- deduplicação
- tratamento de nulos
- flags de qualidade

### `02_validate_silver.ipynb`
Validação da Silver:
- conferência de schema
- checagens básicas de qualidade e contagem

### `03_silver_to_gold.ipynb`
Modelagem analítica na Gold:
- `fact_jobs`
- `dim_skills`
- `fact_job_skills`
- agregações

### `04_metastore_tables.ipynb`
Registro de tabelas externas no metastore.

### `05_sql_queries.ipynb`
Consultas SQL iniciais sobre a Gold.

### `06_analytical_queries.ipynb`
Consultas analíticas de negócio:
- top skills
- salário por área
- vagas por localização
- distribuição de senioridade

## Observações importantes

- o diretório `terraform/` no zip contém arquivos locais de estado e debug que **não devem** ser versionados no GitHub
- arquivos sensíveis como `.env`, `terraform.tfvars` e `terraform.tfstate` devem ficar fora do repositório
- se for publicar este projeto, revise nomes de recursos Azure e quaisquer segredos ou IDs específicos do seu ambiente

## Possíveis melhorias futuras

- migrar a Gold inteiramente para Delta Lake
- automatizar os notebooks com Databricks Workflows
- adicionar dashboard no Power BI ou Databricks SQL
- refatorar transformações em módulos Python reutilizáveis
- adicionar testes de qualidade de dados
- incluir diagrama da arquitetura no README

## Principais aprendizados do projeto

- autenticação segura entre Databricks e ADLS
- leitura correta de JSON multi-linha no Spark
- tratamento de dados semi-estruturados com arrays
- diferenças entre Parquet e Delta
- registro de tabelas externas no metastore
- modelagem de camadas Bronze, Silver e Gold

## Licença

Adicione a licença que preferir, por exemplo MIT.
