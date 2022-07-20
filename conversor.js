// INcluindo a Api
const api =  "https://api.exchangerate-api.com/v4/latest/USD";
// para selecionar controles diferentes
var search = document.querySelector('.searchBox')
var concert = document.querySelector('.convert')
var daMoeda = document.querySelector('.from')
var ParaMoeda = document.querySelector('.to')
var ValorFinal = document.querySelector('.valorFinal')
var QuantidadeFinal = document.querySelector('quantidadeFinal')
var resulatadoDe;
var resultadoPara;
var searchValor;
// Evento quando a moeda é alterada
ParaMoeda.addEventListener('change',(event) =>{
    resulatadoDe = `${event.target.value}`
})
ParaMoeda.addEventListener('change',(event) =>{
    resultadoPara = `${event.target.value}`
})
search.addEventListener('input',updateValur)
//função para atualização de valor
function updateValur(e){
    searchValor = e.target.value;
}
// quando o usuário clica, ele chama a função getresults --> Pegar o resultado
concert.addEventListener("click",PegarResultado)
// Função para pegar o Resultado 
function PegarResultado(){
    fetch(`${api}`)
        .then(currency =>{
            return currency.json();
        }).then(displayresultado)
}
// exibir resultados após a conversão
function displayresultado(currency){
    let daTaxa = currency.rates[resulatadoDe];
    let ParaTaxa = currency.rates[resultadoPara]
    ValorFinal.innerHTML = ((daTaxa/ParaTaxa) * searchValor).toFixed(2);
    QuantidadeFinal.style.display = "block";
}
// quando o usuário clica no botão reset
function clearAll(){
    windom.location.reload();
    document.getElementsByClassName("ValorFinal").innerHTML = "";
}
