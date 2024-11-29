'use strict';
const dicenumba = prompt('dice? how many?');
const dicenumbaint = parseInt(dicenumba);
const goalsum = prompt('desired sum?');
const goalsumint = parseInt(goalsum);
let matches = 0;
const rolls = 100000;

if (isNaN(dicenumbaint) || dicenumbaint < 1 || goalsumint < dicenumbaint || goalsumint > dicenumbaint * 6) {
    document.getElementById('result').textContent = "impossible";
// en saa toimimaan jostain syystä?? ^^
}

for (let i = 0; i < rolls; i++) {
    let sum = 0;
    for (let j = 0; j < dicenumbaint; j++) {
        sum += Math.floor(Math.random() * 6) + 1;
    }
    if (sum === goalsumint) {
        matches++;
    }
}

const probability = (matches / rolls) * 100;
document.querySelector('#result').textContent =
    `chance to get ${goalsumint} with ${dicenumbaint} dice is ${probability.toFixed(2)}%`;