<div align="center">
  
  # 📊 Análise de Vendas no Varejo
  
  [![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
  [![Orange](https://img.shields.io/badge/Orange-3.38%2B-orange)](https://orange.biolab.si/)
  [![SQLite](https://img.shields.io/badge/SQLite-3-003B57)](https://www.sqlite.org/)
  [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

</div>

## 📌 Sobre o Projeto

Projeto focado em engenharia de dados, com ênfase em queries SQL avançadas aplicadas a um pipeline simples de ingestão e análise. O objetivo é demonstrar o uso de CTEs, Window Functions e JOINs em um contexto de dados reais — estrutura que pode ser diretamente aplicada em ferramentas como dbt, Airflow ou Spark SQL.

---

### Queries Parametrizadas
| Arquivo | Operação |
|---|---|
| `3-1-Create.py` | INSERT parametrizado |
| `3-2-Read_Basico.py` | SELECT com limite padrão |
| `3-3-Update.py` | UPDATE por Transaction_ID |
| `3-4-Delete.py` | DELETE por Transaction_ID |
| `3-5-Read_2_5_par.py` | SELECT parametrizado avançado |
| `3-6-Read_one.py` | SELECT por Transaction_ID e ano |

---

## 📐 Conceitos SQL Aplicados

| Conceito | Onde foi usado |
|---|---|
| **CRUD parametrizado** | Create, Read, Update e Delete com parâmetros tipados |
| **CTE** (`WITH`) | Queries do banco 2 nas versões anteriores; Query 1 e 5 do banco 1 |
| **Window Functions** (`OVER`) | Receita acumulada, ranking de categorias, percentual por cliente e por mês |
| **Self JOIN** | Comparação com mês de referência em vendas mensais (Query 1-5) |
| **JOIN** | Percentual por cliente no mês, gênero por categoria (versão original) |
| **LAG** | Comparação de vendas mês a mês (banco 1) |
| **DENSE_RANK()** | Ranking de categorias por quantidade e receita |
| **CASE WHEN** | Tradução de dia numérico para nome da semana; contagem condicional por gênero |
| **strftime/substr** | Extração de ano, mês e dia da semana de datas |
| **Divisão inteira** | Correção com `* 1.0` para porcentagens corretas |
| **Filtro por ano** | `strftime('%Y', Date)` em query parametrizada (Query 3-6) |

---

## 🗂️ Estrutura do Projeto
```
TREINO_SQL/
├── dados/
│   ├── processed/
│   │   ├── retail_sales_clean2.db
│   │   └── retail_sales1.db
│   ├── raw_datasets/
│   │   └── mock_kaggle.csv
│   └── report/
│       ├── orange_data_cleaning/
│       │   ├── missing_values.png
│       │   ├── redundant_column.png
│       │   ├── retail_sales_ver2.csv
│       │   ├── structure.png
│       │   └── unique.png
│       └── retail_sales_dataset2.csv
├── outputs/
│   ├── queries_db1_output/
│   │   ├── maior_venda_por_ano.png
│   │   ├── maiores_vendas.png
│   │   ├── menores_vendas.png
│   │   ├── vendas_comparando_mes.png
│   │   └── vendas_por_semana.png
│   ├── queries_db2_output/
│   │   ├── compras_acima_media.png
│   │   ├── genero_por_categoria.png
│   │   ├── join_compradores.png
│   │   ├── maiores_compradores.png
│   │   ├── renda_acumulada.png
│   │   └── vendas_renda_categoria_ra.png
│   └── queries_parametrizadas/
│       ├── delete+after_delete/
│       │   ├── after_delete.png
│       │   └── delete.png
│       ├── update+after_update/
│       │   ├── after_update.png
│       │   └── update.png
│       ├── create.png
│       ├── read_basico.png
│       ├── read_one.png
│       └── read_parametrizado_2-5.png
├── scripts/
│   ├── queries/
│   │   ├── queries_db1/
│   │   ├── queries_db2/
│   │   └── queries_parametrizadas/
│   │       ├── 3-1-Create.py
│   │       ├── 3-2-Read_Basico.py
│   │       ├── 3-3-Update.py
│   │       ├── 3-4-Delete.py
│   │       ├── 3-5-Read_2_5_par.py
│   │       └── 3-6-Read_one.py
│   ├── clean_retail2.py
│   └── download_conn_retail1.py
├── .gitignore
└── README.md
```

---

## 🖼️ Outputs — Lógica por trás de cada imagem

Cada query gera um print do terminal salvo como `.png`, documentando o resultado real da execução. A organização segue a mesma estrutura das queries.

### Banco 1 — `queries_db1_output/`

| Imagem | O que mostra |
|---|---|
| `maior_venda_por_ano.png` | A transação de maior valor agrupada por ano — valida se há variação significativa de ticket máximo entre períodos |
| `maiores_vendas.png` | Top N transações em valor absoluto — identifica os outliers de receita no dataset |
| `menores_vendas.png` | Transações de menor valor — útil para entender o ticket mínimo e possíveis registros inconsistentes |
| `vendas_comparando_mes.png` | Comparação de receita entre meses usando `LAG` — evidencia crescimento ou queda mês a mês |
| `vendas_por_semana.png` | Distribuição de vendas por dia da semana via `CASE WHEN` — mostra padrões de comportamento semanal |

### Banco 2 — `queries_db2_output/`

| Imagem | O que mostra |
|---|---|
| `maiores_compradores.png` | Clientes rankeados por receita total gerada — base para análise de clientes de alto valor |
| `compras_acima_media.png` | Clientes cujo gasto total supera a média geral — segmentação simples de comportamento de compra |
| `renda_acumulada.png` | Receita acumulada mês a mês com Window Function — visualiza a curva de crescimento do negócio |
| `join_compradores.png` | Percentual de contribuição de cada cliente na receita do seu mês — calculado com Window Function diretamente no SELECT, sem JOIN entre CTEs |
| `vendas_renda_categoria_ra.png` | Ranking de categorias por quantidade vendida e receita gerada com `DENSE_RANK()` — dois rankings calculados em um único SELECT sem CTEs |
| `genero_por_categoria.png` | Percentual de vendas por gênero dentro de cada categoria — calculado com `CASE WHEN` condicional em um único SELECT, sem CTEs separadas por gênero |

### Queries Parametrizadas — `queries_parametrizadas/`

| Imagem | O que mostra |
|---|---|
| `create.png` | Terminal após INSERT — confirma que o novo registro foi inserido com os parâmetros fornecidos |
| `read_basico.png` | Resultado do SELECT com limite padrão — valida a leitura básica do banco |
| `read_one.png` | Resultado do SELECT filtrado por Transaction_ID e ano — demonstra o uso de dois parâmetros combinados com `strftime` |
| `read_parametrizado_2-5.png` | SELECT com múltiplos filtros — mostra o resultado de uma leitura mais específica com parâmetros avançados |
| `update.png` | Estado do registro **antes** do UPDATE — serve como referência do valor original |
| `after_update.png` | Estado do registro **após** o UPDATE — confirma que a alteração foi aplicada corretamente |
| `delete.png` | Estado do registro **antes** do DELETE — documenta o que existia antes da remoção |
| `after_delete.png` | Tentativa de SELECT após o DELETE — retorna vazio, confirmando que o registro foi removido |

> **Nota:** Os pares `update/after_update` e `delete/after_delete` foram intencionalmente organizados em subpastas separadas para deixar clara a sequência antes/depois de cada operação destrutiva.

---

## ⚡ Refatoração — CTE para Window Function

Três queries do Banco 2 foram reescritas com foco em eficiência, eliminando CTEs e JOINs desnecessários em favor de Window Functions e agregações condicionais executadas em uma única passagem pela tabela.

### `2-4-join_compradores_rendapMes.py`

**Antes:** duas CTEs (`soma_user` e `ano_mes`) calculavam separadamente o total por cliente e o total por mês, que eram então combinados via `JOIN`.

**Depois:** o total do mês é calculado diretamente com `SUM(Total_Amount) OVER (PARTITION BY strftime('%Y', Date), strftime('%m', Date))`, eliminando a CTE `ano_mes` e o JOIN. Tudo resolve em um único SELECT.

---

### `2-5-vendas_renda_categoria.py`

**Antes:** duas CTEs (`por_receita` e `por_quantidade`) calculavam `RANK()` separadamente para receita e quantidade, com um `JOIN` final para unir os resultados por categoria.

**Depois:** dois `DENSE_RANK() OVER (...)` são aplicados diretamente no mesmo SELECT — `rank_sum` por receita e `rank_quant` por quantidade — eliminando ambas as CTEs e o JOIN entre elas.

---

### `2-6-genero_pcategoria.py`

**Antes:** duas CTEs (`masc_cat` e `fem_cat`) filtravam os dados por gênero separadamente com `WHERE Gender = 'Male'` e `WHERE Gender = 'Female'`, seguidas de um `JOIN` por categoria.

**Depois:** `COUNT(CASE WHEN Gender = 'Male' THEN 1 END)` e `COUNT(CASE WHEN Gender = 'Female' THEN 1 END)` calculam ambas as contagens em um único SELECT sem filtro, sem CTEs e sem JOIN.

---

> **Por que isso importa:** as versões com CTE + JOIN forçam o banco a materializar subconjuntos intermediários e percorrer a tabela múltiplas vezes. As versões com Window Function e agregação condicional executam em uma única passagem, reduzindo I/O e facilitando a leitura da lógica.

---

## 📦 Datasets

**Banco 1 — `retail_sales1.db`**
Dataset de vendas com foco em séries temporais — análise por dia, semana e mês.

**Banco 2 — `retail_sales_clean2.db`**
Dataset de varejo com foco em comportamento de clientes e categorias de produtos.

Os dois bancos são independentes e treinam contextos diferentes de análise, elas não possuem relação entre si. A decisão de abordar 2 datasets diferentes, veio da ideia de extrair dados de duas formas diferentes, uma por meio da API do Kaggle, e a outra por download na máquina e conversão em tabela SQLite por meio da biblioteca Pandas.

---

## 🧹 Processo de Limpeza

A exploração inicial foi feita no **Orange Data Mining** para identificar visualmente valores ausentes, colunas redundantes e inconsistências na estrutura do dataset.

O problema encontrado foi que ao exportar pelo Orange, o arquivo era salvo com todas as colunas colapsadas em uma só, separadas por `\t`, com linhas de metadata no topo, corrompendo a leitura pelo SQLite.

A solução foi importar o CSV original **direto pelo pandas**, sem passar pelo Orange:
```python
df = pd.read_csv('dados/raw_datasets/retail_sales_dataset.csv')
df.columns = df.columns.str.strip().str.replace(' ', '_')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.to_sql('vendas2', conn, if_exists='replace', index=False)
```

Vale destacar que a limpeza foi efetuada apenas no segundo dataset, que tinha espaços como separadores. O primeiro dataset (`mock_kaggle.csv`) não teve limpeza, por não ter dados ausentes ou colunas com nomenclatura que geraria problema para o SQLite.

---

## 🔍 Queries Desenvolvidas

### Banco 1
| Arquivo | Pergunta respondida |
|---|---|
| `1-1-maior_venda_p_ano.py` | Qual foi a maior venda por ano? |
| `1-2-maiores_vendas.py` | Quais foram as maiores vendas? |
| `1-3-menores_vendas.py` | Quais foram as menores vendas? |
| `1-4-query_vendas_semana.py` | Como as vendas se distribuem por semana? |
| `1-5-vendas_mes_passado.py` | Qual foi o volume de vendas no mês passado? |

### Banco 2
| Arquivo | Pergunta respondida |
|---|---|
| `2-1-maiores_compradores.py` | Quais clientes geraram mais receita? |
| `2-2-compradores_acima_media.py` | Quais clientes compraram acima da média? |
| `2-3-renda_acumulada.py` | Qual a receita acumulada mês a mês? |
| `2-4-join_compradores_rendap.py` | Qual o percentual de cada cliente na receita do mês? |
| `2-5-vendas_renda_categoria.py` | Ranking de categorias por quantidade e receita? |
| `2-6-genero_pcategoria.py` | Qual o percentual de cada gênero por categoria? |

### Queries Parametrizadas
| Arquivo | O que faz |
|---|---|
| `3-1-Create.py` | Insere uma nova transação via parâmetros tipados |
| `3-2-Read_Basico.py` | Lê transações com limite padrão configurável |
| `3-3-Update.py` | Atualiza um registro por Transaction_ID |
| `3-4-Delete.py` | Remove um registro por Transaction_ID |
| `3-5-Read_2_5_par.py` | SELECT avançado com múltiplos filtros parametrizados |
| `3-6-Read_one.py` | Busca uma transação específica por ID e ano |

---

## 🚀 Como Rodar

**1. Instalar dependências:**
```bash
pip install pandas
```

**2. Limpar e importar o dataset:**
```bash
python scripts/clean_retail2.py
python scripts/download_conn_retail1.py
```

**3. Rodar uma query:**
```bash
python scripts/queries/queries_db2/2-1-maiores_compradores.py
```

**4. Rodar uma query parametrizada:**
```bash
python scripts/queries/queries_parametrizadas/3-6-Read_one.py
# Digite o ID da transação e o ano quando solicitado
```

---

## 🛠️ Tecnologias

- **Python** — pandas, sqlite3
- **SQLite** — banco de dados local
- **Orange Data Mining** — exploração visual inicial
- **VS Code** — ambiente de desenvolvimento