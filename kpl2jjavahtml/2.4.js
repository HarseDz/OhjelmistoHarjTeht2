'use strict';

        let numerot = [];

        while (true) {
            let num = prompt("Enter a number (0 to stop):");
            num = parseInt(num);

            if (num === 0) break;
            numerot.push(num);
        }

        numerot.sort((a, b) => b - a);

        numerot.forEach(num => {
            let li = document.createElement("li");
            li.innerText = num;
            document.querySelector("#lista").appendChild(li);
        });