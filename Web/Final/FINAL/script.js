let formulario = document.getElementById('formu');

formulario.addEventListener('submit', calcular);

function verificar(){
    let peso = document.getElementById('peso').value;
    let altura = document.getElementById('altura').value;

    if (parseFloat(peso)!==null || parseFloat(altura)!==null){
        return true;
    }else{
        return false;
    }
}

function calcular(e){
    e.preventDefault();

    if (verificar()){
        let peso = document.getElementById('peso').value;
        let altura = document.getElementById('altura').value;

        
    }
}