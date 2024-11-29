'use strict'
    const answer = confirm('Should I calculate the square root?');


console.log(answer);

if (answer == true) {
    const numba = prompt('Enter your number');
    if (numba < 0)
        document.querySelector('#result').textContent = "positive numbers only"
    else{
    const numberflt = parseFloat(numba)

    const squared = Math.sqrt(numberflt)
    const numbasqrdstr=squared.toString()
    document.querySelector('#result').textContent = numbasqrdstr
}}
else{
    document.querySelector('#result').textContent = "oke wont do it then"
}

