
function enviardados() {

    if ( document.getElementById("txtNome").value == "" ||
        document.getElementById("txtNome").value.length < 8) {
        alert("Preencha campo NOME corretamente!");
        document.getElementById("txtNome").focus();
        return false;
    }


    if (document.getElementById("txtEmail").value == "" ||
        document.getElementById("txtEmail").value.indexOf('@') == -1 ||
        document.getElementById("txtEmail").value.indexOf('.') == -1) {
        alert("Preencha campo E-MAIL corretamente!");
        document.getElementById("txtEmail").focus();
        return false;
    }

    if (document.dados.tx_mensagem.value == "") {
        alert("Preencha o campo MENSAGEM!");
        document.dados.tx_mensagem.focus();
        return false;
    }

    if (document.dados.tx_mensagem.value.length < 50) {
        alert("É necessario preencher o campo MENSAGEM com mais de 50 caracteres!");
        document.dados.tx_mensagem.focus();
        return false;
    }
    return true;
}