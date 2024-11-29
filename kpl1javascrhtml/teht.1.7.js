'use strict'
            const dice =  prompt('how many dice?');
            let sum = 0;

            if (dice < 1) {
                document.getElementById('result').textContent = "need atleast 1 dice";
            }
            else{
            for (let i = 0; i < dice; i++) {
                const roll = Math.floor(Math.random() * 6) + 1;
                sum += roll;
                document.querySelector('#result').textContent = sum
            }}


