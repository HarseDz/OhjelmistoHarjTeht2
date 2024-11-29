let numerot = [];
        while (true) {
            let num = prompt("anna numero");
            if (numerot.includes(num)) {
                alert("toistunut luku");
                break;}
            numerot.push(num);}

numerot.sort((a, b) => a - b);
        console.log(numerot);

         document.body.innerHTML += `<p>luvut ovat: ${numerot.join(', ')}</p>`;