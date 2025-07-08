# 🛠️ Pipeline de Extração de Dados: API → MongoDB → MySQL

Este projeto implementa uma pipeline de dados em Python que realiza as seguintes etapas:

1. **Extração** de dados a partir de uma API.
2. **Armazenamento** dos dados no banco NoSQL **MongoDB**.
3. **Inserção final** dos dados no banco relacional **MySQL**.

---

## 🚀 Tecnologias utilizadas

- **Python 3.10.12**
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://requests.readthedocs.io/)
- [PyMongo](https://pymongo.readthedocs.io/)
- [MySQL Connector Python](https://pypi.org/project/mysql-connector-python/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🗂️ Estrutura do projeto

```bash
├── data/                 # Arquivos CSV utilizados
├── notebooks/            # Notebooks Jupyter de desenvolvimento
├── scripts/              # Scripts Python separados por função
├── .env_example          # Modelo de variáveis de ambiente (sem senhas)
├── requirements.txt      # Dependências do projeto
├── .gitignore            # Arquivos/pastas ignoradas pelo Git


⚙️ Como executar o projeto
1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/jessicalvc/pipeline-python-mongo-mysql.git
cd pipeline-python-mongo-mysql
2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Configure suas variáveis de ambiente
Crie um arquivo .env com base no .env_example e insira:

env
Copiar
Editar
MONGO_URI=...
MYSQL_HOST=...
MYSQL_USER=...
MYSQL_PASSWORD=...
MYSQL_DATABASE=...


📒 Notebooks disponíveis
Os notebooks na pasta notebooks/ podem ser usados para:

Testar conexões com MongoDB e MySQL

Visualizar os dados extraídos

Explorar transformações antes da carga final

🧠 Aprendizados
Este projeto foi desenvolvido com foco em:

Integração de bancos SQL e NoSQL

Automação de ETL com Python

Boas práticas com .env e .gitignore

Organização de portfólio para vagas em dados

📌 Tags
python • etl • api • mongodb • mysql • portfólio • data-pipeline

👩‍💻 Autora
Jessica Cunha
🔗 linkedin.com/in/jessicaalvescunha/

Antes
![image](https://github.com/user-attachments/assets/11654cb0-be5e-479a-8107-b2eacaede3ef)

Depois
![image](https://github.com/user-attachments/assets/aa6f9471-70fc-4c85-ba6e-d43b95eaf555)

![image](https://github.com/user-attachments/assets/87407177-deb4-4236-bc7d-17c83f498ba3)

