# 🛡️ Dashboard de Monitoramento - Defesa Social e Integração Comunitária

## 📌 Visão Geral

Este projeto é uma aplicação web interativa desenvolvida em Python para análise e monitoramento de métricas de segurança pública e apoio comunitário. O sistema processa uma base de dados de ocorrências simuladas e as apresenta através de um dashboard dinâmico, facilitando a extração de insights e a tomada de decisões estratégicas.

O projeto foi construído para demonstrar a integração de bibliotecas modernas de processamento de dados e renderização de interfaces declarativas, cumprindo os requisitos da avaliação final da disciplina de Python.

---

## 🚀 Principais Funcionalidades

- **Geração de Dados Sintéticos:** Script dedicado (`gerador_dados.py`) que utiliza a biblioteca Faker para criar uma base de dados realista (CSV) com 500 registros de ocorrências (ex.: Mediação de Conflitos, Perturbação do Sossego).
- **Processamento e Estruturação:** Limpeza e sumarização de dados brutos utilizando DataFrames do Pandas.
- **Dashboard Interativo Web:** Interface visual construída com Streamlit, apresentando gráficos de barras e métricas em tempo real.
- **Indicadores de Desempenho (KPIs):** Monitoramento instantâneo do volume total de ocorrências, bairros afetados e status de resolução (Pendente, Em Andamento e Resolvido).

---

## 🛠️ Stack Tecnológica

- **Linguagem:** Python 3.10+
- **Interface Gráfica:** Streamlit
- **Manipulação de Dados:** Pandas
- **Mock de Dados:** Faker

---

## 📂 Estrutura do Projeto

```text
📦 projeto-python
 ┣ 📜 gerador_dados.py         # Script para geração da base de dados fictícia
 ┣ 📜 dashboard.py            # Script principal da aplicação web (Interface)
 ┣ 📜 dados_defesa_social.csv # Arquivo gerado automaticamente
 ┗ 📜 README.md               # Documentação do projeto
⚙️ Como Executar o Projeto Localmente

Siga as instruções abaixo para configurar o ambiente e executar a aplicação na sua máquina.

1. Clonar o Repositório

Primeiro, faça o clone do projeto para o seu diretório local:

git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
2. Criar e Ativar o Ambiente Virtual (Recomendado)

Para evitar conflitos com outras bibliotecas do seu sistema, crie um ambiente virtual.

No Windows
python -m venv venv
venv\Scripts\activate
No Linux/macOS
python3 -m venv venv
source venv/bin/activate
3. Instalar as Dependências

Com o ambiente ativado, instale as bibliotecas necessárias para o projeto:

pip install pandas streamlit faker
4. Gerar a Base de Dados

Antes de iniciar a interface visual, é necessário gerar os dados de teste.

python gerador_dados.py

Nota: Aguarde a confirmação:

Arquivo 'dados_defesa_social.csv' gerado com sucesso!

5. Iniciar o Dashboard Web

Para executar a aplicação web, utilize o comando abaixo. O prefixo python -m garante que o sistema operacional localize corretamente o executável do Streamlit.

python -m streamlit run dashboard.py
