
function checkValid1(mail,note1){
    const inpObj = document.getElementById(mail);
    if (!inpObj.checkValidity()) {
    document.getElementById(note1).innerHTML = inpObj.validationMessage;
    }   
}

function checkValid2(com,note2){
    const inpObj = document.getElementById(com);
    if (!inpObj.checkValidity()) {
    document.getElementById(note2).innerHTML = inpObj.validationMessage;
    }   
}
