
'use strict';
let luvut = [];
for (let i = 0; i < 5; i++) {
    const num = prompt(`anna luku`);
    luvut.push(num);}
for (let i = 4; i >= 0; i--) {
    console.log(luvut[i]);}
let reversed = [];
for (let i = 4; i >= 0; i--) {
    reversed.push(luvut[i]);
}
document.querySelector('#tulos').textContent = reversed