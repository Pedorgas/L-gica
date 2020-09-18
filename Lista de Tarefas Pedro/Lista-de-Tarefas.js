let atividades = ["Ver se tem tarefa", "Fazer Tarefa","So isso por enquanto"]

function botaoExcluir(atividade){
    let botaoExcluir = document.createElement("button")
    const texto = document.createTextNode("Excluir")
    const pos = atividades.indexOf(atividade)
    botaoExcluir.setAttribute("href", "#")
    botaoExcluir.setAttribute("onclick", `excluirAtividade("${pos}")`)
    botaoExcluir.appendChild(texto)
    return botaoExcluir
}

function listarTarefas(){
    const listaTarefas = document.getElementById('listaTarefas')
    listaTarefas.innerHTML = ""
    for (atividade of atividades) {
        const novoItem = document.createElement("li")
        listaTarefas.appendChild(novoItem)
        const novoTexto = document.createTextNode(atividade)
        novoItem.appendChild(novoTexto)
        novoItem.appendChild(botaoExcluir(atividade))
    }
}

function excluirAtividade(pos){
    atividades.splice(pos, 1)
    listarTarefas()
}

function adicionarTarefa(){
    const novoItem = document.getElementById("novo_item").value
    atividades.push(novoItem)
    listarTarefas()
}

listarTarefas()