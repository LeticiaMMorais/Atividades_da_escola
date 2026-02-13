const botao = document.getElementById("btn-toggle")
const body = document.body

botao.addEventListener("click", function () {
    body.classList.toggle('dark-mode')
} )