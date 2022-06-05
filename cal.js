const BotoesDONumero = document.querySelectorAll('[data-number]')
const OperacaoDeBotoes = document.querySelectorAll('[data-operation]')
const Igualbotoa = document.querySelector('[data-equals]')
const deletarBotoa = document.querySelector('[data-delet]')
const pervirusOperandTextElement = document.querySelector('[data-previous-operand]')
const currentOperandTexrElemnt = document.querySelector('[data-current-operand]')
const allclearButton = document.querySelector('[data-all-clear]')
// Passando os dados do visor que sao pervirusOperandTextElement/currentOperandTexrElemnt
class calculadora{
    // O construtor é um método especial para criar e inicializar um objeto criado a partir de uma classe
    constructor(pervirusOperandTextElement,currentOperandTexrElemnt){
        this.pervirusOperandTextElement = pervirusOperandTextElement;
        this.currentOperandTexrElemnt = currentOperandTexrElemnt;
        this.clear()
    }
    // vai colocar virgulas automaticas na calculadora
    formatDisplayNumber(number){
        const stringNumber = number.toString()
        const interrr = parseFloat(stringNumber.split('.')[0])
        const decimal = stringNumber.split('.')[1]
        let interDisplay;
        if(isNaN(interrr)){
            interDisplay = ""
        }else{
            interDisplay = interrr.toLocaleString("en",{
                maximumFractionDigits: 0
            })
        }
        if (decimal != null){
            return `${interDisplay} ${decimal}`
        }else{
            return interDisplay;
        }

    }
    delet(){
        // Apagando o ultimo caracter da string
        this.currentOperand = this.currentOperand.toString().slice(0,-1);
    }
    cal(){
        let resul;
        const pervirusOperandfloot = parseFloat(this.pervirusOperand)
        const currentOperandfloot = parseFloat(this.currentOperand)
        if (isNaN(pervirusOperandfloot) || isNaN(currentOperandfloot)) return;
        switch(this.operation){
            case '+':
                resul = pervirusOperandfloot + currentOperandfloot
                break
            case '-':
                resul = pervirusOperandfloot - currentOperandfloot
                break
            case '÷':
                resul = pervirusOperandfloot / currentOperandfloot
                break
            case '*':
                resul = pervirusOperandfloot * currentOperandfloot
                break
            default:
                return
        }
        this.currentOperand = resul
        this.operation = undefined
        this.pervirusOperand = ''

    }
    //Ele e excutado para um sinal de operação 
    chossOperation(operation){
        if (this.currentOperand == '')return
        if (this.pervirusOperand != ''){
            this.cal()
        }
        this.operation = operation
        this.pervirusOperand = this.currentOperand
        this.currentOperand = ""
    }



    appendNumber(number){
        if (this.currentOperand.includes('.') && number == '.')return;

        this.currentOperand = `${this.currentOperand}${number.toString()}`
    }

    // Guardando o valor
    clear(){
        //this mantém o valor undefined em funções globais e em funções anônimas que não estão vinculadas a nenhum objeto
        this.currentOperand = '';
        this.pervirusOperand = '';
        this.operation = undefined;
    }
    // Para atualizar elementos de texto 
    updateDisplay(){
        this.pervirusOperandTextElement.innerText = `${this.pervirusOperand} ${this.operation || ''}`// o sinal || significa ou 
        this.currentOperandTexrElemnt.innerText =this.formatDisplayNumber(this.currentOperand)
    }
}
const calcular = new calculadora(pervirusOperandTextElement,currentOperandTexrElemnt);
// Fazendo aparecer os botão quando clickar
for(const BotoesDONumeros of BotoesDONumero){
    BotoesDONumeros.addEventListener('click', () => {
        calcular.appendNumber(BotoesDONumeros.innerText)
        calcular.updateDisplay()
    })

}
for (const OperacaoDeBotoe of OperacaoDeBotoes){
    OperacaoDeBotoe.addEventListener('click',() =>{
        calcular.chossOperation(OperacaoDeBotoe.innerText)
        calcular.updateDisplay()
    })
}

allclearButton.addEventListener('click',() => {
    calcular.clear()
    calcular.updateDisplay()
})
Igualbotoa.addEventListener('click',()=>{
    calcular.cal()
    calcular.updateDisplay()
})
deletarBotoa.addEventListener('click',()=>{
    calcular.delet()
    calcular.updateDisplay()
})