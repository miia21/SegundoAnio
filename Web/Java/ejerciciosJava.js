function ejVar() {
    var x = 5;
    if (x == 5) {
        var x = 6;
        console.log(x);     // 6
    }
    console.log(x);         // 6
}

function ejLet() {
    let x = 5;
    if (x == 5) {
        let x = 6;
        console.log(x);     // 6
    }
    console.log(x);         // 5
}

function ejConst() {
    const x = 5;
    //const x = 6;          // Error
}

//Ejemplo 1
console.log(a);     // undefined
var a = 10;
console.log(a);     // 10

//Ejemplo 2
var a;              // Declaración hoisteada
console.log(a);     // undefined
a = 10;             // Asignación
console.log(a);     // 10

//Funcion
function numero(num) {
    var x = num + 5;
    console.log(x);
}
numero(5);      // 10

//Funcion con return
function numero(num) {
    var x = num + 5;
    return x;
}
console.log(numero(5));     // 10

//Funcion anonima
let numero = function(num) {
    var x = num + 5;
    console.log(x);
}
numero(5);      // 10

//Funcion flecha
let numero = (num) => num + 5;
console.log(numero(5));     // 10

//Funcion de orden superior
function apOperacion(num, operacion) {
    return operacion(num);
}
let numero = apOperacion(5, (num) => num + 5);
console.log(numero);     // 10

//Funcion como metodo
let numero = {
    num: 5,
    suma: function() {
        return this.num + 5;
    }
}
numero.suma();     // 10

//Funcion recursiva
function numero(num) {
    if (num >= 10) {
        return 0;
    } else {
        return 1 + numero(num + 1);
    }
}
console.log(numero(5));     // 10

//Array
let numeros = [1, 2, 3, 4, 5, 6, 11, 23, 1, 989, 0, 1, 111, 645, 50, 45];

//Retornar el menor elemento
let menor = numeros.reduce((menor, num) => num < menor ? num : menor);

//Retornar la suma de los elementos
let suma = numeros.reduce((suma, num) => suma + num);

//Retornar el doble de los elementos
let doble = numeros.map(num => num * 2);

//Retornar los elementos mayores o iguales a 10
let mayores = numeros.filter(num => num >= 10);

//Retornar el indice del primer elemento mayor a 10 (si existe)
let indice = numeros.findIndex(num => num > 10);

//Objeto
function Auto(ruedas, puertas, color, velocidad){
    this.ruedas = ruedas;
    this.puertas = puertas;
    this.color = color;
    this.velocidad = velocidad;
    this.acelerar = function(){
        this.velocidad += 10;
    }
}