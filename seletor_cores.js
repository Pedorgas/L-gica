function alterarCor() {
    const Vermelho = document.getElementById('Vermelho').value,
        Verde = document.getElementById('Verde').value,
        Azur = document.getElementById('Azur').value

    document.getElementById('Result').value = "(" + Vermelho + ", " + Verde + ", " + Azur + ")"

        document.body.style.background = 'rgb(' + Vermelho + ', ' + Verde + ', ' + Azur + ')' 
}

alterarCor()