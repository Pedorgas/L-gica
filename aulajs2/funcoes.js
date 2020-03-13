alert("theres this tale of a scientist named Rick, but then, an mysterious accident occours, and he turns himself into an pickle, he is now Pickle Rick, funniest shit i've ever seen." )

function numeroLegal(valor) {
    //se for par e maior que 100
    return valor % 2 == 0 && valor > 100
}

console.log("numero legal - 50, 150, 151")
console.log(numeroLegal(50))
console.log(numeroLegal(150))
console.log(numeroLegal(151))

function numeroChato(valor) {
    //se for impar ou menor que 70
    return valor % 2 == 1 || valor < 70
}

console.log("Numero Chato - 66, 76, 77")
console.log(numeroChato(66))
console.log(numeroChato(76))
console.log(numeroChato(77))

frutas = ["banana", "pera", "laranja", "kiwi"]
for(fruta of frutas){
    console.log(fruta)
}
console.log(frutas.indexOf("pera"))
console.log(frutas.indexOf("Maçã"))

console.log("USANDO FOR")
for(var i = 0; i < 10; i++){
    console.log(i)
}

console.log("USANDO WHILE")
var i = 0
while(i < 10){
    console.log(i)
    i += 1
}

function mostrarData() {
    console.log(new Date())
}

mostrarData()
//setInterval(mostrarData, 2000)
//não dá pra misturar Interval e Timeout.
setTimeout(mostrarData, 5000)
