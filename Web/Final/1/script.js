let presupuesto = document.getElementById('presupuesto');

presupuesto.addEventListener('submit', calcular);

function calcular(e){
    e.preventDefault();

    let ingreso = document.getElementById('ingresos').value;
        gastoE = document.getElementById('gastosE').value;
        gastoT = document.getElementById('gastosT').value;
        gastoC = document.getElementById('gastosC').value;

    let gastos = parseInt(gastoE)+parseInt(gastoC)+parseInt(gastoT);
    let total = ingreso-gastos;

    mostrar(total);
}

function mostrar(total){
    let resultado = document.getElementById('resultado');
    resultado.innerHTML = '';
    let verResultado = document.createElement('h2');
    verResultado.innerHTML = 'Resultado: ';
    let numero = document.createElement('span');
    numero.innerHTML = total;
    

    if (total>0){
        numero.style.color='green';
    }else{
        numero.style.color='red';
    }

    verResultado.appendChild(numero);
    resultado.appendChild(verResultado);
    resultado.classList.add('resultado-numero')

    reset()
}

function reset(){
    document.getElementById('presupuesto').reset();
}


