
function enviardados() {

    if (document.dados.tx_nome.value == "" ||
        document.dados.tx_nome.value.length < 8) {
        alert("Preencha campo NOME corretamente!");
        document.dados.tx_nome.focus();
        return false;
    }


    if (document.dados.tx_email.value == "" ||
        document.dados.tx_email.value.indexOf('@') == -1 ||
        document.dados.tx_email.value.indexOf('.') == -1) {
        alert("Preencha campo E-MAIL corretamente!");
        document.dados.tx_email.focus();
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