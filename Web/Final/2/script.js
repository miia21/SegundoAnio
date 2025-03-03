let formulario = document.getElementById('registro');

formulario.addEventListener('submit', verificar);

function verificarUsuario(){
    let usuario=document.getElementById('usuario').value.toLowerCase();
    const nombres=['ana', 'pedro', 'jose'];

    if (nombres.includes(usuario)){
        document.getElementById('errorUs').innerText='Nombre ya existente';
        return false;
    }else{
        document.getElementById('errorUs').innerText = '';
        return true;
    }
}

function verificarContra(){
    let contra=document.getElementById('contra').value;

    if (contra.length<8){
        document.getElementById('errorContra').innerText='Contraseña corta';
        return false;
    }else{
        document.getElementById('errorContra').innerText = '';
        return true;
    }
}

function verificarRepContra(){
    let contra=document.getElementById('contra').value;
    let repContra= document.getElementById('repContra').value;

    if (contra!==repContra){
        document.getElementById('errorRepContra').innerText='No coinciden';
        return false;
    }else{
        document.getElementById('errorRepContra').innerText = '';
        return true;
    }
}

function verificar(e){
    e.preventDefault();

    let usuario= verificarUsuario();
    let contra = verificarContra();
    let repContra= verificarRepContra();
    let resultado= document.getElementById('resultado');
    resultado.innerHTML='';
    let mostrar= document.createElement('h2');

    if (usuario && contra && repContra){
        mostrar.innerHTML='Exito';
        resultado.appendChild(mostrar);
    }else{
        mostrar.innerHTML='No exito';
        resultado.appendChild(mostrar);
    }

    reset()
}

function reset(){
    document.getElementById('registro').reset();
}