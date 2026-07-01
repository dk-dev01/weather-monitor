# monitoramento meteorológico

projeto simples para consultar o clima de uma cidade, mostrando temperatura atual, máxima, mínima e uma mensagem informando se o clima está frio, normal ou quente.

## bibliotecas necessárias

pip install flask flask-cors requests
pip install mysql-connector-python

## criar banco de dados e tabela no xampp

create database metereologia;
use metereologia;

create table temperaturas (
id int auto_increment primary key,
cidade varchar(100) not null,
temperatura decimal(5,1),
maxima decimal(5,1),
minima decimal(5,1),
umidade decimal(5,2),
vento int,
dataBusca datetime
);

## iniciar aplicação
python app.py

## realizar testes postman
http://127.0.0.1:5000/clima/bauru
http://127.0.0.1:5000/clima/sdfgsgsdgsg