from flask import Flask, jsonify, request #framework que cria a api
from flask_cors import CORS #comunicacao segura entre front e back

from database import conectar
from api import buscarClima

app = Flask(__name__)
CORS(app)

#insert de dados na tabela temperaturas
def salvar_no_banco(dados):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    insert into temperaturas
    (cidade, temperatura, maxima, minima, umidade, vento, dataBusca)
    values (%s, %s, %s, %s, %s, %s, now())
    '''

    valor = (
        dados['cidade'],
        dados['temperatura'],
        dados['temp_max'],
        dados['temp_min'],
        dados['umidade'],
        dados['vento']
    )

    #executa e confirma o insert na tabela
    cursor.execute(sql, valor)
    conexao.commit()

    cursor.close()
    conexao.close()

#porta de entrada da api com metodo get
@app.route('/clima/<cidade>', methods=['GET'])
def clima_get(cidade):
    dados = buscarClima(cidade)

    if dados is None:
        return jsonify({
            'erro': 'cidade não encontrada'
        }), 404

    salvar_no_banco(dados)

    return jsonify(dados), 200

#metodo postque faz memsa coisa q get, nesse caso
@app.route('/clima', methods=['POST'])
def clima_post():
    corpo = request.get_json()

    if not corpo or 'cidade' not in corpo:
        return jsonify({
            'erro': 'informe a cidade corretamente'
        }), 400

    cidade = corpo['cidade']

    dados = buscarClima(cidade)

    if dados is None:
        return jsonify({
            'erro': 'cidade não encontrada'
        }), 404

    salvar_no_banco(dados)

    return jsonify(dados), 201

#grafico de linha
@app.route('/dashboard/<cidade>')
def dashboard(cidade):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
    select temperatura, dataBusca
    from temperaturas
    where cidade = %s
    order by id desc
    limit 10
    """

    cursor.execute(sql, (cidade,))

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    resultados.reverse()

    labels = []
    temperaturas = []

    for linha in resultados:
        labels.append(linha['dataBusca'].strftime('%H:%M'))
        temperaturas.append(float(linha['temperatura']))
    return jsonify({
        'labels': labels,
        'temperaturas': temperaturas
    })

#reinicia o srv ao edita o código
if __name__ == '__main__':
    app.run(debug=True)