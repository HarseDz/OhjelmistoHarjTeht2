let name;
'use strict';
const number1str = prompt('Type your number.')
const number2str= prompt('Type your second number.')
const number3str = prompt('Type your third number.')

const number1int = parseInt(number1str)
const number2int = parseInt(number2str)
const number3int = parseInt(number3str)

const sum = number1int+number2int+number3int
const sumstr=sum.toString()

const product = number1int*number2int*number3int
const productstr=product.toString()

const avg = sum/3
const avgstr=avg.toString()

document.querySelector('#target').innerHTML = 'sum:' + sumstr + ' product:' + productstr + ' average:' + avgstr;


