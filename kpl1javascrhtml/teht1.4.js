

'use strict'
    const name = prompt('Enter your name.');

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const house = getRandomInt(4);
let housena
if (house == 0) {
    housena = `Slytherin.`;
} else if (house == 1) {
    housena = `Gryffindor.`;
} else if (house == 2) {
    housena = `Hufflepuff.`;
} else if (house == 3) {
    housena = `Ravenclaw.`;
}

document.querySelector('#result').innerHTML = housena