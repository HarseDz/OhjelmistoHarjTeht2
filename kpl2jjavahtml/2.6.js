 function noppa() {
            return Math.floor(Math.random() * 6) + 1;
        }

        let result;
        do {
            result = noppa();
            let li = document.createElement('li');
            li.textContent = result;
            document.getElementById('lista').appendChild(li);
        } while (result !== 6);