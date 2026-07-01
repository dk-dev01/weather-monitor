# 🌦️ Monitoramento Meteorológico

Projeto simples desenvolvido para consultar informações climáticas de uma cidade utilizando uma API externa. Os dados retornados são armazenados em um banco de dados MySQL e disponibilizados por meio de uma API desenvolvida com Flask.

## 🚀 Tecnologias utilizadas

- Python
- Flask
- Flask-CORS
- Requests
- MySQL
- XAMPP
- Postman (testes da API)

## 📦 Bibliotecas necessárias

```bash
pip install flask flask-cors requests
pip install mysql-connector-python
```

## 🗄️ Banco de dados

Crie o banco de dados e a tabela no MySQL (XAMPP):

```sql
CREATE DATABASE meteorologia;
USE meteorologia;

CREATE TABLE temperaturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cidade VARCHAR(100) NOT NULL,
    temperatura DECIMAL(5,1),
    maxima DECIMAL(5,1),
    minima DECIMAL(5,1),
    umidade DECIMAL(5,2),
    vento INT,
    dataBusca DATETIME
);
```

## ▶️ Executando o projeto

Inicie a aplicação com:

```bash
python app.py
```

## 🧪 Testes da API

Os endpoints foram testados utilizando o **Postman**.

Cidade válida:

```text
http://127.0.0.1:5000/clima/bauru
```

Cidade inválida:

```text
http://127.0.0.1:5000/clima/sdfgsgsdgsg
```

## 📌 Funcionalidades

- Consulta de clima por cidade.
- Consumo de API meteorológica externa.
- Armazenamento das consultas em MySQL.
- API REST desenvolvida com Flask.
- Testes realizados com Postman.
