"use strict";

//мб надо в отдельный класс зафигачить

function login(event) {

    let user = {
        name: document.getElementById('name'),
        password: document.getElementById('password')
    }

    let response = fetch('/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(user)
    });

    if (response.ok) {
        let json = response.json();
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

function register(event) {
    alert('register')
}



