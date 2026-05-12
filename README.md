# 🎬 TMDB Data Engineering Pipeline 

Este projeto implementa um pipeline completo de engenharia de dados utilizando a API do TMDB, com arquitetura em camadas (Medallion Architecture), rodando totalmente em ambiente local com Docker.

---

## 🚀 Objetivo do Projeto

Construir um pipeline end-to-end de engenharia de dados para coletar, transformar e analisar dados de filmes lançados em 2025, simulando um ambiente real de Data Engineering.

---

## 🏗️ Arquitetura do Pipeline

O projeto segue a arquitetura em três camadas:

### 🥉 Bronze (Raw Data)
- Dados brutos extraídos da API do TMDB
- Sem tratamento ou limpeza
- Armazenados diretamente no PostgreSQL

### 🥈 Silver (Clean Data)
- Dados tratados e estruturados
- Remoção de nulos
- Padronização de colunas

### 🥇 Gold (Business Layer)
- Dados agregados e analíticos
- Indicadores como:
  - Top filmes por nota
  - Popularidade média
  - Rankings

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11+
- PostgreSQL
- Docker & Docker Compose
- API TMDB
- psycopg / psycopg2
- requests
- dotenv

---

## 📦 Estrutura do Projeto
```
TMDB_Project/
│
├── app/
│ ├── main.py
│ ├── config/
│ ├── ingestion/
│ ├── bronze/
│ ├── silver/
│ ├── gold/
│ └── utils/
│
├── docker/
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── .gitignore
```



---

## 🔐 Configuração de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
TMDB_API_KEY=your_api_key

DB_HOST=localhost
DB_NAME=tmdb_db
DB_USER=admin
DB_PASSWORD=admin
DB_PORT=5433
```
---

## 🔐 Configuração de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
TMDB_API_KEY=your_api_key

DB_HOST=localhost
DB_NAME=tmdb_db
DB_USER=admin
DB_PASSWORD=admin
DB_PORT=5433
```

---

## 🐳 Como executar o projeto
1. Subir o banco de dados
```env
docker-compose up -d
```
2. Instalar dependências
```env
pip install -r requirements.txt
```
3. Executar pipeline
```env
python -m app.main
```
---

## 📊 Fluxo do Pipeline

```
TMDB API
   ↓
Bronze (Raw Data)
   ↓
Silver (Tratamento)
   ↓
Gold (Análise)
   ↓
PostgreSQL
```
