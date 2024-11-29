'use strict'
    const numba = prompt('Enter your year');


let number
if ((numba % 4 === 0 && numba % 100 !== 0) || (numba % 400 === 0)){
    number = `yes leap`;
} else  {
    number = `not leap`;
}


document.querySelector('#result').textContent = number