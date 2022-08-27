// BlockChain 
const sha256 = require('crypto-js/sha256') 

class Bloco{
	constructor(index = 0,previoHash = null, data='Bloco genesis'){
		this.index = index 
		this.previoHash = previoHash 
		this.data = data 
		this.timestamp = new Date() 
		this.hash = this.generateHash() 
	}
	generateHash(){
		return sha256(this.index + this.previoHash + JSON.stringify(this.data) + this.timestamp).toString() 
	}
} 
module.exports = Bloco
