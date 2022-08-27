const Bloco = require('./bloco') 
// O hash de cada bloco foi gerado corretamente 
// O index dos Blocos está em sequencia 
// Os blocos estao ligados entre si atraves dos hashes 
class BlockChain{
	constructor(){
		this.blocos = [new Bloco()] 
		this.index = 1 
	}
	// Pagar o ultimo bloco adicionado
	getLastBloco(){
		return this.blocos[this.blocos.length - 1] 
	} 
	// Criar um novo bloco 
	addBlock(data){
		const index = this.index 
		const previouHash = this.getLastBloco().hash 
		const bloco = new Bloco(index,previouHash,data) 
		this.index++ 
		this.blocos.push(bloco) 
	}
	isValid(){
		for (let i = 1; i < this.blocos.length;i++){
			const currentBloco = this.blocos[i] 
			const previoBloco = this.blocos[i -1] 
			if (currentBlock.hash !== currentBlock.generateHash()){
				return false 
			} 
			if (currentBloco.previoHash !== previoBloco.hash){
				return false 
			}
		}
		return true 
	}

} 
module.exports = BlockChain 

