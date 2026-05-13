# TMDB Movies Data Pipeline (2026)

## Visão Geral

Projeto End-to-End de Engenharia de Dados utilizando a API do TMDB para coleta, transformação e análise de filmes lançados em 2026.

O pipeline foi desenvolvido localmente utilizando Docker, PostgreSQL, Python e Power BI, seguindo a arquitetura moderna de dados em camadas:

* Bronze → Dados brutos
* Silver → Dados tratados
* Gold → Dados analíticos

O projeto foi criado com foco em:

* Portfólio de Engenharia de Dados
* Pipeline ETL/ELT moderno
* Integração com APIs
* Modelagem de dados
* Visualização analítica no Power BI
* Boas práticas com Docker

---

# Arquitetura do Projeto

```text
TMDB_Project-main/
│
├── app/
│   ├── bronze/
│   │   └── load_bronze.py
│   │
│   ├── silver/
│   │   └── transform_silver.py
│   │
│   ├── gold/
│   │   └── transform_gold.py
│   │
│   ├── ingestion/
│   │   └── tmdb_extractor.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── utils/
│   │   ├── db_connection.py
│   │   └── genres.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── docker/
│   └── docker-compose.yml
│
├── TMDB_Dashboard.pbix
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

# Tecnologias Utilizadas

## Linguagens

* Python 3.10
* SQL

## Banco de Dados

* PostgreSQL 15

## Orquestração

* Docker
* Docker Compose

## Bibliotecas Python

* pandas
* sqlalchemy
* psycopg2
* requests

## BI e Visualização

* Power BI

## Fonte de Dados

* TMDB API

---

# Fluxo do Pipeline

## 1. Ingestion

Arquivo:

```text
app/ingestion/tmdb_extractor.py
```

Responsável por:

* Consumir a API do TMDB
* Buscar filmes lançados em 2026
* Aplicar filtros de data
* Retornar os dados brutos

### Regras aplicadas

* Apenas filmes com pelo menos 7 dias de lançamento
* Idioma em português (pt-BR)
* Região Brasil
* Filmes com quantidade mínima de votos

---

## 2. Bronze Layer

Arquivo:

```text
app/bronze/load_bronze.py
```

Responsável por:

* Receber os dados brutos da API
* Carregar no PostgreSQL
* Persistir tabela `bronze_movies`

### Características

* Dados sem tratamento
* Estrutura original da API
* Camada histórica

---

## 3. Silver Layer

Arquivo:

```text
app/silver/transform_silver.py
```

Responsável por:

* Limpeza dos dados
* Conversão de tipos
* Remoção de duplicados
* Tratamento de datas
* Conversão de gêneros

### Tabela gerada

```sql
silver_movies
```

### Principais colunas

* id
* title
* release_date
* release_year
* vote_average
* vote_count
* popularity
* genres
* original_language

---

## 4. Gold Layer

Arquivo:

```text
app/gold/transform_gold.py
```

Responsável por:

* Criação da camada analítica
* Agregações
* Métricas para dashboards

### Tabela gerada

```sql
gold_movies
```

### Métricas disponíveis

* Média de avaliações
* Popularidade média
* Quantidade de filmes
* Filmes por gênero
* Filmes por idioma
* Filmes por ano

---

# Configuração do Ambiente

## 1. Clonar o repositório

```bash
git clone <repo>
```

---

## 2. Criar arquivo .env

```env
API_KEY=SUA_API_KEY
BASE_URL=https://api.themoviedb.org/3
```

---

## 3. Build do projeto

Dentro da pasta docker:

```bash
docker compose up --build
```

---

## 4. Resetar containers

Caso necessário:

```bash
docker compose down -v
```

---

# Banco de Dados

## Conexão PostgreSQL

| Campo    | Valor     |
| -------- | --------- |
| Host     | localhost |
| Porta    | 5433      |
| Database | tmdb_db   |
| Usuário  | admin     |
| Senha    | lz1600    |

---

# Estrutura das Tabelas

## Bronze

```sql
bronze_movies
```

Dados crus vindos diretamente da API.

---

## Silver

```sql
silver_movies
```

Dados tratados e padronizados.

---

## Gold

```sql
gold_movies
```

Dados analíticos para consumo no Power BI.

---

# Dashboard Power BI

Arquivo:

```text
TMDB_Dashboard.pbix
```
---



