async function buscarTemperatura(){
    const cidade = document.getElementById('cidade').value;
    const buscaAPI = await fetch(`http://127.0.0.1:5000/clima/${cidade}`);
    const dados = await buscaAPI.json();
    const temperatura = document.getElementById('temperatura');

    let msg;

    if (cidade.trim() === "") {
        temperatura.innerHTML = `
             <div class="resultado erro">
                <div class="icone-clima">❌</div>
                <strong>DIGITE UMA CIDADE!</strong>
            </div>
        `;
    }
    else if (dados.erro){
        temperatura.innerHTML = `
             <div class="resultado erro">
                <div class="icone-clima">⚠️</div>
                <strong>CIDADE NÃO ENCONTRADA!</strong>
            </div>
        `;
    } 
    else {
        if(dados.temperatura > 26){
            msg = "🔥 O clima está quente 🔥";
        }
        else if(dados.temperatura < 20){
            msg = "❄️ O clima está frio ❄️";
        }
        else{
            msg = "🌤️ O clima está normal 🌤️";
        }

        temperatura.innerHTML = `
    <div class="card-clima">
        <h2 class="cidade">${dados.cidade}</h2>

        <div class="linha-temperatura">
            <div class="info">
                <span class="titulo-info">MÍNIMA</span>
                <h3>${dados.temp_min}ºC</h3>
            </div>
            <div class="info principal">
                <span class="titulo-info">TEMPERATURA</span>
                <h1>${dados.temperatura}ºC</h1>
            </div>
            <div class="info">
                <span class="titulo-info">MÁXIMA</span>
                <h3>${dados.temp_max}ºC</h3>
            </div>
        </div>

        <div class="linha-extra">
            <div class="extra">
                <span>UMIDADE</span>
                <h3>${dados.umidade}%</h3>
            </div>
            <div class="extra">
                <span>VENTO</span>
                <h3>${dados.vento} km/h</h3>
            </div>
        </div>

        <p class="mensagem">${msg}</p>
    </div>
`;
    carregarGrafico(cidade)
    }
}

//grafico de linha em tempo real
let grafico = null;

async function carregarGrafico(cidade) {
    const resposta = await fetch(`http://127.0.0.1:5000/dashboard/${cidade}`);
    const dados = await resposta.json();
    const ctx = document.getElementById('graficoTemperatura');

    // destrói gráfico antigo
    if (grafico != null) {
        grafico.destroy();
    }
    grafico = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dados.labels,
            datasets: [{
                label: 'Temperatura °C',
                data: dados.temperaturas,
                borderWidth: 2,
                tension: 0.3
            }]
        },
        options: {
            responsive: true
        }
    });
}