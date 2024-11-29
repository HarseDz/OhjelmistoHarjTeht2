'use strict'
let koirat = [];

for (let i = 1; i <= 6; i++) {
    let nimi = prompt("Anna koiran nimi " + i);
    koirat.push(nimi);
}
koirat = koirat.sort().reverse();

for (let i = 0; i < koirat.length; i++) {
    let li = document.createElement("li");
            li.innerText = koirat[i];
            document.querySelector("#lista").appendChild(li);
}

