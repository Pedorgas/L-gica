function alterarCor(){
    const colores = ["black", "yellow", "green", "orange", "pink", "red", "blue", "purple", "burgundy", "coral", "cyan", "gray"]
    const escolhe = colores[Math.floor(Math.random() * 12)]
    document.body.style.background = escolhe
}
