'use strict';
let articleList = document.getElementById("result");

const showForm=document.querySelector("#show-form")
showForm.addEventListener('submit',async function(event){
    event.preventDefault();
    const value