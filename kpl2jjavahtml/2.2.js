'use strict';
let lkm=prompt("anna osallistujen lukumäärä");

let osallistujat =[];

for(let i =0; i < lkm; i++) {
    let osallistuja = prompt("anna nimi")
    osallistujat.push(osallistuja);
}
osallistujat=osallistujat.sort();

for(let x = 0; x<osallistujat.length; x++){
    let li=document.createElement("li");
    li.innerText=osallistujat[x];
    document.querySelector("#result").appendChild(li)
}


