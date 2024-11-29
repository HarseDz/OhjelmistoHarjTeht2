
        function noppa(sides) {
            return Math.floor(Math.random() * sides) + 1;
        }
        let sides = parseInt(prompt("how many sides on the dice?"));

        let result;
        do {
            result = noppa(sides);
            let li = document.createElement('li');
            li.textContent = result;
            document.getElementById('lista').appendChild(li);
        } while (result !== sides);